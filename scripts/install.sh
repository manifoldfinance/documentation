#!/bin/sh

pip install -r -requirements.txt

npm i

npm run-script build

mkdocs build --config-file mkdocs.yml

