# E1 evidence

No flight evidence exists yet. After committed Chase GO, capture two independent
session exports with `opencode export <sessionID> --sanitize`. The planned names
are `tp1.sanitized.json` and `tp2.sanitized.json`.

Never commit raw exports. Preserve sanitized exports exactly as produced; record
their SHA-256 hashes and session IDs in the flight log. Commentary and arithmetic
checks belong in the log, not inside the exported JSON. These instructions are
procedural; a filename does not mechanically prove that an export was sanitized.
