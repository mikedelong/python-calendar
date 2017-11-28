# https://plot.ly/python/heatmaps/

import datetime
import numpy as np
import plotly.offline
import plotly.graph_objs as graph_objects
import calendar

items = ['Days']

end_date = datetime.date(year=2018, month=2, day=26)
start_date = datetime.date.today()

day_count = (end_date - start_date).days
date_list = [end_date - datetime.timedelta(days=x) for x in range(0, day_count)]

z = []

busday_count = np.busday_count(start_date, end_date)
print(busday_count)

weekday_count = 0
for item in items:
    new_row = []
    for date in date_list:
        if date.weekday() < 5:
            print(str(date) + ' ' + calendar.day_name[date.weekday()])
            new_row.append(np.random.randint(low=0, high=4))
            weekday_count += 1
    z.append(list(new_row))

print('weekdays: ' + str(weekday_count) + ' total days: ' + str(day_count))
colorscale = 'Viridis'
data = [
    graph_objects.Heatmap(
        z=z,
        x=date_list,
        y=items,
        colorscale=colorscale,
    )
]

layout = graph_objects.Layout(
    # title='...',
    xaxis=dict(ticks='', nticks=36),
    yaxis=dict(ticks='')
)

fig = graph_objects.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='datetime-heatmap.html')
