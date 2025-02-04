import pandas as pd
from plotly import express as px
from plotly import graph_objects as go
from plotly.subplots import make_subplots

import vdl_tools.py2mappr.vdl_palette as pal

from vdl_tools.shared_tools.plotly_charts.plotly_template import pio


pio.templates.default = "vibrant_white"
template = pio.templates[pio.templates.default]


def create_aggregated_df(
    df: pd.DataFrame,
    xaxis_column=None,
    color_by_column=None,
    facet_by_column=None,
    agg_func="count",
    agg_column="uid",
    normalize_by_total_column=None,
):
    groupby_columns = []
    if xaxis_column:
        groupby_columns.append(xaxis_column)
    if color_by_column:
        groupby_columns.append(color_by_column)
    if facet_by_column:
        groupby_columns.append(facet_by_column)
    
    if groupby_columns:
        agg_df = (
            df
            .groupby(groupby_columns)
            .agg({agg_column: agg_func})
            .reset_index()
        )
    else:
        agg_df = df.agg({agg_column: agg_func}).reset_index()

    agg_df["aggregated_value"] = agg_df[agg_column]
    if normalize_by_total_column:
        if len(groupby_columns) < 2:
            raise ValueError("normalize_by_total_column requires at least 2 groupby columns")

        normalized_column_totals = (
            agg_df
            .groupby(normalize_by_total_column)
            .sum()
            [agg_column]
            .to_dict()
        )
        
        agg_df['totals'] = agg_df[normalize_by_total_column].map(normalized_column_totals)
        agg_df["normalized_value"] = agg_df[agg_column] / agg_df["totals"]
    return agg_df
    

def create_aggregated_plot(
    df,
    xaxis_column=None,
    color_by_column=None,
    facet_by_column=None,
    agg_func="count",
    agg_column="uid",
    normalize_by_total_column=None,
    chart_type="bar",
    n_plot_rows=None,
    n_plot_cols=None,
):

    agg_df = create_aggregated_df(
        df=df,
        xaxis_column=xaxis_column,
        color_by_column=color_by_column,
        facet_by_column=facet_by_column,
        agg_func=agg_func,
        agg_column=agg_column,
        normalize_by_total_column=normalize_by_total_column,
    )

    agg_df = agg_df.sort_values(by="aggregated_value", ascending=False)

    if chart_type == "bar":
        chart_func = px.bar
    elif chart_type == "line":
        chart_func = px.line
    elif chart_type == "scatter":
        chart_func = px.scatter
    else:
        raise ValueError(f"Invalid chart type: {chart_type}")
    
    chart_kwargs = {}

    if xaxis_column:
        chart_kwargs["x"] = xaxis_column
    if color_by_column:
        chart_kwargs["color"] = color_by_column
    if facet_by_column:
        chart_kwargs["facet_col"] = facet_by_column
    if not normalize_by_total_column:
        chart_kwargs["y"] = "aggregated_value"
    else:
        chart_kwargs["y"] = "normalized_value"
    
    fig = chart_func(
        agg_df,
        **chart_kwargs,
    )

    # When faceting a plot, if the facet column and x-axis column are unique combinations,
    # the other faceted plots will have lots of blanks (this is evident when we have level1 on x and level0 on facet)
    # This code uses the work that plotly did above, but re-arranges as subplots
    if facet_by_column:
        facet_col_order = (
            agg_df
            .groupby(facet_by_column)
            .sum()
            .sort_values(
                by="aggregated_value",
                ascending=False
            )
            .index
        )

        n_plot_rows = n_plot_rows or 1
        n_plot_cols = n_plot_cols or len(facet_col_order)

        new_fig = make_subplots(
            rows=1,
            cols=len(facet_col_order),
            shared_yaxes=True,
            horizontal_spacing=0.03,
        )
        traces = [trace for trace in fig.select_traces()]
        for i, trace in enumerate(traces):
            xaxis_name = trace.xaxis
            col_n = 1
            if len(xaxis_name) > 1:
                col_n = int(xaxis_name[1:])
            new_fig.add_trace(trace, row=1, col=col_n)
        new_fig.layout.annotations = fig.layout.annotations

        for i, annotation in enumerate(new_fig.layout.annotations):
            annotation_text = annotation.text.split('=')[-1]
            annotation.update(text=annotation_text)

        new_fig.update_layout(
            legend={"tracegroupgap": 0},
        )
        fig = new_fig
    return fig


def make_timeseries_plot(
        df,
        facet_col=None,
        color_by_col=None,
        facet_col_rename=None,
        color_by_col_rename=None,
        chart_type='area',
):

    df, facet_col_rename, color_by_col_rename = _rename_columns(
        df,
        facet_col,
        color_by_col,
        facet_col_rename,
        color_by_col_rename,
    )

    funding_allocated_columns = [
        x for x in
        df.columns
        if '20' in x and 'Allocated' in x
    ]

    grouping_cols = []
    if color_by_col:
        grouping_cols.append(color_by_col_rename)

    if facet_col:
        grouping_cols.append(facet_col_rename)

    if grouping_cols:
        funding_timeseries = (
            df
            .groupby(grouping_cols)
            .sum()
            [funding_allocated_columns]
            .reset_index()
        )
        funding_timeseries = (
            funding_timeseries
            .melt(
                id_vars=grouping_cols,
                var_name='Year',
                value_name='Allocated Funding'
            )
        )
    else:
        funding_timeseries = df[funding_allocated_columns].sum().reset_index()
        funding_timeseries.rename(columns={0: 'Allocated Funding', 'index': "Year"}, inplace=True)
        funding_timeseries = (
            funding_timeseries
            .melt(
                id_vars='Year',
                value_name='Allocated Funding'
            )
        )

    funding_timeseries['Year_Int'] = (
        funding_timeseries['Year']
        .apply(lambda x: x.split('_')[1])
    )

    kwargs = {
        'x': 'Year_Int',
        'y': 'Allocated Funding',
    }
    if color_by_col:
        kwargs['color'] = color_by_col_rename
    if facet_col:
        kwargs['facet_col'] = facet_col_rename
    fig = px.area(
        funding_timeseries,
        **kwargs
    )

    fig.update_layout(
        title={
            "text": "Funding Over Time",
            "x": 0.5,
        },
        xaxis_title="Year",
        yaxis_title="Funding",
    )

    if facet_col:
        for annotation in fig.layout.annotations:
            annotation.update(text=annotation.text.split('=')[-1])

        for i in range(2, df[facet_col_rename].nunique() + 1):
            fig.update_yaxes(visible=False, showticklabels=False, row=1, col=i)
            fig.update_xaxes(title_text="Year", row=1, col=i)

    return fig
