# Migration Guide: json-scout → json-anatomy

## ⚠️ IMPORTANT NOTICE

**The package has been renamed from `json-scout` to `json-anatomy`.**

If you previously installed `json-scout`, please update to the new package name.

---

## Why the Change?

The package has been rebranded to better reflect its purpose of dissecting and analyzing JSON structures, similar to how anatomical analysis examines biological structures in detail.

---

## Migration Steps

### 1. Uninstall the Old Package

```bash
pip uninstall json-scout -y
```

### 2. Install the New Package

```bash
pip install json-anatomy
```

### 3. Update Your Import Statements

**Before (json-scout):**
```python
import jsonscout as js

explorer = js.Xplore(data)
explore = js.Explore(data)
maybe = js.Maybe(data)
```

**After (json-anatomy):**
```python
import jsonanatomy as ja

explorer = ja.Xplore(data)
explore = ja.Explore(data)
maybe = ja.Maybe(data)
```

### 4. Update Requirements Files

**requirements.txt:**
```diff
- json-scout==0.1.0
+ json-anatomy==0.1.0
```

**pyproject.toml:**
```toml
[project]
dependencies = [
-    "json-scout>=0.1.0",
+    "json-anatomy>=0.1.0",
]
```

**setup.py:**
```python
install_requires=[
-    'json-scout>=0.1.0',
+    'json-anatomy>=0.1.0',
]
```

**Pipfile:**
```toml
[packages]
- json-scout = ">=0.1.0"
+ json-anatomy = ">=0.1.0"
```

---

## What Changed?

### Package Names
- **Distribution name**: `json-scout` → `json-anatomy`
- **Import name**: `jsonscout` → `jsonanatomy`
- **Recommended alias**: `js` → `ja`

### URLs
- **PyPI**: https://pypi.org/project/json-anatomy/
- **Documentation**: https://deamonpog.github.io/json-anatomy/
- **Repository**: https://github.com/deamonpog/json-anatomy

### What Stayed the Same?

✅ **All functionality remains identical**
- Same classes: `Explore`, `Maybe`, `SimpleXML`, `Xplore`
- Same methods: `.keys()`, `.child()`, `.field_counts()`, `.value()`, etc.
- Same API: No breaking changes to functionality
- Same features: File operations, XML integration, safe navigation

**Only the package and import names changed!**

---

## Quick Migration Script

For Linux/macOS:
```bash
#!/bin/bash
# migrate_to_json_anatomy.sh

echo "Uninstalling json-scout..."
pip uninstall json-scout -y

echo "Installing json-anatomy..."
pip install json-anatomy

echo "Updating Python files..."
find . -name "*.py" -type f -exec sed -i 's/import jsonscout/import jsonanatomy/g' {} +
find . -name "*.py" -type f -exec sed -i 's/jsonscout as js/jsonanatomy as ja/g' {} +
find . -name "*.py" -type f -exec sed -i 's/from jsonscout/from jsonanatomy/g' {} +

echo "Migration complete!"
```

For Windows (PowerShell):
```powershell
# migrate_to_json_anatomy.ps1

Write-Host "Uninstalling json-scout..." -ForegroundColor Yellow
pip uninstall json-scout -y

Write-Host "Installing json-anatomy..." -ForegroundColor Yellow
pip install json-anatomy

Write-Host "Updating Python files..." -ForegroundColor Yellow
Get-ChildItem -Path . -Filter *.py -Recurse | ForEach-Object {
    (Get-Content $_.FullName) `
        -replace 'import jsonscout', 'import jsonanatomy' `
        -replace 'jsonscout as js', 'jsonanatomy as ja' `
        -replace 'from jsonscout', 'from jsonanatomy' |
    Set-Content $_.FullName
}

Write-Host "Migration complete!" -ForegroundColor Green
```

---

## Need Help?

If you encounter any issues during migration:

1. **Check your import statements**: Make sure all `jsonscout` references are changed to `jsonanatomy`
2. **Verify installation**: Run `pip show json-anatomy` to confirm it's installed
3. **Test your code**: Run your test suite to ensure everything works
4. **Report issues**: Open an issue at https://github.com/deamonpog/json-anatomy/issues

---

## Timeline

- **Before October 2025**: Package was named `json-scout`
- **October 2025**: Package renamed to `json-anatomy`
- **Future**: `json-scout` package will be deprecated on PyPI

---

## Deprecation Notice for json-scout

The `json-scout` package on PyPI will remain available temporarily but will show a deprecation warning directing users to `json-anatomy`. 

**Please migrate as soon as possible** to ensure you receive future updates and bug fixes.

---

## Questions?

- **Documentation**: https://deamonpog.github.io/json-anatomy/
- **GitHub Issues**: https://github.com/deamonpog/json-anatomy/issues
- **PyPI Page**: https://pypi.org/project/json-anatomy/

Thank you for your understanding and support! 🙏
