# https://pythonhosted.org/calmap/

import numpy as np; np.random.seed(sum(map(ord, 'calmap')))
import pandas as pd
import calmap
import matplotlib.pyplot as plt


all_days = pd.date_range('1/15/2014', periods=700, freq='D')
days = np.random.choice(all_days, 500)
events = pd.Series(np.random.randn(len(days)), index=days)

calmap.calendarplot(events, monthticks=3, daylabels='MTWTFSS',
                    dayticks=[0, 2, 4, 6], cmap='YlGn',
                    fillcolor='grey', linewidth=0,
                    fig_kws=dict(figsize=(8, 4)))

plt.show()
