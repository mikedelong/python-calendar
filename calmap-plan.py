import calmap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

start_date = datetime.datetime.today().date()
end_date = datetime.date(year=2018, month=2, day=28)

use_workdays = True
if use_workdays:
    frequency = 'B'
else:
    frequency = 'D'

all_days = pd.date_range(start=start_date, end=end_date, freq=frequency)

random_days = False
if random_days:
    days = np.random.choice(all_days, 50)
else:
    days = all_days.copy()
    travel_days = [
        datetime.date(year=2017, month=11, day=28),
        datetime.date(year=2017, month=11, day=29),
        datetime.date(year=2017, month=11, day=30),
        datetime.date(year=2017, month=12, day=1),
        datetime.date(year=2017, month=12, day=1),
        datetime.date(year=2017, month=12, day=4),
        datetime.date(year=2017, month=12, day=5),
        datetime.date(year=2017, month=12, day=6)
    ]
    days = days.drop(travel_days)
    holidays = [
        datetime.date(year=2017, month=12, day=25),
        datetime.date(year=2018, month=1, day=1),
        datetime.date(year=2018, month=1, day=15),
        datetime.date(year=2018, month=2, day=19)
    ]
    days = days.drop(holidays)

seventy = int(0.7 * len(days))
eighty = int(0.8 * len(days))
ninety = int(0.9 * len(days))

random_events = False
if random_events:
    events = pd.Series(np.random.randn(len(days)), index=days)
else:
    values = [1 if index < seventy else 2 if index < eighty else 3 if index < ninety else 4 for index in
              range(0, len(days))]
    events = pd.Series(values, index=days)

calmap.calendarplot(events,
                    cmap='YlGn',
                    daylabels='MTWTFSS',
                    fig_kws=dict(figsize=(8, 4)),
                    linewidth=0,
                    monthticks=3,
                    # dayticks=[0, 2, 4, 6],
                    # fillcolor='grey',
                    )

plt.show()
