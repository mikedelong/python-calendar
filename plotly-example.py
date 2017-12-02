# https://plot.ly/python/heatmaps/

import calendar
import datetime

import plotly.graph_objs as graph_objects
import plotly.offline

items = ['days']

end_date = datetime.date(year=2018, month=2, day=26)
start_date = datetime.date.today()

day_count = (end_date - start_date).days
holidays = [
    datetime.date(2017, 12, 25),
    datetime.date(2017, 12, 31),
    datetime.date(2018, 1, 1),
    datetime.date(2018, 1, 15),
]

date_list = [start_date + datetime.timedelta(days=day) for day in range(0, day_count) if
             (start_date + datetime.timedelta(days=day)).weekday() < 5]

weekday_count = 0
rows = []
for item in items:
    new_row = []
    for date in date_list:
        if date.weekday() < 5:
            if date in holidays:
                level = 0
                print(str(date) + ' Holiday ' + str(level))
            else:
                index = len(new_row)
                fraction = index / len(date_list)
                level = 1 if fraction < 0.7 else 2 if fraction < 0.8 else 3 if fraction < 0.9 else 4
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

nticks = len(date_list) / 5  # was 36
layout = graph_objects.Layout(xaxis=dict(ticks='', nticks=nticks), yaxis=dict(ticks=''))

fig = graph_objects.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='datetime-heatmap.html')
