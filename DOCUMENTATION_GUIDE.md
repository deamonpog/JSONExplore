# Documentation and GitHub Workflows Guide

Complete guide for managing documentation and GitHub Actions workflows for JSON Anatomy.

## Package Name Information

**Distribution name** (for pip): `json-anatomy`  
**Import name** (in Python): `jsonanatomy`

```bash
# Install with hyphen
pip install json-anatomy

# Import without hyphen
import jsonanatomy as js
```

**Note:** The package was rebranded from "jsonexplore" to "json-anatomy" before initial PyPI publication.

## Table of Contents

1. [Documentation Overview](#documentation-overview)
2. [Building Documentation Locally](#building-documentation-locally)
3. [Deploying Documentation](#deploying-documentation)
4. [GitHub Actions Workflows](#github-actions-workflows)
5. [Troubleshooting](#troubleshooting)

---

## Documentation Overview

JSON Anatomy uses **MkDocs** with the **Material** theme for documentation.

### Package Naming Convention

JSON Anatomy follows Python packaging best practices:

| Context | Name | Example |
|---------|------|---------|
| **PyPI package name** | `json-anatomy` | `pip install json-anatomy` |
| **Python import** | `jsonanatomy` | `import jsonanatomy as js` |
| **GitHub repo** | `json-anatomy` | `github.com/deamonpog/json-anatomy` |
| **Documentation** | `json-anatomy` | `deamonpog.github.io/json-anatomy/` |

**Why the difference?**
- PyPI allows hyphens (`json-anatomy`) for readability
- Python imports cannot have hyphens (must be `jsonanatomy`)
- This is standard practice (e.g., `scikit-learn` → `import sklearn`)

### Documentation Structure

```
docs/
├── index.md          # Home page with features, examples, use cases
└── api.md            # Auto-generated API reference from docstrings

mkdocs.yml            # MkDocs configuration
site/                 # Generated documentation (don't commit)
```

### Key Features

- **Auto-generated API docs** from NumPy-style docstrings using mkdocstrings
- **Material theme** with dark/light mode, search, and navigation
- **Code copy buttons** for easy example usage
- **Hosted on GitHub Pages** at https://deamonpog.github.io/json-anatomy/

---

## Building Documentation Locally

### Prerequisites

```bash
conda activate jsonexplore
pip install mkdocs mkdocs-material mkdocstrings[python]
```

### Build and Preview

```bash
# Serve locally with live reload (recommended for development)
mkdocs serve
```

This will:
- Build the documentation
- Start a local server at http://127.0.0.1:8000/
- Auto-reload when you edit files

**Tip:** Keep `mkdocs serve` running while editing docs to see changes instantly!

### Build Static Site

```bash
# Build static HTML files in site/ directory
mkdocs build
```

Use this to:
- Check for build errors
- Preview the final output before deploying
- Test search functionality

### Clean Build

```bash
# Remove previous build
Remove-Item -Path "site" -Recurse -Force -ErrorAction SilentlyContinue

# Rebuild from scratch
mkdocs build
```

---

## Deploying Documentation

### Method 1: Manual Deployment (Recommended)

```bash
# From project root
conda activate jsonexplore
mkdocs gh-deploy
```

This will:
1. Build the documentation
2. Push to `gh-pages` branch
3. Deploy to GitHub Pages automatically

**After deployment:**
- Visit: https://deamonpog.github.io/json-anatomy/
- May take 1-2 minutes to reflect changes

### Method 2: Automatic Deployment via GitHub Actions

Documentation auto-deploys on push to `main` or `master` branch.

**See:** `.github/workflows/docs.yml`

#### Trigger Manual Deployment

1. Go to: https://github.com/deamonpog/json-anatomy/actions
2. Select "Deploy Documentation" workflow
3. Click "Run workflow"
4. Select branch and run

---

## GitHub Actions Workflows

### 1. Documentation Deployment (docs.yml)

**File:** `.github/workflows/docs.yml`

**Triggers:**
- Push to `main` or `master` branch
- Pull request to `main` or `master`
- Manual workflow dispatch

**What it does:**
```yaml
✅ Checks out code
✅ Sets up Python 3.9
✅ Installs mkdocs + dependencies
✅ Builds documentation
✅ Deploys to GitHub Pages (only on main/master)
```

**Status:** ✅ Already configured for `json-anatomy`

---

### 2. PyPI Publishing (publish.yml)

**File:** `.github/workflows/publish.yml`

**Triggers:**
- GitHub release published
- Manual workflow dispatch

**What it does:**
```yaml
✅ Tests imports on Python 3.7-3.11
✅ Builds source distribution and wheel
✅ Checks distribution validity
✅ Publishes to PyPI (on release only)
```

**Status:** ✅ Already configured with `jsonanatomy` imports

---

## Configuration Details

### mkdocs.yml Configuration

```yaml
# Site metadata
site_name: JSON Anatomy Documentation
site_description: Scout JSON structure and navigate data safely
site_url: https://deamonpog.github.io/json-anatomy/
repo_url: https://github.com/deamonpog/json-anatomy

# Auto-generated API docs
plugins:
  - mkdocstrings:
      handlers:
        python:
          paths: ["src"]              # Look for source code here
          options:
            docstring_style: numpy    # Parse NumPy-style docstrings
```

**Key Points:**
- ✅ All URLs updated to `json-anatomy`
- ✅ Docstring style set to `numpy`
- ✅ Source path points to `src/`

---

## Updating Documentation

### Editing Content

#### Home Page (docs/index.md)

Contains:
- Introduction
- Key features
- Installation instructions
- Quick start examples
- Use cases
- Architecture overview

**To update:**
1. Edit `docs/index.md`
2. Test with `mkdocs serve`
3. Commit and push (auto-deploys) or run `mkdocs gh-deploy`

#### API Reference (docs/api.md)

Auto-generated from docstrings. To update:
1. Edit docstrings in source code (NumPy style)
2. Rebuild docs to see changes

**Example:**
```python
def keys(self):
    """
    Get the keys or indices of direct children.

    Returns
    -------
    list
        For dictionaries: list of string keys.
        For lists: list of integer indices.

    Examples
    --------
    >>> explorer = Explore({'a': 1, 'b': 2})
    >>> print(explorer.keys())
    ['a', 'b']
    """
    return self.child_keys
```

### Adding New Pages

1. Create new `.md` file in `docs/` folder
2. Add to navigation in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - API Reference: api.md
  - Your New Page: newpage.md
```

3. Build and deploy

---

## Troubleshooting

### Documentation Build Fails

**Problem:** `mkdocstrings` can't find module

```
Error: No module named 'jsonanatomy'
```

**Solution:**
```bash
# Install package in development mode
pip install -e .

# Or add src to PYTHONPATH
$env:PYTHONPATH = "src;$env:PYTHONPATH"
mkdocs build
```

---

**Problem:** Import errors in docstring examples

**Solution:**
- Docstring examples are tested during build
- Make sure examples use correct import: `import jsonanatomy as js`
- Fix examples in source code docstrings

---

### GitHub Pages Not Updating

**Problem:** Changes don't appear after `mkdocs gh-deploy`

**Solution:**
1. Check GitHub Pages settings:
   - Go to: Settings → Pages
   - Source should be: `gh-pages` branch
   - Should show: `Your site is published at https://deamonpog.github.io/json-anatomy/`

2. Wait 1-2 minutes for deployment

3. Hard refresh browser (Ctrl+Shift+R)

4. Check GitHub Actions for errors

---

**Problem:** 404 on GitHub Pages

**Solution:**
- Verify `site_url` in `mkdocs.yml` matches GitHub Pages URL
- Check that `gh-pages` branch exists
- Ensure repository is public or GitHub Pages is enabled for private repos

---

### GitHub Actions Failing

**Problem:** Documentation workflow fails

**Solution:**
1. Check workflow run: https://github.com/deamonpog/json-anatomy/actions
2. Look for error messages
3. Common issues:
   - Missing dependencies (update workflow YAML)
   - Import errors (check package name)
   - Permission issues (verify repository settings)

---

**Problem:** PyPI publish workflow fails

**Solution:**
1. Verify `PYPI_API_TOKEN` secret exists:
   - Go to: Settings → Secrets and variables → Actions
   - Should have secret named `PYPI_API_TOKEN`

2. Check token is valid:
   - Generate new token at https://pypi.org/manage/account/token/
   - Update secret in GitHub

3. Ensure workflow triggers on releases:
   - Create release via GitHub UI
   - Tag must match version in `_version.py`

---

## Quick Reference

### Common Commands

```bash
# Development workflow
mkdocs serve              # Preview locally with live reload
mkdocs build              # Build static site
mkdocs gh-deploy          # Deploy to GitHub Pages

# Package workflow  
python -m build           # Build package
python -m twine upload dist/*  # Upload to PyPI

# Git workflow
git add .
git commit -m "Update docs"
git push origin docsite
```

### File Locations

```
Documentation:
├── docs/index.md              # Home page
├── docs/api.md                # API reference
├── mkdocs.yml                 # MkDocs config
└── site/                      # Generated site (don't commit)

Workflows:
├── .github/workflows/docs.yml     # Documentation deployment
└── .github/workflows/publish.yml  # PyPI publishing

Source Code:
└── src/jsonanatomy/             # All docstrings here
```

### Important URLs

- **Documentation:** https://deamonpog.github.io/json-anatomy/
- **Repository:** https://github.com/deamonpog/json-anatomy
- **PyPI:** https://pypi.org/project/json-anatomy/ (after publishing)
- **GitHub Actions:** https://github.com/deamonpog/json-anatomy/actions

---

## Workflow for Updating Everything

When you make changes to the package:

```bash
# 1. Update source code and docstrings
# Edit files in src/jsonanatomy/

# 2. Update documentation content (if needed)
# Edit files in docs/

# 3. Preview changes
mkdocs serve

# 4. Build and test package
python -m build
pip install dist/json_scout-0.1.0-py3-none-any.whl
python scripts/test_installation.py

# 5. Commit changes
git add .
git commit -m "Update: describe changes"
git push

# 6. Deploy documentation (if not auto-deploying)
mkdocs gh-deploy

# 7. Create release (when ready for PyPI)
# Go to GitHub → Releases → Create new release
# Tag: v0.1.0, Title: JSON Anatomy v0.1.0
# This triggers automatic PyPI publishing
```

---

## Best Practices

### Documentation

1. **Keep examples up-to-date** - Test all code examples work
2. **Use NumPy style docstrings** - Consistent with mkdocstrings config
3. **Add type hints** - Improves auto-generated API docs
4. **Test locally first** - Always run `mkdocs serve` before deploying
5. **Version your docs** - Tag releases in git

### Workflows

1. **Test before publishing** - Use Test PyPI first
2. **Semantic versioning** - Follow semver for releases
3. **Monitor actions** - Check workflow runs for errors
4. **Update dependencies** - Keep GitHub Actions up-to-date
5. **Secure secrets** - Never commit API tokens

---

**Happy Documenting! 📚**

