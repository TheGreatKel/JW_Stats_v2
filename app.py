import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd




app = dash.Dash(__name__)
data = pd.read_csv("test_data.csv")
map_data = pd.read_csv("test_map_data.csv")
print(map_data.dtypes["Country or Territory"])

# map_data.isnull()
# map_data.fillna(0, inplace=True)
# map_data.isnull()

# #map figure
# fig = px.scatter_geo(map_data, locations="Country or Territory", locationmode="country names",
#                      hover_name="Country or Territory", size="Population",
#                      projection="natural earth")

# app.layout = html.Div(children=[
#     html.Div(children=[
#         html.H1(children="Jehovah's Witnesses Statistics", className="center"),
#         html.H2(children="Grand Totals", className="center"),
#         html.Br(),
#         dcc.Dropdown(
#             id="year-dropdown",
#             options=[{'label': x, 'value': x}
#                      for x in data["Year"].tolist()],
#             value=data["Year"].tolist()[0]),
#         dcc.Dropdown(
#             id="year-dropdown-2",
#             options=[{'label': x, 'value': x}
#                      for x in data["Year"].tolist()],
#             value=data["Year"].tolist()[0]),
#     ]),
#     html.Div(className="grid", children=[
#         dcc.Graph(id="total-congs", style={'width': '400px'}),
#         dcc.Graph(id="memorial-attendance", style={'width': '400px'}),
#         dcc.Graph(id="memorial-partakers", style={'width': '400px'}),
#         dcc.Graph(id="peak-pubs", style={'width': '400px'}),
#         dcc.Graph(id="av-pubs", style={'width': '400px'}),
#         dcc.Graph(id="total-bap", style={'width': '400px'}),
#         dcc.Graph(id="total-hours", style={'width': '400px'}),
#         dcc.Graph(id="av-studies", style={'width': '400px'})
    
#     ]),
#     html.H2(children="World Map", className="center"),
#     html.Div(className="map", children=[
#         dcc.Graph(figure = fig, id="world-map", style={'width': '600px'})
#     ])
# ])    

# @app.callback(
#     [Output("memorial-attendance","figure"),Output("memorial-partakers","figure"),Output("peak-pubs","figure"),
#     Output("av-pubs","figure"),Output("total-bap","figure"),Output("total-hours","figure"),
#     Output("av-studies","figure"),Output("total-congs","figure")],
#     [
#         Input('year-dropdown','value'),
#         Input("year-dropdown-2",'value'),
#     ],
# )

# def update_charts(year1, year2):
#     mask = (data['Year'] > year1) & (data['Year'] <= year2)
#     filtered_data = data.loc[mask, :]
#     memorial_attendance_figure={
#         "data": [
#             {
#                 "x": filtered_data["Year"],
#                 "y": filtered_data["Worldwide Memorial Attendance"],
#                 "type": "lines",
#             },
#         ],
#        "layout": {"title": "Worldwide Memorial Attendance"},
#     }
#     memorial_partakers_figure={
#         "data": [
#             {
#                 "x": filtered_data["Year"],
#                 "y": filtered_data["Memorial Partakers Worldwide"],
#                 "type": "lines",
#             },
#         ],
#        "layout": {"title": "Memorial Partakers Worldwide"},
#     }
#     peak_pubs_figure={
#         "data": [
#             {
#                 "x": filtered_data["Year"],
#                 "y": filtered_data["Peak of Publishers"],
#                 "type": "lines",
#             },
#         ],
#        "layout": {"title": "Peak of Publishers"},
#     }
#     av_pubs_figure={
#         "data": [
#             {
#                 "x": filtered_data["Year"],
#                 "y": filtered_data["Average Publishers Preaching Each Month"],
#                 "type": "lines",
#             },
#         ],
#        "layout": {"title": "Average Publishers Preaching Each Month"},
#     }
#     total_bap_figure={
#         "data": [
#             {
#                 "x": filtered_data["Year"],
#                 "y": filtered_data["Total Number Baptized"],
#                 "type": "lines",
#             },
#         ],
#        "layout": {"title": "Total Number Baptized"},
#     }
#     total_hours_figure={
#         "data": [
#             {
#                 "x": filtered_data["Year"],
#                 "y": filtered_data["Total Hours Spent in Field"],
#                 "type": "lines",
#             },
#         ],
#        "layout": {"title": "Total Hours Spent in Field"},
#     }
#     av_studies_figure={
#         "data": [
#             {
#                 "x": filtered_data["Year"],
#                 "y": filtered_data["Average Bible Studies Each Month"],
#                 "type": "lines",
#             },
#         ],
#        "layout": {"title": "Average Bible Studies Each Month"},
#     }
#     total_congs_figure={
#         "data": [
#             {
#                 "x": filtered_data["Year"],
#                 "y": filtered_data["Total Congregations"],
#                 "type": "lines",
#             },
#         ],
#        "layout": {"title": "Total Congregations"},
#     }
#     # map_figure={
#     #     "data": [
#     #         {
#     #             "data": map_data,
#     #             "locations": 
#     #             "type": "scattergeo",
#     #         },
#     #     ],
#     #    "layout": {"title": "Jehovah's Witnesses Worldwide"},
#     # }
#     return memorial_attendance_figure,memorial_partakers_figure,peak_pubs_figure,av_pubs_figure,total_bap_figure,total_hours_figure,av_studies_figure,total_congs_figure#, map_figure

# if __name__ == '__main__':
#     app.run_server(debug=True, port=8050)
