import streamlit as st
from streamlit_monaco import st_monaco
import duckdb
from pathlib import Path
import os
from utils.files import delete_file, list_files, load_file, save_file, remove_incomplete_rows


@st.dialog("Save query")
def save_modal(filename, text):
    st.write("Choose a filename:")
    new_name = st.text_input(value=filename, label="Filename:")
    if st.button("Save"):
        save_file(file_name=f"{new_name.split('.')[0]}.sql", text=text)
        st.rerun()


@st.dialog("Delete")
def delete_modal(filename):
    st.write(f"Are you sure you want to delete {filename}")
    if st.button("Yes"):
        delete_file(filename)
        st.rerun()
        
@st.dialog("Upload to Exakt")
def upload_modal():
    workspaces=['Belgium - MTPL']
    st.write('''I confirm that the data l'm uploading does not contain any Personal Identifiable Information (PI).
PlI includes but is not limited to names, addresses, social security numbers, phone numbers, email addresses, and any other information that could be used to identify an individual.
    ''')
    upload_check=st.checkbox("I understand and confirm my data does not contain PII")
    
    if upload_check:
        with st.form("dataset_form"):
            selected_workspace = st.selectbox("Select Workspace", options=workspaces)
            datasource_type = st.selectbox("Select Datasource Type", options=["Geo", "Modelling"])
            dataset_name = st.text_input("Dataset Name", placeholder="Enter a name for your dataset")
            submit_button = st.form_submit_button("Upload Dataset")
            
        if submit_button:
            st.write("Submitted")
            st.rerun()

@st.dialog("Export")
def export_modal(selected_file, alternative):
    st.write("Do you want to exclude empty entries?")

    include_empty = st.radio("Include empty entries", ["Yes", "No"])

    if st.button("Run"):
        home = Path.home()
        lookup_dir = os.path.join(home, "Documents", "Cast", "data", "export", selected_file.split(".")[0])
        with st.spinner(text="In progress..."):
            sql_rendered = f"SET ieee_floating_point_ops = false; \n {alternative}"
            data = duckdb.sql(sql_rendered).pl()

            if include_empty == "Yes":
                data.write_parquet(f"{lookup_dir}.parquet")
            else:
                remove_incomplete_rows(data).write_parquet(f"{lookup_dir}.parquet")
            st.rerun()


def query_extract():

    if "ran" not in st.session_state:
        st.session_state["ran"] = False
    c1, c2 = st.columns([1, 9], gap="small")
    upload_button = False
    with c1:
        if len(list_files()) > 0:
            selected_file = st.selectbox(options=list_files(), label="Query")
            if "selected_file" not in st.session_state:
                st.session_state["selected_file"] = selected_file
                text = load_file(selected_file)
                st.session_state["query"] = text

            if st.session_state["selected_file"] != selected_file:
                st.session_state["selected_file"] = selected_file
                text = load_file(selected_file)
                st.session_state["query"] = text

            else:
                text = st.session_state["query"]

            run_button = st.button("Run", type="primary", use_container_width=True)
            export_button = st.button("Export", type="secondary", use_container_width=True)
            save_button = st.button("Save", type="secondary", use_container_width=True)
            delete_button = st.button("Delete", type="secondary", use_container_width=True)
            
            if 'exakt' in st.session_state["settings"]:
                upload_button = st.button("Upload", icon="🚀", use_container_width=True)
            else:
                upload_button = False
        else:
            selected_file = "new_query.sql"
            text = ""
            run_button = st.button("Run", type="primary", use_container_width=True, disabled=True)
            export_button = st.button("Export", type="secondary", use_container_width=True, disabled=True)
            save_button = st.button("Save", type="secondary", use_container_width=True)
            delete_button = st.button("Delete", type="secondary", use_container_width=True, disabled=True)

    with c2:
        alternative = st_monaco(value=text, height="500px", language="sql", theme="vs-dark", lineNumbers=True)

    if run_button:
        try:
            t1, t2 = st.tabs(["Results", "Freestyle"])
            sql_rendered = f"select * from ({alternative}) limit 1000"
            st.session_state["ran"] = True

            with t1:
                if run_button:
                    st.session_state["ran"]
                    df = duckdb.sql(sql_rendered).df()
                    st.session_state["df"] = df
                else:
                    df = st.session_state["df"]

                st.dataframe(df.head(1000))
        except Exception as e:
            st.write(e)

    elif save_button:
        try:
            save_modal(selected_file, alternative)
        except Exception as e:
            st.write(e)

    elif delete_button:
        delete_modal(filename=selected_file)

    elif export_button:
        export_modal(selected_file, alternative)
        
    elif upload_button:
        upload_modal(selected_file)
