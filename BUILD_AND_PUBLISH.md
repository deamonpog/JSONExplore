# Build and Publish Guide - JSON Anatomy

Complete guide for building and publishing the JSON Anatomy package to PyPI.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Pre-Build Checklist](#pre-build-checklist)
3. [Building the Package](#building-the-package)
4. [Local Testing](#local-testing)
5. [Publishing to Test PyPI](#publishing-to-test-pypi)
6. [Publishing to Production PyPI](#publishing-to-production-pypi)
7. [Post-Publication](#post-publication)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Tools

```bash
# Ensure you have these installed in your conda environment
conda activate jsonexplore
pip install --upgrade build twine
```

### PyPI Accounts

1. **Test PyPI** (for testing): https://test.pypi.org/account/register/
2. **Production PyPI**: https://pypi.org/account/register/

### API Tokens

Generate API tokens (recommended over passwords):

1. **Test PyPI**: https://test.pypi.org/manage/account/token/
2. **Production PyPI**: https://pypi.org/manage/account/token/

Store tokens securely - you'll need them for uploading.

---

## Pre-Build Checklist

Before building, verify everything is ready:

### 1. Version Number

Check `src/jsonanatomy/_version.py`:

```python
__version__ = "0.1.0"  # Update as needed
```

### 2. Package Metadata

Verify `pyproject.toml`:

- [ ] Package name: `name = "json-anatomy"`
- [ ] Version reads from `jsonanatomy._version.__version__`
- [ ] Author information is correct
- [ ] Description is accurate
- [ ] All URLs point to correct repository
- [ ] Dependencies are listed
- [ ] Classifiers are appropriate

### 3. Documentation

- [ ] README.md is up to date
- [ ] CHANGELOG exists (create if needed)
- [ ] API documentation is current
- [ ] Examples work correctly

### 4. Code Quality

```bash
# Run tests (if you have them)
pytest tests/

# Check for errors
python -c "import sys; sys.path.insert(0, 'src'); import jsonanatomy; print('✅ Import works')"
```

### 5. Clean Previous Builds

```bash
# Remove old build artifacts
Remove-Item -Path "dist" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "build" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "src\*.egg-info" -Recurse -Force -ErrorAction SilentlyContinue
```

---

## Building the Package

### Step 1: Activate Environment

```bash
conda activate jsonexplore
```

### Step 2: Build Distribution Files

```bash
# Build both source distribution (.tar.gz) and wheel (.whl)
python -m build
```

**Expected Output:**
```
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment...
* Getting build dependencies for sdist...
* Building sdist...
* Building wheel from sdist...
Successfully built json_scout-0.1.0.tar.gz and json_scout-0.1.0-py3-none-any.whl
```

### Step 3: Verify Build Artifacts

```bash
# Check dist/ folder
dir dist\
```

You should see:
- `json_scout-0.1.0.tar.gz` (source distribution)
- `json_scout-0.1.0-py3-none-any.whl` (wheel distribution)

---

## Local Testing

**ALWAYS test locally before publishing!**

### Method 1: Test in Fresh Environment

```bash
# Create test environment
conda create -n jsonanatomy-test python=3.9 -y
conda activate jsonanatomy-test

# Install from local wheel
pip install dist\json_scout-0.1.0-py3-none-any.whl

# Test imports
python -c "import jsonanatomy as js; print(js.__version__)"

# Run comprehensive tests
python scripts\test_installation.py

# Cleanup
conda deactivate
conda env remove -n jsonanatomy-test -y
```

### Method 2: Quick Test in Current Environment

```bash
# Install in editable mode for quick testing
pip install -e .

# Test functionality
python scripts\test_installation.py
```

---

## Publishing to Test PyPI

**Always test on Test PyPI first!**

### Step 1: Upload to Test PyPI

```bash
# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*
```

**You'll be prompted for:**
- Username: `__token__`
- Password: Your Test PyPI API token (starts with `pypi-...`)

### Step 2: Test Installation from Test PyPI

```bash
# Create fresh test environment
conda create -n test-from-pypi python=3.9 -y
conda activate test-from-pypi

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple json-anatomy

# Test it works
python -c "import jsonanatomy as js; print(f'Version: {js.__version__}')"

# Cleanup
conda deactivate
conda env remove -n test-from-pypi -y
```

### Step 3: Verify on Test PyPI Website

Visit: https://test.pypi.org/project/json-anatomy/

Check:
- [ ] Package description renders correctly
- [ ] Version number is correct
- [ ] All metadata looks good
- [ ] README is properly formatted

---

## Publishing to Production PyPI

**⚠️ WARNING: You cannot delete or re-upload the same version to PyPI!**

Make sure everything is perfect before this step.

### Final Pre-Flight Checks

- [ ] Tested on Test PyPI successfully
- [ ] All documentation is correct
- [ ] Version number is final
- [ ] CHANGELOG is updated
- [ ] Git commits are pushed
- [ ] No sensitive information in code

### Upload to Production PyPI

```bash
# Upload to real PyPI
python -m twine upload dist/*
```

**You'll be prompted for:**
- Username: `__token__`
- Password: Your Production PyPI API token

### Verify Upload

Visit: https://pypi.org/project/json-anatomy/

Test installation:

```bash
# Anyone can now install with:
pip install json-anatomy
```

---

## Post-Publication

### 1. Tag the Release in Git

```bash
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

### 2. Create GitHub Release

Go to: https://github.com/deamonpog/json-anatomy/releases/new

- Tag: `v0.1.0`
- Title: `JSON Anatomy v0.1.0`
- Description: Copy from CHANGELOG

### 3. Update Documentation

```bash
# Deploy updated docs to GitHub Pages
mkdocs gh-deploy
```

### 4. Announce

- Tweet/post about the release
- Update project README badges
- Share on relevant communities

### 5. Monitor

- Check PyPI stats: https://pypistats.org/packages/json-anatomy
- Monitor GitHub issues
- Watch for bug reports

---

## Troubleshooting

### Build Fails

**Problem:** `ModuleNotFoundError` during build

**Solution:** Make sure all dependencies are in `pyproject.toml` under `dependencies`

---

**Problem:** `License classifiers are deprecated` warning

**Solution:** This is just a warning, the build still succeeds. You can ignore it or update to newer setuptools format later.

---

### Upload Fails

**Problem:** `403 Forbidden` error

**Solution:** 
- Check your API token is correct
- Make sure you're using `__token__` as username
- Verify token has upload permissions

---

**Problem:** `File already exists` error

**Solution:** 
- You cannot re-upload the same version
- Increment version number in `_version.py`
- Rebuild and upload again

---

**Problem:** `Invalid distribution filename`

**Solution:**
- Check that package name in `pyproject.toml` matches
- Rebuild with `python -m build`
- Don't rename files in `dist/` manually

---

### Installation Fails

**Problem:** `Could not find a version that satisfies the requirement`

**Solution:**
- Wait a few minutes for PyPI to index the package
- Check package name is correct (`json-anatomy` not `jsonanatomy`)
- Verify you're using the right Python version

---

**Problem:** Import fails after installation

**Solution:**
- Remember: Install with `pip install json-anatomy`
- But import with `import jsonanatomy` (no hyphen)
- Check you're in the right environment

---

## Quick Reference Commands

```bash
# Complete build and publish workflow
conda activate jsonexplore

# Clean previous builds
Remove-Item -Path "dist", "build" -Recurse -Force -ErrorAction SilentlyContinue

# Build
python -m build

# Test locally
pip install dist\json_scout-0.1.0-py3-none-any.whl
python scripts\test_installation.py

# Upload to Test PyPI (recommended first)
python -m twine upload --repository testpypi dist/*

# Upload to Production PyPI (when ready)
python -m twine upload dist/*

# Tag release
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0

# Deploy docs
mkdocs gh-deploy
```

---

## Version Numbering Guide

Follow [Semantic Versioning](https://semver.org/):

- **0.1.0** - Initial release
- **0.1.1** - Bug fixes
- **0.2.0** - New features (backward compatible)
- **1.0.0** - First stable release
- **2.0.0** - Breaking changes

Update version in: `src/jsonanatomy/_version.py`

---

## Security Best Practices

1. **Never commit API tokens** to git
2. **Use tokens, not passwords** for PyPI
3. **Revoke tokens** if compromised
4. **Use separate tokens** for Test PyPI and Production
5. **Set token scope** to upload only (not delete/modify)

---

## Additional Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Help](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)

---

**Happy Publishing! 🚀**

