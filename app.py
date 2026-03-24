import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

#start dash app
app = Dash(__name__)

#load data
df = pd.read_csv("formatted_output.csv")

#prepare data
#convert date(text format) to date format
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

#create line chart x-axis date and y-axis sales
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Visualiser",
    labels={"sales":"Total Sales ($)", "date": "Date"}
)

#define layout
app.layout = html.Div(style={'fontFamily': 'sans-serif', 'padding': '20px'}, children=[
    html.H1(
        children="Soul Foods: Pink Morsel Sales Data",
        style={'textAlign': 'center', 'color': '#2c3e50'}
        ),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
        )
])

#run the server
if __name__ == '__main__':
    app.run(debug=True)

