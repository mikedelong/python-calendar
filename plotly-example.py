# https://plot.ly/python/heatmaps/

import datetime
import numpy as np
import plotly.offline
import plotly.graph_objs as go

programmers = ['Alex', 'Nicole',
               # 'Sara', 'Etienne', 'Chelsea', 'Jody', 'Marianne'
               ]

end_date = datetime.date(year=2018, month=2, day=26)
start_date  = datetime.date.today()

day_count = (end_date - start_date).days
date_list = [end_date - datetime.timedelta(days=x) for x in range(0, day_count)]

z = []

for person in programmers:
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
plotly.offline.plot(fig, filename='datetime-heatmap.html')
