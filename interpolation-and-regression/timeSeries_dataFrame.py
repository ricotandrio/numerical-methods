import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

time_series = pd.Series(np.random.rand(1000), index=pd.date_range("1/1/2000", periods=1000))
time_series = time_series.cumsum()

time_series.plot()

data_frame = pd.DataFrame(np.random.randn(1000, 10), index=time_series.index, columns=list("ABCDEFGHIJ"))
data_frame = data_frame.cumsum()

data_frame.plot()

plt.show()
