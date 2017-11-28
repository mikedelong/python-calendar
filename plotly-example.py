# https://plot.ly/python/heatmaps/

import datetime
import numpy as np
import plotly.offline
import plotly.graph_objs as go

programmers = ['Alex', 'Nicole', 'Sara', 'Etienne', 'Chelsea', 'Jody', 'Marianne']

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, 180)]

z = []

for prgmr in programmers:
    new_row = []
    for date in date_list:
        new_row.append(np.random.poisson())
    z.append(list(new_row))

data = [
    go.Heatmap(
        z=z,
        x=date_list,
        y=programmers,
        colorscale='Viridis',
    )
]

layout = go.Layout(
    title='GitHub commits per day',
    xaxis=dict(ticks='', nticks=36),
    yaxis=dict(ticks='')
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='datetime-heatmap')
pass
