import plotly.graph_objects as go
import plotly.io as pio
from  plotly.subplots import make_subplots
import pandas as pd
import datetime as dt
import numpy as np
from main import streching
from graphing import calc_time



def plot_streching():
    summer_starts = dt.datetime(2023, 6, 5).date()
    current_date = summer_starts
    summer = []
    for i in range(90):            
        summer.append(current_date)
        current_date += dt.timedelta(days=1)

    streching_vals = calc_time(summer_starts, streching, summer)

    strech_bool = []
    for i in streching_vals:     # can do a date check here so its only upto the day
        if i == "0:00":
            strech_bool.append(0)
        else:
            strech_bool.append(1)

    #week1 = strech_bool[:7]
    week2 = strech_bool[7:14]
    week3 = strech_bool[14:21]
    week4 = strech_bool[21:28]
    week5 = strech_bool[28:35]
    week6 = strech_bool[35:42]
    week7 = strech_bool[42:49]
    week8 = strech_bool[49:56]
    week9 = strech_bool[56:63]
    week10 = strech_bool[63:70]
    #week11 = strech_bool[63:70]
    #week12 = strech_bool[63:70]

    def bool2string(A):
        # Convert a binary array into an array of strings 'Yes' and 'No'
        S = np.where(A, 'Yes', 'No')
        return S

    clrs = [
        [0, '#b10000'],  # Map 0 (No) to red
        [1, '#b10000'],  # Map values between 0 and 0.5 to red
        [1, '#00b100'],  # Map values between 0.5 and 1 to green
        [1, '#00b100']  # Map 1 (Yes) to green
    ]

    d = {
        'Week of: 6/12' : week2,
        " 6/19" : week3,
        " 6/26" : week4, 
        "6/19" : week5,
        "7/03" : week6,
        "7/10" : week7,
        "7/17" : week8,
        "7/24": week9,
        "7/31 ": week10
        #"Week of 8/7": week3,
        # "Week of 8/14 ": week4,
        }

    df = pd.DataFrame(d)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[.75, 0])

    fig.update_layout(yaxis_domain=[.75, 1], yaxis2_domain=[0, 1]) 
    groups = list(df.columns)
    A = df.values.T
    fig.add_trace(go.Heatmap(z=A, coloraxis='coloraxis', xgap=1, ygap=1, customdata=bool2string(A),
                            hovertemplate='%{customdata}<extra></extra>'), 2, 1)
    and_01 = np.array(np.logical_and(A[0], A[1]), int).reshape(1, -1)
    #fig.add_trace(go.Heatmap(z=and_01, coloraxis='coloraxis', xgap=1, customdata=bool2string(and_01),
    #                         hovertemplate='%{customdata}<extra></extra>'), 1, 1)

    fig.update_layout(
        title_text='Streching Consistency',
        title_x=0.5,
        width=799,
        height=400,
        coloraxis=dict(colorscale=clrs, showscale=False),
        yaxis2_tickvals=[0, 1, 2, 3, 4,5,6,7,8,9,10], # what ones get titles
    yaxis2_ticktext=groups,
        yaxis2_autorange='reversed',
        #yaxis_showticklabels=False,
        #yaxis_title=f'{groups[0]}<br>and<br>{groups[1]}'
    )

    fig.update_traces(xaxis='x2', selector=dict(type='heatmap')) 


    for i in range(8):  # can do a lot simpler but works so no worries 
        fig.update_xaxes(
            tickvals=np.arange(7),
            ticktext=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            row=i+1, col=1
        )

    # fig.update_xaxes(
    #     tickvals=np.arange(7),
    #     ticktext=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    #     row=2, col=1
    # )


    pio.write_image(fig, 'fitness-tracker/images/graph_image.png')