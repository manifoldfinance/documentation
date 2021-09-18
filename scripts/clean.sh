#!/bin/bash

"Cleaning build artifacts..."
rm -rf /node_modules
rm -rf __pycache__
rm -rf venv
rm -rf .venv

# Build files
rm -rf build
rm -rf MANIFEST
rm -rf site

# Distribution files
rm -rf dist
rm -rf mkdocs_material.egg-info
