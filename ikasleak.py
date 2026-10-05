import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ikasleak_Matplot.csv")
plt.bar(df["ikasgela"], df.groupby("ikasgela")["ikasgela"].transform("count"), width=-0.35, align = "edge", label="Ikasle kopurua", color="Green")
plt.bar(df["ikasgela"], df.groupby("ikasgela")["nota"].transform("mean"), width=0.35, align = "edge", label="Bataz besteko nota", color="Red")
plt.title("Ikasgela")
plt.legend()
plt.show()