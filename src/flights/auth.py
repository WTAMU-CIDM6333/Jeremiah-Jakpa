"""Token verification for MCP server."""

import json
import hmac
import hashlib
import base64
from typing import Dict, Any, Optional, List

from .scopes import TOKEN_SECRET, VALID_AUDIENCE


class AuthError(Exception):
    """Authentication/authorization error."""
    pass


class UnauthorizedError(AuthError):
    """401 - token with wrong audience or invalid token."""
    pass


class InsufficientScopeError(AuthError):
    """403 - read token gets insufficient scope on write tool."""
    pass


def create_token(subject: str, scopes: List[str], audience: str = VALID_AUDIENCE) -> str:
    """Create a signed token (for testing)."""
    payload = {
        "sub": subject,
        "scopes": scopes,
        "aud": audience
    }
    payload_bytes = json.dumps(payload, sort_keys=True).encode('utf-8')
    payload_b64 = base64.urlsafe_b64encode(payload_bytes).decode('utf-8').rstrip('=')
    signature = hmac.new(TOKEN_SECRET.encode('utf-8'), payload_bytes, hashlib.sha256).hexdigest()
    return f"{payload_b64}.{signature}"


def verify_token(token: str) -> Dict[str, Any]:
    """Verify token and return payload. Raises UnauthorizedError if invalid/wrong audience."""
    try:
        if not token or '.' not in token:
            raise UnauthorizedError("Invalid token")
        payload_b64, signature = token.split('.')
        # Add padding if needed
        padding = 4 - len(payload_b64) % 4
        if padding != 4:
            payload_b64_padded = payload_b64 + '=' * padding
        else:
            payload_b64_padded = payload_b64
        payload_bytes = base64.urlsafe_b64decode(payload_b64_padded)
        expected_sig = hmac.new(TOKEN_SECRET.encode('utf-8'), payload_bytes, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, expected_sig):
            raise UnauthorizedError("Invalid token signature")
        payload = json.loads(payload_bytes.decode('utf-8'))
        if payload.get('aud') != VALID_AUDIENCE:
            raise UnauthorizedError("Invalid audience")
        return payload
    except UnauthorizedError:
        raise
    except Exception as e:
        raise UnauthorizedError(f"Token verification failed: {e}")
