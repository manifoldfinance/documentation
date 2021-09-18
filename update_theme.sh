#!/bin/bash -x
echo "Deleting theme..."
sleep 1
rm -rf material/ package.json requirements.txt setup.py src/ tools/ tsconfig.json, typings/
echo "unpacking update..."
unzip insiders.zip
