#!/usr/bin/env python3
"""Adversarial client for E5 - tests server hardening."""

import json
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from flights import auth
from flights import server
from flights.auth import create_token, UnauthorizedError, InsufficientScopeError


def test_adversarial_attacks():
    """Run adversarial tests."""
    results = []
    
    # Test 1: Read token tries to call write tool - should get 403
    try:
        read_token = create_token("adversary1", ["read:flights"], audience="flights-mcp-server")
        os.environ['MCP_TOKEN'] = read_token
        try:
            server.check_authorization("add_flight")
            results.append({"test": "read_token_write", "result": "FAIL - should have been denied"})
        except InsufficientScopeError as e:
            results.append({"test": "read_token_write", "result": "PASS - got 403 insufficient_scope", "error": str(e)})
    except Exception as e:
        results.append({"test": "read_token_write", "result": f"ERROR: {e}"})
    
    # Test 2: Wrong audience gets 401
    try:
        bad_aud_token = create_token("adversary2", ["write:flights"], audience="wrong-audience")
        os.environ['MCP_TOKEN'] = bad_aud_token
        try:
            server.check_authorization("add_flight")
            results.append({"test": "wrong_audience", "result": "FAIL - should have been denied"})
        except UnauthorizedError as e:
            results.append({"test": "wrong_audience", "result": "PASS - got 401", "error": str(e)})
    except Exception as e:
        results.append({"test": "wrong_audience", "result": f"ERROR: {e}"})
    
    # Test 3: Scope claimed in argument/body/header changes nothing
    try:
        read_token = create_token("adversary3", ["read:flights"])
        os.environ['MCP_TOKEN'] = read_token
        # Try to inject scope via args
        try:
            server.check_authorization("add_flight", scope="write:flights", scopes=["write:flights"])
            results.append({"test": "scope_in_args", "result": "FAIL - scope injection worked"})
        except InsufficientScopeError:
            results.append({"test": "scope_in_args", "result": "PASS - scope in args ignored"})
    except Exception as e:
        results.append({"test": "scope_in_args", "result": f"ERROR: {e}"})
    
    # Test 4: Tool not in table refused
    try:
        write_token = create_token("adversary4", ["write:flights"])
        os.environ['MCP_TOKEN'] = write_token
        try:
            server.check_authorization("admin_delete_all")
            results.append({"test": "tool_not_in_table", "result": "FAIL - should be refused"})
        except (InsufficientScopeError, Exception):
            results.append({"test": "tool_not_in_table", "result": "PASS - tool not in table refused"})
    except Exception as e:
        results.append({"test": "tool_not_in_table", "result": f"ERROR: {e}"})
    
    return results


if __name__ == "__main__":
    results = test_adversarial_attacks()
    print(json.dumps(results, indent=2))
