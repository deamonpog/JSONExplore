# API Reference

This comprehensive API reference is automatically generated from the source code docstrings using **mkdocstrings**. All classes, methods, and functions are documented with complete parameter descriptions, return values, and usage examples following NumPy documentation standards.

---

## Package Overview

The `jsonscout` package provides a comprehensive suite of tools for JSON data structure exploration, safe navigation, and analysis. All primary components are available through the main package namespace for convenient access.

::: jsonscout
    options:
      show_root_heading: true
      show_root_full_path: false
      members_order: source
      filters:
        - "!^_"         # hide private members
        - "!^__"        # hide dunder methods

---

## Core Modules

### File Operations Module

The `file_reader` module provides essential utilities for locating and loading JSON data files from the filesystem with robust error handling and encoding support.

::: jsonscout.file_reader
    options:
      members:
        - get_json_file_paths
        - read_json_file

### Structural Exploration Module

The `Explore` class offers lightweight structural analysis capabilities for JSON objects, enabling inspection of nested hierarchies and statistical analysis of data schemas.

::: jsonscout.Explore

### Safe Access Module  

The `Maybe` class implements a monadic pattern for safe, exception-free navigation through potentially incomplete or malformed JSON structures, supporting chainable operations.

::: jsonscout.Maybe

### XML Processing Module

The `SimpleXML` class provides efficient XML-to-dictionary conversion capabilities for integrating XML data sources into JSON-based workflows.

::: jsonscout.SimpleXML

### Unified Interface Module

The `Xplore` class serves as a comprehensive facade that combines the functionality of all core modules into a single, intuitive interface for streamlined JSON exploration workflows.

::: jsonscout.Xplore