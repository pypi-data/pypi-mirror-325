#!/bin/bash

MYDIR="${0%/*}"

pushd ${MYDIR}

echo [+] Creating venv...
virtualenv venv
cp upload.py venv/
cd venv
source bin/activate

echo
echo [+] Installing dependencies...
python3 -m pip install brightspace-api

echo
echo [+] Running upload script
python3 upload.py

echo
echo [+] Removing venv
deactivate
cd ..
rm -rf venv/

popd
