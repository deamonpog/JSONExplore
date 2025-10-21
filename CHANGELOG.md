# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-10-20

### Changed

⚠️ **BREAKING CHANGE: Package Renamed**

- **Package name changed from `json-scout` to `json-anatomy`**
  - Distribution name: `json-scout` → `json-anatomy`
  - Import name: `jsonscout` → `jsonanatomy`
  - Recommended alias: `js` → `ja`
  
- **All URLs updated**:
  - PyPI: https://pypi.org/project/json-anatomy/
  - Documentation: https://deamonpog.github.io/json-anatomy/
  - Repository: https://github.com/deamonpog/json-anatomy

- **Migration required for existing users**:
  - See [MIGRATION.md](MIGRATION.md) for complete migration guide
  - All functionality remains identical
  - Only package and import names changed

### API Improvements (from previous versions)

- Standardized data access with `.data` attribute and `.value()` method across all classes
- Renamed methods for better usability:
  - `get_child_keys()` → `keys()`
  - `explore_child()` → `child()`
  - `invest_grandchildren()` → `field_counts()`

### Documentation

- Added comprehensive [Migration Guide](MIGRATION.md)
- Updated all documentation with new package name
- Updated code examples to use `import jsonanatomy as ja`

### Infrastructure

- Updated GitHub Actions workflows to latest versions
- Modernized all deprecated action dependencies
- Enhanced build and publish automation

## [Pre-rename versions as json-scout]

Previous versions were published under the package name `json-scout` with import name `jsonscout`.

### Initial Features

- **Explore**: Lightweight structural analysis of JSON objects
- **Maybe**: Monadic wrapper for safe, exception-free navigation
- **SimpleXML**: Efficient XML-to-dictionary conversion
- **Xplore**: Unified interface combining all functionality
- **File Operations**: Robust JSON file discovery and loading
- Full type annotations with `py.typed`
- Comprehensive NumPy-style docstrings
- Complete API documentation with MkDocs

---

## Migration from json-scout

If you're upgrading from `json-scout` (any version):

```bash
pip uninstall json-scout
pip install json-anatomy
```

Then update your imports:
```python
# Old
import jsonscout as js

# New
import jsonanatomy as ja
```

See [MIGRATION.md](MIGRATION.md) for detailed instructions.

---

[0.1.0]: https://github.com/deamonpog/json-anatomy/releases/tag/v0.1.0
