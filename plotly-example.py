# https://plot.ly/python/heatmaps/

import calendar
import datetime

import numpy as np
import plotly.graph_objs as graph_objects
import plotly.offline

items = ['days']

end_date = datetime.date(year=2018, month=2, day=26)
start_date = datetime.date.today()

day_count = (end_date - start_date).days
date_list = [end_date - datetime.timedelta(days=day) for day in range(0, day_count)]

busday_count = np.busday_count(start_date, end_date)

holidays = [
    datetime.date(2017, 12, 25),
    # datetime.date(2017, 12, 31),
    datetime.date(2018, 1, 1),
    datetime.date(2018, 1, 15),
]

weekday_count = 0
rows = []
for item in items:
    new_row = []
    for date in date_list:
        if date.weekday() < 5:
            if date in holidays:
                level = 0
                print(str(date) + ' Holiday ' + str(level))
                new_row.append(level)
            else:
                index = len(new_row)
                fraction = index / busday_count
                level = 1 if fraction > 0.3 else 2 if fraction > 0.2 else 3 if fraction > 0.1 else 4
                print(str(date) + ' ' + calendar.day_name[date.weekday()] + ' ' + str(level))
                weekday_count += 1
            new_row.append(level)
    rows.append(list(new_row))

print('weekdays: ' + str(weekday_count) + ' total days: ' + str(day_count))
# colorscale = 'Viridis'
colorscale = 'Plasma'
data = [
    graph_objects.Heatmap(
        z=rows,
        x=date_list,
        y=items,
        colorscale=colorscale,
    )
]

nticks = busday_count / 5  # was 36
layout = graph_objects.Layout(xaxis=dict(ticks='', nticks=nticks), yaxis=dict(ticks=''))

fig = graph_objects.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='datetime-heatmap.html')
