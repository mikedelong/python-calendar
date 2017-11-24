
import calmap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

start_date = datetime.datetime.today()
end_date = datetime.datetime(year=2018, month=2, day=28)

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

random_events = False
if random_events:
    events = pd.Series(np.random.randn(len(days)), index=days)
else:
    values = [index for index in range(0, len(days))]
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
