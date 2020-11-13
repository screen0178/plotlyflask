"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
import dash_table
from datetime import datetime as dt
import dash_html_components as html
import dash_core_components as dcc
# from .data import create_dataframe
from .data import instalytics_dataframe
from .layout import html_layout
from dash.dependencies import Input, Output

# Load DataFrame
# df = create_dataframe()
df = instalytics_dataframe()


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            '/static/dist/css/styles.css',
            'https://fonts.googleapis.com/css?family=Lato'
        ]
    )

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            # create_data_graph(df),
            # create_data_table(df),
            datePicker(),
            instalytics_graph(df),
            instalytics_table(df)
        ],
        id='dash-container'
    )

    # Pass dash_app as a parameter
    init_callbacks(dash_app)

    return dash_app.server

# def create_data_graph(df):
#     graph = dcc.Graph(
#             id='histogram-graphh',
#             figure={
#                 'data': [{
#                     'x': df['complaint_type'],
#                     'text': df['complaint_type'],
#                     'customdata': df['key'],
#                     'name': '311 Calls by region.',
#                     'type': 'histogram'
#                 }],
#                 'layout': {
#                     'title': '311 Calls by region.',
#                     'height': 500,
#                     'padding': 150
#                 }
#             })
#     return graph

# def create_data_table(df):
#     """Create Dash datatable from Pandas DataFrame."""
#     table = dash_table.DataTable(
#         id='database-table',
#         columns=[{"name": i, "id": i} for i in df.columns],
#         data=df.to_dict('records'),
#         sort_action="native",
#         sort_mode='native',
#         page_size=20
#     )
#     return table

def instalytics_table(df):
    """Create instalytics data table"""
    tabel = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        page_size=20
    )
    return tabel

def instalytics_graph(df):
    graph = dcc.Graph(
            id='histogram-graph',
            figure={
                'data': [{
                    'x': df['ig_username'],
                    'name': 'Post by user.',
                    'type': 'histogram'
                }],
                'layout': {
                    'title': 'Insatgram Post by User.',
                    'height': 500,
                    'padding': 150
                }
            })
    return graph

def datePicker():
    datepick = dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2025, 12, 31),
        initial_visible_month=dt(2020, 8, 5),
        # end_date=dt(2020, 11, 11),
        minimum_nights=0,
        updatemode='singledate'
    )
    return datepick

def init_callbacks(app):
    @app.callback(
        Output('histogram-graph', 'children'),
        [Input('my-date-picker-range', 'start_date'),
        Input('my-date-picker-range', 'end_date')]
    )

    def update_output(start_date, end_date):
        print("Start date: " + start_date)
        print("End date: " + end_date)
        return print(dff = df.loc[start_date:end_date])
