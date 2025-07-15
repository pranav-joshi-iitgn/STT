import matplotlib.pyplot as plt
import pandas as pd
import os
from ast import literal_eval
data1 = pd.read_csv("Flask_results/commits_info_hist.csv")
data2 = pd.read_csv("Flask_results/commits_info_myers.csv")
data2["diff_hist"] = data1["diff_hist"]
data2["equal"] = 1*(data2["diff_hist"] == data2["diff_myers"])
eq = data2["equal"].values.sum()
neq = len(data2["equal"]) - eq
print("equal :",eq)
print("not equal :",neq)
data2.to_csv("Flask_results/commits_info_full.csv",index=False)