#!/bin/bash
# simple demo - it use param from cmd line to run the actual section

function setup {
    # set -x

    pip install -r ./requirements.txt
}
setup
python -m streamlit run search_engine_comparison.py
