import os
from pathlib import Path
import pandas as pd
import duckdb
from pygwalker.api.streamlit import StreamlitRenderer
import streamlit as st


from utils.config import read_setting_local


@st.cache_resource
def get_pyg_renderer(file_path) -> StreamlitRenderer:
    settings = read_setting_local()
    try:
        data = duckdb.sql(f"SELECT * FROM '{file_path}.parquet' limit {settings['interactive_limit']}").df()
    except:
        try:
            data = duckdb.sql(f"SELECT * FROM '{file_path}.csv' limit {settings['interactive_limit']}").df()
        except:
            data=pd.DataFrame()
            
    home = Path.home()

    filepath = Path(file_path)
    last_entry = filepath.name
    second_last_entry = filepath.parent.name

    file_dir = os.path.join(home, "Documents", "Cast", "configs", f"{second_last_entry}|{last_entry}.json")

    if len(data)>0:
        return StreamlitRenderer(data, spec=file_dir, spec_io_mode="rw", kernel_computation=True)


def walker_viewer(main_view, export_view):
    if "ran" not in st.session_state:
        st.session_state["ran"] = False

    c1, c2 = st.columns([3, 17], gap="small")

    with c1:
        folder_set = st.selectbox("Folder", ["Source", "Export"], key="dataset_dw_walker")
        if folder_set == "Source":
            if len(main_view.keys()) > 0:
                data_set = st.selectbox(options=main_view.keys(), label="DataSource", key="export_ds_walker")
                submitted = st.button("Explore")
            else:
                data_set=''
                submitted = False
        else:
            if len(export_view.keys()) > 0:
                data_set = st.selectbox(options=export_view.keys(), label="DataSource", key="export_ds_walker")
                submitted = st.button("Explore")
            else:
                data_set=''
                submitted = False

        if "py_walker" not in st.session_state:
            if submitted:
                
                st.session_state["py_walker"] = f"{folder_set}|{data_set}"
            else:
                st.session_state["py_walker"] = ""

        if not submitted:
            if st.session_state["py_walker"] != f"{folder_set}|{data_set}":
                st.session_state["py_show"] = False
            else:
                st.session_state["py_show"] = True
        else:
            st.session_state["py_walker"] = f"{folder_set}|{data_set}"
            st.session_state["py_show"] = True

    with c2:
        home = Path.home()
        base_dir = os.path.join(home, "Documents", "Cast", "data")

        try:
            pyg_app = get_pyg_renderer(file_path=f"{base_dir}/{folder_set.lower()}/{data_set}")
            pyg_app.explorer()
        except:
            st.write("No data to display")