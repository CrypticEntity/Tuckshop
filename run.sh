#!/bin/bash
if [ "$(ls data | grep balance)" == "" ]; then
    echo 0.0 >> data/balance
fi
python ./main.py
