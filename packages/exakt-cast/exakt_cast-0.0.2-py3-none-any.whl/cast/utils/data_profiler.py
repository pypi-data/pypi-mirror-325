import os
from pathlib import Path
import pandas as pd
import duckdb
import json
import streamlit as st


@st.cache_resource
def read_files(folder):
    home = Path.home()
    lookup_dir = os.path.join(home, "Documents", "Cast", "data", folder)
    files = os.listdir(lookup_dir)
    main_view = dict()

    for file in files:
        if file.endswith(".DS_Store") is False:
            if file.endswith("json") is False:
                lookup_file = os.path.join(lookup_dir, file)
                sample = duckdb.sql(f"SELECT * FROM '{lookup_file}' limit 5000").df()
                main_view[file.split(".")[0]] = sample
                get_conversion_mapping(main_view, file.split(".")[0])

    return main_view


@st.cache_resource
def process_types(main_view, selected_object):
    home = Path.home()
    lookup_dir = os.path.join(home, "Documents", "Cast", "settings.json")
    with open(lookup_dir, "r") as f:
        settings = json.load(f)

    head = main_view[selected_object].head(1).T
    head.columns = ["Sample"]
    dtype = pd.DataFrame(main_view[selected_object].dtypes)
    dtype.columns = ["Type"]
    dtype["Type"] = dtype["Type"].apply(lambda x: "string" if x == "object" else str(x))

    df = main_view[selected_object]
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].replace(settings["missing_values"], "NULL")

    df = df.fillna(0)
    df_numeric = df.apply(pd.to_numeric, errors="coerce")

    percent_nulls = pd.DataFrame(100 - df_numeric.isna().mean() * 100)
    percent_nulls.columns = ["Perc_numeric"]
    temp_1 = dtype.join(head)
    result = temp_1.join(percent_nulls)

    result["Sample"] = result["Sample"].astype("str")

    return result


@st.cache_resource
def get_conversion_mapping(main_view, selected_object):
    statements = []
    type_df = process_types(main_view, selected_object)

    numeric_casts = list(type_df[(type_df.Perc_numeric > 0.2) & (type_df.Type == "string")].index)
    home = Path.home()
    lookup_dir = os.path.join(home, "Documents", "Cast", "settings.json")
    with open(lookup_dir, "r") as f:
        settings = json.load(f)

    missing = settings["missing_values"]
    numeric_separator = settings["numeric_separator"]
    string_casts = list(type_df[(type_df.Perc_numeric < 0.2) & (type_df.Type == "string")].index)

    all_columns = list(type_df.index)

    for col in all_columns:
        if col not in string_casts:
            if col not in numeric_casts:
                statement = col
                statements.append(statement)

    for entry in numeric_casts:
        statement = f"""coalesce(
TRY_CAST(IF({entry}::VARCHAR in ({",".join(f"'{w}'" for w in missing)}),'',if({entry}::VARCHAR ilike '%{numeric_separator}%',replace({entry}::VARCHAR,'{numeric_separator}','.'),{entry}::VARCHAR)) as Float) 
,TRY_CAST({entry} as Float)) as  {entry}"""
        statements.append(statement)

    for entry in string_casts:
        statement = f"IF({entry} in ({','.join(f"'{w}'" for w in missing)}),NULL,{entry}) as {entry}"
        statements.append(statement)

    home = Path.home()

    lookup_dir = os.path.join(home, "Documents", "Cast", "data", "source")

    files = os.listdir(lookup_dir)
    for file in files:
        if file.startswith(selected_object):
            data_source = file
            break
        else:
            data_source = f"{selected_object}.parquet"

    clean_statements = "\n \t,".join(statements)
    file = os.path.join(home, "Documents", "Cast", "data", "source", data_source)

    final_query = f"""
select
    {clean_statements}
from '{file}'
    """

    lookup_dir = os.path.join(home, "Documents", "Cast", "queries")
    if f"{selected_object}.sql" not in os.listdir(lookup_dir):
        file_dir = os.path.join(home, "Documents", "Cast", "queries", f"{selected_object}.sql")
        with open(file_dir, "w") as f:
            f.write(final_query)


@st.cache_resource
def get_numeric_cols(main_view, selected_object):
    df = process_types(main_view, selected_object)
    df["Type"] = df["Type"].astype("str")
    return list(df[df["Type"].isin(["float64", "float32,", "int64", "int32"])].index)
