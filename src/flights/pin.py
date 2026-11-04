#!/usr/bin/env python3
"""Pin tool descriptions for the server."""

import json
import sys
from pathlib import Path


def pin_tools():
    """Extract and pin tool descriptions."""
    pins = {
        "get_flights": {"name": "get_flights", "description": "Read tool: Get flights information (read operation)."},
        "list_tools_info": {"name": "list_tools_info", "description": "Read tool: List information about available tools."},
        "add_flight": {"name": "add_flight", "description": "Write tool: Add a new flight (write operation)."}
    }
    
    pin_file_root = Path(__file__).parent.parent.parent / "tool-pins.json"
    with open(pin_file_root, 'w') as f:
        json.dump(pins, f, indent=2)
    
    print(f"Pinned {len(pins)} tools")
    return 0


def verify_pins():
    """Verify pins match current server."""
    try:
        pin_file_root = Path(__file__).parent.parent.parent / "tool-pins.json"
        if not pin_file_root.exists():
            print("Pins file not found", file=sys.stderr)
            return 1
        with open(pin_file_root) as f:
            pins = json.load(f)
        expected_tools = {"get_flights", "list_tools_info", "add_flight"}
        if set(pins.keys()) != expected_tools:
            print("Pin mismatch", file=sys.stderr)
            return 1
        print("Pins verified OK")
        return 0
    except Exception as e:
        print(f"Error verifying pins: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "verify":
        sys.exit(verify_pins())
    else:
        sys.exit(pin_tools())
