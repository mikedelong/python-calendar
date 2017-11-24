
import calmap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

start_date = datetime.datetime.today()
end_date = datetime.datetime(year=2018, month=2, day=28)
all_days = pd.date_range(start=start_date, end=end_date, freq='D')

days = np.random.choice(all_days, 50)
events = pd.Series(np.random.randn(len(days)), index=days)

calmap.calendarplot(events, monthticks=3, daylabels='MTWTFSS',
                    dayticks=[0, 2, 4, 6], cmap='YlGn',
                    fillcolor='grey', linewidth=0,
                    fig_kws=dict(figsize=(8, 4)))

plt.show()
