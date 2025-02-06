import json
from pathlib import Path
import streamlit as st
import os


@st.cache_data
def read_setting():
    home = Path.home()
    file_dir = os.path.join(home, "Documents", "Cast", "settings.json")
    with open(file_dir, "r") as f:
        settings = json.load(f)
    return settings


def read_setting_local():
    home = Path.home()
    file_dir = os.path.join(home, "Documents", "Cast", "settings.json")
    with open(file_dir, "r") as f:
        settings = json.load(f)
    return settings
