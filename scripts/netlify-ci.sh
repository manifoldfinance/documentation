#!/bin/sh
mkdocs build --clean --site-dir output/
netlify deploy --dir=output/ --prod
