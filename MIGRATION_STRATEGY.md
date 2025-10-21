# Migration Warning Strategy for json-scout Users

## Overview

Comprehensive warning system implemented to notify users about the package rename from `json-scout` to `json-anatomy`.

---

## Warning Locations

### 1. ✅ README.md (GitHub Landing Page)
**Location**: Top of file, immediately after badges  
**Format**: Blockquote with warning emoji  
**Content**: 
```markdown
> **⚠️ MIGRATION NOTICE**: This package was previously named `json-scout`. 
> If you're upgrading from `json-scout`, please see the [Migration Guide](MIGRATION.md) 
> for instructions on updating your code.
```

### 2. ✅ MIGRATION.md (Detailed Guide)
**Location**: Root directory  
**Purpose**: Complete migration instructions  
**Includes**:
- Why the change was made
- Step-by-step migration instructions
- Code examples (before/after)
- Requirements file updates
- Migration scripts for automated updates
- Help/support resources

### 3. ✅ Documentation Website (docs/index.md)
**Location**: Top of documentation homepage  
**Format**: MkDocs admonition (warning box)  
**Content**: Visible warning box with quick migration steps + link to full guide

### 4. ✅ Package Docstring (src/jsonanatomy/__init__.py)
**Location**: Module-level docstring  
**Purpose**: Warning visible in Python help() and IDE documentation  
**Content**: Migration notice with link to GitHub guide

### 5. ✅ CHANGELOG.md
**Location**: Root directory  
**Purpose**: Document the breaking change  
**Content**: 
- Version 0.1.0 entry
- Clear "BREAKING CHANGE" label
- Migration instructions
- Link to detailed guide

---

## Files Created/Modified

### New Files
1. **MIGRATION.md** - Complete migration guide
2. **CHANGELOG.md** - Version history with migration notice

### Modified Files
1. **README.md** - Added prominent migration notice
2. **docs/index.md** - Added warning admonition box
3. **src/jsonanatomy/__init__.py** - Updated docstring with migration notice

---

## User Experience Flow

### For New Users
1. See "JSON Anatomy" name everywhere
2. Install: `pip install json-anatomy`
3. Import: `import jsonanatomy as ja`
4. Notice migration warning (optional context)

### For Existing json-scout Users

#### Discovery Path 1: PyPI
1. Search for "json-scout" on PyPI
2. See package (if still published) with deprecation warning
3. Click link to json-anatomy
4. See migration notice on PyPI page

#### Discovery Path 2: GitHub
1. Visit repository
2. See prominent warning at top of README
3. Click MIGRATION.md link
4. Follow step-by-step instructions

#### Discovery Path 3: Import Error
1. Code fails: `ModuleNotFoundError: No module named 'jsonscout'`
2. Search for error or check GitHub
3. Find migration notice
4. Follow migration guide

#### Discovery Path 4: Documentation
1. Visit documentation website
2. See prominent warning box at top
3. Click migration guide link
4. Follow instructions

---

## Migration Scripts Provided

### Linux/macOS
```bash
#!/bin/bash
pip uninstall json-scout -y
pip install json-anatomy
find . -name "*.py" -type f -exec sed -i 's/import jsonscout/import jsonanatomy/g' {} +
```

### Windows (PowerShell)
```powershell
pip uninstall json-scout -y
pip install json-anatomy
Get-ChildItem -Filter *.py -Recurse | ForEach-Object {
    (Get-Content $_) -replace 'import jsonscout','import jsonanatomy' | Set-Content $_
}
```

---

## Next Steps for PyPI Publication

### Option 1: Deprecate json-scout on PyPI
1. Publish one final version of json-scout (0.1.1)
2. Add deprecation warning that prints on import
3. Update PyPI description to redirect to json-anatomy
4. Mark as deprecated using PyPI classifiers

**Example deprecation code for json-scout 0.1.1:**
```python
import warnings
warnings.warn(
    "The 'json-scout' package has been renamed to 'json-anatomy'. "
    "Please uninstall json-scout and install json-anatomy instead. "
    "See https://github.com/deamonpog/json-anatomy/blob/main/MIGRATION.md",
    DeprecationWarning,
    stacklevel=2
)
```

### Option 2: Yank json-scout from PyPI
1. Use PyPI's "yank" feature to mark old versions
2. Prevents new installations but allows existing users to continue
3. Add link to json-anatomy in yank message

### Option 3: Abandon json-scout
1. Simply don't publish updates to json-scout
2. Users will discover the rename organically
3. All warnings in json-anatomy guide them

---

## Communication Checklist

- [x] Migration guide created (MIGRATION.md)
- [x] README warning added
- [x] Documentation warning added
- [x] Package docstring updated
- [x] CHANGELOG created
- [ ] Publish json-anatomy to PyPI
- [ ] Update GitHub repository description
- [ ] Create GitHub release with migration notes
- [ ] (Optional) Publish deprecated json-scout version with warnings
- [ ] (Optional) Post announcement in relevant forums/channels
- [ ] (Optional) Send email to known users (if applicable)

---

## Key Messages

1. **Functionality unchanged** - Only names changed
2. **Easy migration** - Simple find-replace in most cases
3. **Scripts provided** - Automated migration available
4. **Support available** - GitHub issues for help
5. **Better name** - More descriptive of package purpose

---

## Testing the Warnings

Before publishing:

1. **Build documentation**: `mkdocs build` - verify warning displays
2. **Check README**: View on GitHub - verify warning is prominent
3. **Test import help**: `python -c "import jsonanatomy; help(jsonanatomy)"` - verify docstring
4. **Review CHANGELOG**: Ensure migration section is clear
5. **Validate links**: All migration guide links work

---

## Success Metrics

- Users discover migration path quickly
- Minimal GitHub issues about "can't find json-scout"
- Smooth transition with minimal confusion
- Clear upgrade path documented and accessible

---

## Files Reference

```
JSONExplore/
├── MIGRATION.md           ← Detailed migration guide
├── CHANGELOG.md           ← Version history with migration notice
├── README.md              ← Prominent warning at top
├── docs/
│   └── index.md          ← Warning admonition box
└── src/
    └── jsonanatomy/
        └── __init__.py    ← Docstring migration notice
```
