"""
Streamlit app: Simulate an "algo pushes then dumps" option-market scenario

Save this file as `streamlit_app.py` (or the name you prefer) and push to GitHub.
Run locally with:
    pip install streamlit pandas numpy
    streamlit run streamlit_app.py

This single-file app provides interactive controls in the sidebar to configure
fair price, initial quotes, human order schedule, algo behavior and then
runs a simplified discrete-time market simulation. Outputs (no graphs):
 - Price history table (downloadable CSV)
 - Trade log (downloadable CSV)
 - Positions summary

This is an educational toy model — not a market microstructure-accurate
simulation. Use it for demonstration and learning.
"""

import streamlit as st
import pandas as pd
import numpy as np
import io

st.set_page_config(page_title="Algo Push-and-Dump Simulator (No Graphs)", layout="wide")

st.title("Algo Push-and-Dump — Option Market Simulator (Tables Only)")
st.markdown(
    """
    This toy simulator models a simplified scenario where an algorithm posts
    wide passive quotes, buys into the market to push the price when a human
    buyer shows interest, then dumps inventory to that buyer once price
    reaches a threshold (e.g., 20% above fair value). The algo then returns
    to passive quotes. Use controls on the left to change parameters.

    This version intent
