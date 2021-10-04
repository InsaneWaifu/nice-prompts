#!/bin/bash
if [[ $(python3 -m pip list | grep nice-prompts) ]]; then
printf ''
else
    python3 -m pip install .;
fi
cd test
python3 test.py
