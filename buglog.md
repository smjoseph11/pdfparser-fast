---
name: "\U0001F41E Bug Report"
labels: kind/bug, status/triage
---

## Issue

  ```Installing psycopg2 (2.9.9): Failed

  ChefBuildError

  Backend subprocess exited when trying to invoke get_requires_for_build_wheel

  running egg_info
  writing psycopg2.egg-info/PKG-INFO
  writing dependency_links to psycopg2.egg-info/dependency_links.txt
  writing top-level names to psycopg2.egg-info/top_level.txt

  Error: pg_config executable not found.
  Note: This error originates from the build backend, and is likely not a problem with poetry but with psycopg2 (2.9.9) not supporting PEP 517 builds. You can verify this by running 'pip wheel --no-cache-dir --use-pep517 "psycopg2 (==2.9.9)"'.
```
### Solution

This issue arises because psycopg is a wrapper for the libpq library. This dependency must be installed first.
```
sudo apt install libpq-dev
```
We can now run
```
poetry install
```