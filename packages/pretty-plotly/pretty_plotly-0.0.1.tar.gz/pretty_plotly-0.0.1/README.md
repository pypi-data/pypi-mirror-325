# Pretty Plotly

This module provides a set of functions to create various types of plots using Plotly. It includes functions for setting the renderer, plotting scatter plots, creating traces, histograms, candlestick charts, and collections of plots.

## Functions

### `set_renderer(renderer="plotly_mimetype+notebook")`

Set the default renderer for Plotly plots.

**Parameters:**
- `renderer` (str): The name of the renderer to set as the default. Defaults to "plotly_mimetype+notebook".

**Returns:**
- `None`

**Example:**
```
import plotly.io as pio
set_renderer("notebook_connected")
print(pio.renderers.default)  # Output: notebook_connected
```

### `plot_data(x=None, y=None, z=None, size=None, colour=None, title="", colour_title="", x_label="", y_label="", name="", mode="markers", text="", fill=None, **traces)`

General purpose function for plotting scatter plots in Plotly.

**Parameters:**
- `x` (list or array-like, optional): x-coordinates of the data points.
- `y` (list or array-like, optional): y-coordinates of the data points.
- `z` (list or array-like, optional): z-coordinates of the data points for 3D plots.
- `size` (list or array-like, optional): Sizes of the markers.
- `colour` (list or array-like, optional): Colors of the markers.
- `title` (str, optional): Title of the plot.
- `colour_title` (str, optional): Title of the colorbar.
- `x_label` (str, optional): Label for the x-axis.
- `y_label` (str, optional): Label for the y-axis.
- `name` (str, optional): Name of the trace.
- `mode` (str, optional): Mode of the scatter plot.
- `text` (list or array-like, optional): Text labels for the data points.
- `fill` (str, optional): Fill type for the markers.
- `**traces` (dict, optional): Additional traces to be added to the plot.

**Returns:**
- `fig` (plotly.graph_objects.Figure): The scatter plot figure.

**Example:**
```
import plotly.graph_objects as go

fig = plot_data(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    size=[40, 60, 80, 100],
    colour=[0, 1, 2, 3],
    title="Scatter Plot Example",
    x_label="X Axis",
    y_label="Y Axis"
)
fig.show()
```

### `create_trace(x=None, y=None, z=None, size=None, colour=None, colour_title="", name="", mode="lines", text="", fill=None)`

Create a trace for a plot.

**Parameters:**
- `x` (list): x-coordinates of the trace.
- `y` (list): y-coordinates of the trace.
- `z` (list): z-coordinates of the trace (for 3D plots).
- `size` (int): Size of the markers.
- `colour` (list): Colour of the markers.
- `colour_title` (str): Title for the colour bar.
- `name` (str): Name of the trace.
- `mode` (str): Mode of the trace (e.g., 'lines', 'markers', 'lines+markers').
- `text` (list): Text associated with each marker.
- `fill` (str): Fill type for the trace (for area plots).

**Returns:**
- `trace` (go.Scatter or go.Scatter3d): The created trace object.

**Example:**
```
trace = create_trace(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode="lines+markers",
    name="Example Trace"
)
fig = go.Figure(data=[trace])
fig.show()
```

### `create_histogram(x=None, y=None, histnorm="", name="")`

Create a histogram plot.

**Parameters:**
- `x` (list or array-like): Data for the x-axis.
- `y` (Not used in this function).
- `histnorm` (str): Type of normalization used for the histogram. Default is "" (no normalization).
- `name` (str): Name of the histogram plot.

**Returns:**
- `go.Histogram`: The histogram plot object.

**Example:**
```
hist = create_histogram(
    x=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
    histnorm="probability",
    name="Example Histogram"
)
fig = go.Figure(data=[hist])
fig.show()
```

### `create_candle_stick(x=None, open=None, close=None, high=None, low=None, name="")`

Create a candlestick chart object.

**Parameters:**
- `x` (list): List of x-axis values.
- `open` (list): List of opening prices.
- `close` (list): List of closing prices.
- `high` (list): List of high prices.
- `low` (list): List of low prices.
- `name` (str): Name of the candlestick chart.

**Returns:**
- `go.Candlestick`: The candlestick chart object.

**Example:**
```
candlestick = create_candle_stick(
    x=["2021-01-01", "2021-01-02", "2021-01-03"],
    open=[100, 110, 105],
    close=[110, 105, 115],
    high=[115, 120, 125],
    low=[95, 100, 105],
    name="Example Candlestick"
)
fig = go.Figure(data=[candlestick])
fig.show()
```

### `plot_collection(plots, rows=1, cols=1, title="", subplot_titles=[], x_labels={}, y_labels={}, height=1000)`

Create a collection of plots arranged in a grid layout.

**Parameters:**
- `plots` (dict): A dictionary containing the plots to be added to the collection. The keys represent the position of the plot in the grid (row, col), and the values are instances of the `Plot` class.
- `rows` (int): The number of rows in the grid layout. Default is 1.
- `cols` (int): The number of columns in the grid layout. Default is 1.
- `title` (str): The title of the plot collection. Default is an empty string.
- `subplot_titles` (list): A list of titles for each subplot. The length of the list should be equal to the number of subplots. Default is an empty list.
- `x_labels` (dict): A dictionary mapping the position of each subplot to its x-axis label. Default is an empty dictionary.
- `y_labels` (dict): A dictionary mapping the position of each subplot to its y-axis label. Default is an empty dictionary.
- `height` (int): The height of the plot collection in pixels. Default is 1000.

**Returns:**
- `fig` (plotly.graph_objects.Figure): The plotly figure object representing the plot collection.

**Example:**
```
scatter_plot = plot_data(
    x=[1, 2, 3],
    y=[4, 5, 6],
    title="Scatter Plot",
    x_label="X Axis",
    y_label="Y Axis"
)

histogram = create_histogram(
    x=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
    name="Histogram"
)

plots = {
    (1, 1): scatter_plot,
    (1, 2): histogram
}

fig = plot_collection(
    plots=plots,
    rows=1,
    cols=2,
    title="Plot Collection",
    subplot_titles=["Scatter Plot", "Histogram"]
)
fig.show()
```