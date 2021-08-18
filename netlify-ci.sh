#!/bin/sh
pip install -r requirements.txt
python3 setup.py install
yarn install
yarn run build
mkdocs build --clean --site-dir build/
