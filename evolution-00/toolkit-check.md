# Toolkit Check

Verified on 2026-09-20.

## Installed Toolkit

| Tool | Version or model |
| --- | --- |
| uv | 0.12.17 |
| Python | 3.14.2 |
| gzkit | 0.34.7 |
| Visual Studio Code | 1.137.0 (x64) |
| Git | 2.52.0.windows.1 |
| Ollama | 0.34.0 |
| Ollama model | llama3.2:3b |
| Harness: OpenCode | 1.18.21 |

`py-gzkit` was installed with `uv tool install py-gzkit`. OpenCode is the selected harness for this toolkit check.

## Required Command Output

### `gz --version`

```text
gzkit 0.34.7
```

### `ollama list`

```text
NAME           ID              SIZE      MODIFIED
llama3.2:3b    a80c4f17acd5    2.0 GB    17 seconds ago
```

### `opencode --version`

```text
1.18.21
```

## Additional Verification

```text
> uv --version
uv 0.12.17 (635500036 2026-09-18 x86_64-pc-windows-msvc)

> python --version
Python 3.14.2

> git --version
git version 2.52.0.windows.1

> code --version
1.137.0
645f29cc3176500b4b5762ba887cf2a7f0ffdf2c
x64

> ollama --version
ollama version is 0.34.0
```

The installed `llama3.2:3b` model was also run locally and successfully returned the requested test response, `MODEL OK`.
