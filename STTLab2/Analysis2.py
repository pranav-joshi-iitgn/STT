import os
import pandas as pd
Winner = []
Reason = []
for i in range(50):
    file = f"row{i+1}/context.txt"
    s =open(file,'r').read().split("\n")
    n = len(s)
    assert n == 10
    Winner.append(s[-2])
    Reason.append(s[-1])
context = ["Bug type","Commit Message","File Path","Fixed Commit"]
data = pd.read_csv("flask.csv")[context].iloc[:50]
data["Better"] = Winner
data["Reason"] = Reason
pd.options.display.max_colwidth =30
print(data)
data.to_csv("data.csv",index=False)