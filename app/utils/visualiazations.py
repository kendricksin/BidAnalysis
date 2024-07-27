import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from scipy import stats

def create_bar_chart(data, x, y, title):
    fig = px.bar(data, x=x, y=y, title=title)
    return fig

def create_pie_chart(data, names, values, title):
    fig = px.pie(data, names=names, values=values, title=title)
    return fig

def create_histogram(data, x, title, nbins=30, log_y=False):
    fig = px.histogram(data, x=x, nbins=nbins, title=title)
    
    # Calculate normal distribution
    mean = np.mean(data[x])
    std = np.std(data[x])
    x_range = np.linspace(min(data[x]), max(data[x]), 100)
    y = stats.norm.pdf(x_range, mean, std)
    
    # Scale the normal distribution to match the histogram
    y_scaled = y * (len(data) * (max(data[x]) - min(data[x])) / nbins)
    
    # Add normal distribution curve
    fig.add_trace(go.Scatter(x=x_range, y=y_scaled, mode='lines', name='Normal Distribution'))
    
    if log_y:
        fig.update_yaxes(type="log")
    return fig

def create_thailand_bubble_map(data, lat, lon, size, title):
    # Cap the size at 5000 projects
    data['bubble_size'] = np.minimum(data[size], 5000)
    
    # Calculate size_max for better visualization
    size_max = data['bubble_size'].max()
    
    fig = go.Figure(go.Scattermapbox(
        lat=data[lat],
        lon=data[lon],
        mode='markers',
        marker=dict(
            size=data['bubble_size'],
            sizemode='area',
            sizeref=5.*size_max/(40.**2),
            sizemin=10,
            color=f'rgba(255, 0, 255, 0.5)',  # Semi-transparent blue
        ),
        text=data.apply(lambda row: f"{row['province']}: {row[size]} projects", axis=1),
        hoverinfo='text'
    ))

    fig.update_layout(
        title=title,
        mapbox_style="open-street-map",
        mapbox=dict(
            center=dict(lat=13.7563, lon=100.5018),  # Center on Bangkok
            zoom=5
        ),
        width=800,
        height=600,
    )

    return fig