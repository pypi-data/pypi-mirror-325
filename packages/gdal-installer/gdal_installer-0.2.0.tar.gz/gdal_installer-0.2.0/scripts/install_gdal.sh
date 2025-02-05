#!/bin/bash

# Get script directory and change to it
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Execute Python installer
python3 install-gdal
