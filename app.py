import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)
data = pd.read_csv("test_data.csv")
app.layout = html.Div(children=[
        html.H1(children="Jehovah's Witnesses Statistics"),
        html.P(children="Analyze various statistics of Jehovah's Witnesses"),
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

app.run_server(port=8050)