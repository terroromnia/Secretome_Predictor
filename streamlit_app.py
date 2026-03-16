import streamlit as st
import pandas as pd
from src.pipeline import run_pipeline

st.title("Microbial Secretome Predictor")

uploaded_file = st.file_uploader("Upload proteome FASTA")

if uploaded_file:

    results = run_pipeline(uploaded_file)

    st.subheader("Prediction Results")
    st.dataframe(results)

    st.download_button(
        "Download results",
        results.to_csv(index=False),
        "secretome_results.csv"
    )
