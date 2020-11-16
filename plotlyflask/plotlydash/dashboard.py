"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
import dash_table
from datetime import datetime as dt
import dash_html_components as html
import dash_core_components as dcc
from .data import instalytics_dataframe
from .layout import html_layout
from dash.dependencies import Input, Output
import plotly.express as px

# Load DataFrame
df = instalytics_dataframe()

# Prepare initial data
df_init = df[['ig_username','like_count']].groupby(['ig_username'], sort=False).sum().reset_index()
df_init.sort_values('like_count', axis = 0, ascending = False, 
                 inplace = True, na_position ='last') 
# print(df_init[:25])


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
            datePicker(),
            radioButton(),
            # dropDown(),
            instalytics_graph(df_init),
            instalytics_table(df_init)
        ],
        id='dash-container'
    )

    # Calling callback function
    init_callbacks(dash_app)

    # Pass dash_app as a parameter
    return dash_app.server 

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
    df = df[0:25]
    graph = dcc.Graph(
            id='histogram-graph',
            figure=
            {
                'data': [{
                    'x': df['ig_username'],
                    'y': df['like_count'],
                    'name': 'total like per user.',
                    'type': 'bar'
                }],
                'layout': {
                    'title': 'Like Count per User.',
                    'height': 500,
                    'padding': 150
                }
            }
            )
    return graph

def datePicker():
    datepick = dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2025, 12, 31),
        initial_visible_month=dt(2020, 10, 1),
        # end_date=dt(2020, 11, 11),
        minimum_nights=0,
        updatemode='singledate'
    )
    return datepick

def radioButton():
    radItem = dcc.RadioItems(
        id = 'radio-item',
        options = [
            {'label': 'Daily', 'value': 'daily'},
            {'label': 'Monthly', 'value': 'monthly'},
            {'label': 'Dynamic', 'value': 'dinamis'}
        ],
        value = 'dinamis'
    )
    return radItem

# def dropDown():
#     drpDown = dcc.Dropdown(
#         id='drop-down',
#         option=[
#             {'label': 'Jan', 'value': 1},
#             {'label': 'Feb', 'value': 2},
#             {'label': 'Mar', 'value': 3},
#             {'label': 'Apr', 'value': 4},
#             {'label': 'Mei', 'value': 5},
#             {'label': 'Jun', 'value': 6},
#             {'label': 'Jul', 'value': 7},
#             {'label': 'Aug', 'value': 8},
#             {'label': 'Sep', 'value': 9},
#             {'label': 'Oct', 'value': 10},
#             {'label': 'Nov', 'value': 11},
#             {'label': 'Des', 'value': 12},
#         ],
#         value=1
#     )
#     return drpDown

def init_callbacks(app):
    @app.callback(
        Output('histogram-graph', 'figure'),
        [Input('radio-item', 'value'),
        Input('my-date-picker-range', 'start_date'),
        Input('my-date-picker-range', 'end_date'),],
        prevent_initial_call=True
    )

    def update_output(value, start_date, end_date):
        if value == 'dinamis':
            print("Start date: " + start_date)
            print("End date: " + end_date)
            mask = (df['taken_at'] >= start_date) & (df['taken_at'] <= end_date)
            dff = df.loc[mask]

            dff = dff[['ig_username','like_count']].groupby(['ig_username'], sort=False).sum().reset_index()
            dff.sort_values('like_count', axis = 0, ascending = False, 
                                inplace = True, na_position ='last')
            # print(dff)
            dff = dff[0:25]
            fig = {
                    'data': [{
                        'x': dff['ig_username'],
                        'y': dff['like_count'],
                        'name': 'Post by user.',
                        'type': 'bar'
                    }],
                    'layout': {
                        'title': 'Total like from {} until {} per account'.format(start_date,end_date),
                        'height': 500,
                        'padding': 150
                    }
                }
        elif value == 'daily':
            dff = df.groupby(['ig_username',pd.Grouper(key='taken_at')])['like_count'].sum().reset_index()
            dff['taken_at_daily'] = dff['taken_at'].dt.day
            mask = dff['taken_at'].dt.month == 9
            dff = dff.loc[mask]

            fig = px.bar(
                data_frame=dff,
                x='taken_at_daily',
                y='like_count',
                color='ig_username',
                opacity=0.9,
                barmode='relative'
            )
        elif value == 'monthly':
            dff = df.groupby(['ig_username',pd.Grouper(key='taken_at')])['like_count'].sum().reset_index()
            dff['taken_at_monthly'] = dff['taken_at'].dt.month

            fig = px.bar(
                data_frame=dff,
                x='taken_at_monthly',
                y='like_count',
                color='ig_username',
                opacity=0.9,
                barmode='relative'
            )
        return fig

        # @app.callback(
        #     Output('histogram-graph', 'figure'),
        #     Input('radio-item', 'value'),
        #     prevent_initial_call=True
        # )

        # def graph_update(cat):
        #     if cat == 'daily':
        #         dff = df.groupby(['ig_username',pd.Grouper(key='taken_at')])['like_count'].sum().reset_index()
        #         dff['taken_at_daily'] = dff['taken_at'].dt.day
        #         mask = dff['taken_at'].dt.month == 9
        #         dff = dff.loc[mask]

        #     fig = px.bar(
        #         data_frame=dff,
        #         x='taken_at_daily',
        #         y='like_count',
        #         color='ig_username',
        #         opacity=0.9,
        #         barmode='relative'
        #     )
        #     return fig

