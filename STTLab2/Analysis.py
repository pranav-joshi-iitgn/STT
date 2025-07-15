import pandas as pd
import os
data = pd.read_csv("flask.csv")
data["URL"] = "https://github.com/pallets/flask/commit/" + data["Fixed Commit"]
data = data.iloc[:50]
context = ["Bug type","Commit Message","File Path","Fixed Commit","Buggy Commit","URL"]
C = data[context]
L = data["Location"]
before = data["Before Bug fix"]
after = data["After Bug fix"]
for i in range(50):
    fold = f"row{i+1}"
    try:os.mkdir(fold)
    except: pass
    f = open(fold + "/before.txt",'w')
    f.write(before[i])
    f.close()
    f = open(fold + "/after.txt",'w')
    f.write(after[i])
    f.close()
    f = open(fold + "/context.txt",'w')
    s = L[i] + "\n" + "\n".join([f"{attr} : {C[attr][i]}" for attr in context])
    f.write(s)
    f.close()
