import streamlit as st
from components.bi_tool import walker_viewer
from components.extract import query_extract
from utils.config import read_setting
from utils.data_profiler import get_numeric_cols, read_files
from utils.documentation import parse_documentation
from components.graph import make_graph


st.set_page_config(
    page_title="Exakt Cast",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
stAppDeployButton {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


try:
    st.image(
        image="assets/cast.png",
        caption=None,
        width=200,
        use_column_width=None,
        clamp=False,
        channels="RGB",
        output_format="auto",
    )
except:
    st.image(
        image="cast/assets/cast.png",
        caption=None,
        width=200,
        use_column_width=None,
        clamp=False,
        channels="RGB",
        output_format="auto",
    )

with st.spinner("Refreshing"):
    main_view = read_files(folder="source")
    export_view = read_files(folder="export")
    documentation = parse_documentation()
    settings = read_setting()
    
    if settings not in st.session_state:
        st.session_state["settings"] = settings

main_col1, main_col2 = st.columns([8, 2])


with main_col2:
    clear_cache_btn = st.button("Refresh", icon="🔄", type="tertiary")
    if clear_cache_btn:
        st.cache_data.clear()
        st.cache_resource.clear()

q_t1, q_t2, q_t3, q_t4 = st.tabs(["Data", "One-way", "Data Viewer", "Help"])

with q_t1:
    query_extract()

with q_t2:
    q_t1c1, q_t1c2 = st.columns([3, 17], gap="small")

    with q_t1c1:
        folder_set = st.selectbox("Folder", ["Source", "Export"])

        if folder_set == "Source":
            if len(main_view.keys()) > 0:
                data_set = st.selectbox(options=main_view.keys(), label="Datasource")
                data_dim = st.selectbox(options=list(main_view[data_set].columns), label="Dimension")
                data_target = st.selectbox(options=get_numeric_cols(main_view, data_set), label="Target")
                submitted = st.button("render")

            else:
                submitted = False
        else:
            if len(export_view.keys()) > 0:
                data_set = st.selectbox(options=export_view.keys(), label="Datasource")
                data_dim = st.selectbox(options=list(export_view[data_set].columns), label="Dimension")
                data_target = st.selectbox(options=get_numeric_cols(export_view, data_set), label="Target")
                submitted = st.button("render")
            else:
                submitted = False

    if submitted:
        with q_t1c2:
            st.plotly_chart(make_graph(folder_set, data_set, data_dim, data_target))


with q_t3:
    walker_viewer(main_view, export_view)

with q_t4:
    documentation_list = st.selectbox(options=documentation.keys(), label="Topic")
    st.divider()
    st.markdown(documentation[documentation_list])
