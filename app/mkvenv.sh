#!/bin/sh
rm -rf .venv
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install wheel
.venv/bin/pip install -e ../base3
