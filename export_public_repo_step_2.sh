#!/usr/bin/env bash
set -euo pipefail

# Step 2: Initialize and push public repository
# Run this from the exported directory created by export_public_repo_step_1.sh

echo "======================================================================="
echo "EXPORT PUBLIC REPOSITORY - STEP 2"
echo "======================================================================="
echo ""

# Verify we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ ERROR: pyproject.toml not found. Run this from the exported directory."
    exit 1
fi

VERSION=$(grep "^version = " pyproject.toml | grep -o '[0-9]\+\.[0-9]\+\.[0-9]\+')
echo "Repository version: $VERSION"
echo ""

# Initialize git
echo "Step 1: Initializing git repository..."
git init
git add .
echo "✅ Files staged"
echo ""

# Create initial commit
echo "Step 2: Creating initial commit..."
git commit -m "Release v$VERSION"
git branch -M main
echo "✅ Commit created"
echo ""

# Add remote (update this URL)
echo "Step 3: Adding remote..."
git remote add origin git@github.com:revenium/revenium-middleware-ollama-python.git
echo "⚠️  Remote added: git@github.com:revenium/revenium-middleware-ollama-python.git"
echo ""

# Push (commented out for safety - uncomment when ready)
echo "Step 4: Ready to push..."
echo ""
echo "⚠️  MANUAL STEP REQUIRED:"
echo ""
echo "Review the repository, then run:"
echo "  git push origin main"
echo ""
echo "Then create and push tag:"
echo "  git tag v$VERSION"
echo "  git push origin v$VERSION"
echo ""
echo "Then publish to PyPI:"
echo "  python -m build"
echo "  twine upload dist/*"
echo ""
echo "======================================================================="
echo "READY FOR MANUAL PUSH"
echo "======================================================================="
