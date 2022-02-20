import dash_bootstrap_components as dbc
from dash import Input, Output, Dash
from dash import html

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    # Title
    dbc.Row([
        dbc.Col(html.H1("Nurse Dashboard Log In", className='text-center text-primary'),
                width=12),
    ]),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    # First Row - Username input box
    dbc.Row([
        dbc.Col([]),
        dbc.Col([
            dbc.Label("Username", html_for="example-email"),
            dbc.Input(type="email", id="example-email", placeholder="Enter email"),
            dbc.FormText(
                "Enter your username",
                color="secondary", ),
        ]),
    ]),
    # Second Row - password input box
    dbc.Row([
        dbc.Col([]),
        dbc.Col([
            dbc.Label("Password", html_for="password-a"),
            dbc.Input(type="password", id="password-a", placeholder="Enter password"),
            dbc.FormText(
                "Enter your password",
                color="secondary", ),
        ])
    ]),
    # Third Row - Log In Button & Forgot username/password
    dbc.Row([
        dbc.Col([]),
        dbc.Col([
            dbc.Button("Log In", color="secondary", outline=True),
            dbc.Button("Forgot Username/Password", color="secondary", outline=True),
        ])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
