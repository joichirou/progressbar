#!/bin/bash

echo "[START]"
echo "example program for progress bar."
echo ""

for i in $(seq 0 10); do
    python3 progressbar/progressBar.py --value=$(($i * 10))
    sleep 0.1s
done

echo ""
echo "[END]"
