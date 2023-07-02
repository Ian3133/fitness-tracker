import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import numpy as np

def bool2string(A):
    # convert a binary array into an array of strings 'True' and 'False'
    S = np.empty(A.shape, dtype=object)
    S[np.where(A)] = 'True'
    S[np.where(A == 0)] = 'False'
    return S

clrs = [[0, '#0000db'], [0.5, '#0000db'], [0.5, '#b10000'], [1, '#b10000']]

d = {
    'Week_1': [1, 0, 0, 1, 1, 0, 1]
}

figs = []

# Iterate over the keys in the dictionary
for key in d.keys():
    df = pd.DataFrame({key: d[key]})
    fig = go.Figure()

    fig.add_trace(
        go.Heatmap(
            z=df.values.T,
            coloraxis='coloraxis',
            xgap=1,
            customdata=bool2string(df.values.T),
            hovertemplate='%{customdata}<extra></extra>'
        )
    )

    fig.update_layout(
        title_text=f'{key} Graph',
        title_x=0.5,
        width=799,
        height=400,
        coloraxis=dict(colorscale=clrs, showscale=False),
        yaxis_showticklabels=False,
        xaxis=dict(
            tickmode='array',
            tickvals=np.arange(len(df.columns)),
            ticktext=df.columns
        )
    )

    figs.append(fig)

# Save the figures as images
for i, fig in enumerate(figs):
    fig.write_image(f'graph_{i+1}.png')
