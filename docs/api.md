# API Reference

This page is generated automatically from your docstrings via **mkdocstrings**.

> Tip: Keep your docstrings in Google or NumPy style so signatures & types render cleanly.

---

## Top-Level API

The `jsonexplore` package exposes its main entry points here (re-exported in `__init__.py`):

::: jsonexplore
    options:
      show_root_heading: true
      show_root_full_path: false
      members_order: source
      filters:
        - "!^_"         # hide private members
        - "!^__"        # hide dunder methods

---

## Modules

### `file_reader` — File utilities
Low-level helpers to find and read JSON files.

::: jsonexplore.file_reader
    options:
      members:
        - get_json_file_paths
        - read_json_file

### `Explore` — Lightweight structural explorer
Wrapper to inspect children and “grandchildren” of dict/list JSON structures.

::: jsonexplore.Explore

### `Maybe` — Safe access wrapper
Monadic-style wrapper for optional traversal over dicts/lists.

::: jsonexplore.Maybe

### `SimpleXML` — Tiny XML → dict helper
Convenience class to parse a small XML string and convert to nested dicts.

::: jsonexplore.SimpleXML

### `Xplore` — Unified convenience facade
One entry object that wires `Explore`, `Maybe`, and `SimpleXML` together.

::: jsonexplore.Xplore
