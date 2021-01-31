# Copied from the Dash documetation sample code at https://github.com/plotly/dash-recipes/tree/master/multi-page-app
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from multi_page_app.app import app

layout = html.Div([
    html.H3('App 2'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
])


@app.callback(
    Output('app-2-display-value', 'children'),
    [Input('app-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)