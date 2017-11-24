# https://pythonhosted.org/calmap/

import calmap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(sum(map(ord, 'calmap')))

all_days = pd.date_range('1/15/2014', periods=700, freq='D')
days = np.random.choice(all_days, 500)
events = pd.Series(np.random.randn(len(days)), index=days)

calmap.yearplot(events, year=2015)
plt.show()
