import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("eguraldia.csv")
plt.plot(df["eguna"], df["tenperatura"], label="Tenperatura")
plt.plot(df["eguna"], df["euria_mm"], label="Euria MM")
plt.title("Eguraldia")
plt.xlabel("Eguna")
plt.legend()
plt.show()


