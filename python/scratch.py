import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import plotly.io as pio

def bool2string(A):
    # convert a binary array into an array of strings 'True' and 'False'
    S = np.empty(A.shape, dtype=object)
    S[np.where(A)] = 'True'
    S[np.where(A == 0)] = 'False'
    return S

clrs = [[0, '#0000db'], [0.5, '#0000db'], [0.5, '#b10000'], [1, '#b10000']]

d = {
    'Week 0': [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    "week 1": [1, 0, 1, 1, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(d)
fig = make_subplots(rows=2, cols=1, shared_xaxes=True)

fig.update_layout(yaxis_domain=[0.75, 1], yaxis2_domain=[0, 0.725])
groups = list(df.columns)
A = df.values.T
fig.add_trace(
    go.Heatmap(
        z=A,
        coloraxis='coloraxis',
        xgap=1,
        ygap=1,
        customdata=bool2string(A),
        hovertemplate='%{customdata}<extra></extra>'
    ),
    2, 1
)

and_01 = np.array(np.logical_and(A[0], A[1]), int).reshape(1, -1)

fig.add_trace(
    go.Heatmap(
        z=and_01,
        coloraxis='coloraxis',
        xgap=1,
        customdata=bool2string(and_01),
        hovertemplate='%{customdata}<extra></extra>'
    ),
    1, 1
)

fig.update_layout(
    title_text='Your title',
    title_x=0.5,
    width=799,
    height=400,
    coloraxis=dict(colorscale=clrs, showscale=False),
    yaxis2_tickvals=[0, 1, 2],
    yaxis2_ticktext=groups,
    yaxis2_autorange='reversed',
    yaxis_showticklabels=False,
    yaxis_title=f'{groups[0]}<br>and<br>{groups[1]}'
)

# Save the figure as an image
pio.write_image(fig, 'graph.jpg')