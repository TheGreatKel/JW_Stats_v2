import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)
data = pd.read_csv("test_data.csv")
app.layout = html.Div(children=[
    html.Div(children=[
        html.H1(children="Jehovah's Witnesses Statistics"),
        html.P(children="Analyze various statistics of Jehovah's Witnesses"),
        html.Br(),
        dcc.Dropdown(
            id="year-dropdown",
            options=[{'label': x, 'value': x}
                     for x in data["Year"].tolist()],
            value=data["Year"].tolist()[0]),
        dcc.Dropdown(
            id="year-dropdown-2",
            options=[{'label': x, 'value': x}
                     for x in data["Year"].tolist()],
            value=data["Year"].tolist()[0]),
    ]),
    html.Div(children=[
        dcc.Graph(id="total-congs"),
        dcc.Graph(id="memorial-attendance"),
        dcc.Graph(id="memorial-partakers"),
        dcc.Graph(id="peak-pubs"),
        dcc.Graph(id="av-pubs"),
        dcc.Graph(id="total-bap"),
        dcc.Graph(id="total-hours"),
        dcc.Graph(id="av-studies")
    
    ]),

        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["Total Congregations"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Total Congregations"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["Worldwide Memorial Attendance"],
                        "type": "lines",
                    },
                ],
               "layout": {"title": "Worldwide Memorial Attendance"},
            },
       ),
       dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["Memorial Partakers Worldwide"],
                        "type": "lines",
                    },
                ],
               "layout": {"title": "Memorial Partakers Worldwide"},
            },
       ),
       dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["Peak of Publishers"],
                        "type": "lines",
                    },
                ],
               "layout": {"title": "Peak of Publishers"},
            },
       ),
       dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["Average Publishers Preaching Each Month"],
                        "type": "lines",
                    },
                ],
               "layout": {"title": "Average Publishers Preaching Each Month"},
            },
       ),
       dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["Total Number Baptized"],
                        "type": "lines",
                    },
                ],
               "layout": {"title": "Total Number Baptized"},
            },
       ),
       dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["Total Hours Spent in Field"],
                        "type": "lines",
                    },
                ],
               "layout": {"title": "Total Hours Spent in Field"},
            },
       ),
       dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["Average Bible Studies Each Month"],
                        "type": "lines",
                    },
                ],
               "layout": {"title": "Average Bible Studies Each Month"},
            },
       ),
    ]
)

@app.callback(
    [Output("memorial-attendance","figure"),Output("memorial-partakers","figure"),Output("peak-pubs","figure"),
    Output("av-pubs","figure"),Output("total-bap","figure"),Output("total-hours","figure"),Output("av-studies","figure")]
    [
        Input(),
        Input(),
        
    ],
    
)

app.run_server(port=8050)