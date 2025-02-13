# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

# Build
**Firstly increase the version in `pyproject.toml`.**
## Windows
Cleanup
```pwsh
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue .\dist\*
```

Build & upload
```pwsh
py -m pip install --upgrade pip
py -m pip install --upgrade build
py -m build
py -m pip install --upgrade twine
```