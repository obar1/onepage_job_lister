#!/bin/bash
# simple demo - it use param from cmd line to run the actual section

function setup {
    # set -x
    export MAP_YAML_PATH=map.yaml

    pip install .

    chmod +x main.py
}

streamlit run search_engine_comparison.py
