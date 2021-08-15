#!/bin/sh
mkdocs gh-deploy
mkdocs build --clean --site-dir output/
netlify deploy output/
