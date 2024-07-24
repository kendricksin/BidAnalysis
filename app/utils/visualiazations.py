import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json

def create_bar_chart(data, x, y, title, x_label, y_label):
    """
    Create a bar chart using Plotly Express.
    
    :param data: DataFrame or Series containing the data
    :param x: Column name for x-axis
    :param y: Column name for y-axis
    :param title: Chart title
    :param x_label: Label for x-axis
    :param y_label: Label for y-axis
    :return: Plotly figure object
    """
    fig = px.bar(data, x=x, y=y, title=title)
    fig.update_xaxes(title=x_label)
    fig.update_yaxes(title=y_label)
    return fig

def create_pie_chart(data, values, names, title):
    """
    Create a pie chart using Plotly Express.
    
    :param data: DataFrame containing the data
    :param values: Column name for slice values
    :param names: Column name for slice names
    :param title: Chart title
    :return: Plotly figure object
    """
    fig = px.pie(data, values=values, names=names, title=title)
    return fig

def create_histogram(data, x, nbins=50, log_y=False, title='', x_label='', y_label='Count'):
    """
    Create a histogram using Plotly Express.
    
    :param data: DataFrame containing the data
    :param x: Column name for x-axis
    :param nbins: Number of bins (default: 50)
    :param log_y: Boolean to use log scale for y-axis (default: False)
    :param title: Chart title
    :param x_label: Label for x-axis
    :param y_label: Label for y-axis
    :return: Plotly figure object
    """
    fig = px.histogram(data, x=x, nbins=nbins, title=title)
    fig.update_xaxes(title=x_label)
    fig.update_yaxes(title=y_label, type='log' if log_y else 'linear')
    return fig

def create_time_series(data, x, y, title, x_label, y_label):
    """
    Create a time series plot using Plotly Express.
    
    :param data: DataFrame containing the data
    :param x: Column name for x-axis (typically dates)
    :param y: Column name for y-axis
    :param title: Chart title
    :param x_label: Label for x-axis
    :param y_label: Label for y-axis
    :return: Plotly figure object
    """
    fig = px.line(data, x=x, y=y, title=title)
    fig.update_xaxes(title=x_label)
    fig.update_yaxes(title=y_label)
    return fig

def create_box_plot(data, x, y, title, x_label, y_label):
    """
    Create a box plot using Plotly Express.
    
    :param data: DataFrame containing the data
    :param x: Column name for x-axis (categories)
    :param y: Column name for y-axis (values)
    :param title: Chart title
    :param x_label: Label for x-axis
    :param y_label: Label for y-axis
    :return: Plotly figure object
    """
    fig = px.box(data, x=x, y=y, title=title)
    fig.update_xaxes(title=x_label)
    fig.update_yaxes(title=y_label)
    return fig

def create_thailand_heatmap(data, province_column, value_column, title):
    """
    Create a heatmap of Thailand provinces using Plotly.
    
    :param data: DataFrame containing province data
    :param province_column: Column name for provinces
    :param value_column: Column name for values to be displayed
    :param title: Chart title
    :return: Plotly figure object
    """
    with open('app/data/thailand.json', 'r', encoding='utf-8') as f:
        geojson = json.load(f)

    fig = px.choropleth_mapbox(
        data,
        geojson=geojson,
        locations=province_column,
        color=value_column,
        featureidkey="properties.name",
        center={"lat": 13.7563, "lon": 100.5018},
        mapbox_style="carto-positron",
        zoom=4,
        opacity=0.5,
        title=title
    )

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

def create_heatmap(data, x, y, z, title, x_label, y_label, z_label):
    """
    Create a heatmap using Plotly Graph Objects.
    
    :param data: DataFrame containing the data
    :param x: Column name for x-axis
    :param y: Column name for y-axis
    :param z: Column name for z-axis (values)
    :param title: Chart title
    :param x_label: Label for x-axis
    :param y_label: Label for y-axis
    :param z_label: Label for z-axis (colorbar)
    :return: Plotly figure object
    """
    fig = go.Figure(data=go.Heatmap(
        z=data[z],
        x=data[x],
        y=data[y],
        colorscale='Viridis'))
    
    fig.update_layout(title=title,
                      xaxis_title=x_label,
                      yaxis_title=y_label)
    fig.update_traces(colorbar_title=z_label)
    return fig

# You can add more visualization functions as needed