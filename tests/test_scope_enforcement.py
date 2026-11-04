"""Tests for scope enforcement."""

import unittest
import os
import json
import tempfile
from pathlib import Path

from src.flights import auth
from src.flights import scopes
from src.flights.auth import create_token, verify_token, UnauthorizedError, InsufficientScopeError
from src.flights import server


class TestScopeEnforcement(unittest.TestCase):
    def setUp(self):
        # Clear env
        for key in ['MCP_TOKEN', 'FLIGHTS_TOKEN']:
            if key in os.environ:
                del os.environ[key]
    
    def test_wrong_audience_gets_401(self):
        """Token with the wrong audience gets 401."""
        token = create_token("user1", ["write:flights"], audience="wrong-audience")
        with self.assertRaises(UnauthorizedError):
            verify_token(token)
    
    def test_read_token_insufficient_scope_on_write(self):
        """A read token gets 403 insufficient_scope on the write tool before the function runs."""
        read_token = create_token("reader", ["read:flights"])
        os.environ['MCP_TOKEN'] = read_token
        with self.assertRaises(InsufficientScopeError):
            server.check_authorization("add_flight")
    
    def test_scope_in_args_does_not_change_authorization(self):
        """Scope claimed in the body, a header, or an argument changes nothing."""
        read_token = create_token("reader", ["read:flights"])
        os.environ['MCP_TOKEN'] = read_token
        # Try to pass scope in args - should be ignored
        with self.assertRaises(InsufficientScopeError):
            server.check_authorization("add_flight", scopes=["write:flights"], scope="write:flights")
    
    def test_scope_in_kwargs_does_not_change_authorization(self):
        """Scope claimed in argument changes nothing."""
        read_token = create_token("reader", ["read:flights"])
        os.environ['MCP_TOKEN'] = read_token
        with self.assertRaises(InsufficientScopeError):
            server.check_authorization("add_flight", write_scope="write:flights")
    
    def test_tool_not_in_table_refused(self):
        """A tool not in the table is refused."""
        write_token = create_token("writer", ["write:flights"])
        os.environ['MCP_TOKEN'] = write_token
        with self.assertRaises(InsufficientScopeError):
            server.check_authorization("delete_everything")
    
    def test_refusal_logged_with_sub_and_tool(self):
        """Each refusal writes a log line with sub and tool."""
        read_token = create_token("badreader", ["read:flights"])
        os.environ['MCP_TOKEN'] = read_token
        log_file = Path(server.__file__).parent / "server.log"
        # Don't delete if locked, just append and check
        try:
            server.check_authorization("add_flight")
        except InsufficientScopeError:
            pass
        self.assertTrue(log_file.exists())
        with open(log_file) as f:
            content = f.read()
        self.assertIn("add_flight", content)
        self.assertIn("badreader", content)


if __name__ == "__main__":
    unittest.main()
