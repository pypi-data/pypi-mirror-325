import plotly.graph_objects as go
import duckdb as db
import os
from pathlib import Path


def make_graph(folder_set, data_set, data_dim, data_target):
    home = Path.home()
    lookup_dir = os.path.join(home, "Documents", "Cast", "data", folder_set.lower(), data_set)

    try:
        query = f"""
        select  coalesce({data_dim},'-1') as {data_dim},avg({data_target}) as {data_target},count(*) as volumes
        from  '{lookup_dir}.csv' 
        group by 1
        order by 1
        
        """
        data_extract = db.sql(query=query).df()

    except:
        query = f"""
        select  coalesce({data_dim},'-1') as {data_dim},avg({data_target}) as {data_target},count(*) as volumes
        from  '{lookup_dir}.parquet' 
        group by 1
        order by 1
        """

        data_extract = db.sql(query=query).df()

    # Create a bar chart for volumes
    bar_chart = go.Bar(x=data_extract[data_dim], y=data_extract["volumes"], name="Volume", marker_color="rgba(55, 83, 109, 0.7)")

    # Create a line chart for average amounts
    line_chart = go.Scatter(
        x=data_extract[data_dim],
        y=data_extract[f"{data_target}"],
        name=f"Average {data_target}",
        mode="lines+markers",
        marker=dict(color="#3dbf79", size=8),
        line=dict(color="#3dbf79", width=3),
        yaxis="y2",
    )

    # Combine both charts in a single figure
    fig = go.Figure(data=[bar_chart, line_chart])

    # Customize the layout
    fig.update_layout(
        title=f"Volumes and Average {data_target}",
        xaxis_title=f"{data_dim}",
        yaxis_title="Values",
        yaxis=dict(title="Volume", side="left"),
        yaxis2=dict(title=f"Average  {data_target}", overlaying="y", side="right"),
        barmode="group",
        hovermode="x unified",
        legend=dict(x=0.1, y=1.1),
    )

    return fig
