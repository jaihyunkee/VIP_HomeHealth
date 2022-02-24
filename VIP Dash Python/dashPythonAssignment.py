import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3("VIP Computer Programming Assignments"),
    html.H5("by Jaihyun Kee"),
    html.Div(children='''Please enter number between 1 to 4'''),
    html.Br(),
    dcc.Input(id='input1', type='number', value='0'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    dcc.Graph(
        id='life-exp-vs-gdp'
    )])

@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    Input('submit-button-state', 'n_clicks'),
    State('input1', 'value'))

def update_graph(n_clicks, input1):
    fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                     size="population", color="continent", hover_name="country",
                     log_x=True, size_max=60)
    if input1 == 1:
        fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                         size="population", color="continent", hover_name="country",
                         log_x=True, size_max=60)
        fig.update_layout(transition_duration=40)
        return fig
    if input1 == 2:
        fig = px.scatter(df, x="gdp per capita", y="life expectancy", title='gdp per capita vs life expectancy')
        fig.update_layout(transition_duration=40)
        return fig
    if input1 == 3:
        fig = px.scatter(df2, x='pork', y='beef', size='total exports', color='state')
        fig.update_layout(transition_duration=40)
        return fig
    if input1 == 4:
        fig = px.scatter(df2, x='poultry', y='dairy', size='total exports', color='state')
        fig.update_layout(transition_duration=40)
        return fig
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
