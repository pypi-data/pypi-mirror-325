import os
import streamlit as st


@st.cache_data
def parse_documentation():
    os.getcwd()  # noqa: F821
    try:
        files = os.listdir(f"{os.getcwd()}/assets/")
        documentation = dict()
        for file in files:
            if file.endswith("md"):
                content = open(f"{os.getcwd()}/assets/{file}").read()
                documentation[file.split(".")[0]] = content

    except Exception as e:
        files = os.listdir(f"{os.getcwd()}/assets/")
        documentation = dict()

        for file in files:
            if file.endswith("md"):
                content = open(f"{os.getcwd()}/assets/{file}").read()
                documentation[file.split(".")[0]] = content

    return documentation
