import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mb = np.array([1.0, 1.7, 2.8, 4.6, 7.7, 12.9, 21.5, 35.9, 59.9, 100.0])

df = pd.read_csv("scan_run_[01-10].txt", sep="\s+")
mb_from_file = df[df.columns[1]]
xs = df[df.columns[2]]

plt.plot(mb, xs)
plt.xscale("log")
plt.xlabel("$m_b$ [GeV]")
plt.ylabel("$\sigma$ [pb]")
plt.savefig("xs(mb).pdf")
