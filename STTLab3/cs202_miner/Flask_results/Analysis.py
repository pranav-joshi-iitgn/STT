import pandas as pd
import os
pd.set_option('display.max_colwidth', 10)
data1 = pd.read_csv("Flask_results/commits_info_hist.csv")
data2 = pd.read_csv("Flask_results/commits_info_myers.csv")
print(data1.head(),"\n")
print(data2.head(),"\n")
data2["diff_hist"] = data1["diff_hist"]
data2["Matches"] = 1*(data2["diff_hist"] == data2["diff_myers"])
print(data2.head(),"\n")
eq = data2["Matches"].values.sum()
neq = len(data2["Matches"]) - eq
print("equal :",eq)
print("not equal :",neq)
print(round(100*neq/(neq+eq),2),"% match")
path = os.getcwd() + "/STTLab3/cs202_miner/Flask_results/commits_info_full.csv"
data2.to_csv(path,index=False)