import matplotlib.pyplot as plt
import pandas as pd
import os
from ast import literal_eval
data = pd.read_csv("STTLab4/cs202_miner/Flask_results/commits_info_comp_clean.csv").dropna(subset=["new_file path","old_file path"])
print(len(data))
edges = data[["old_file path","new_file path","commit SHA","new_file_MCC"]]
edges = list(edges.values)
print("file name changes will be printed :")
fc = {}
for e in edges:
    old,new,commit,comp =e
    if old == new:
        if old in fc:fc[old].append((commit,new,comp))
        else:fc[old] = [(commit,new,comp)]
        continue
    e_desc = f"{commit} : {old} -> {new}"
    print(e_desc)
    if old in fc:
        fc[new] = fc[old]
        fc[new].append((commit,new,comp))
        fc[old] = []
    else:
        assert (new not in fc or fc[new] == []),f"{fc[new][-1]} already uses file name {new}. So, {commit} can't rename {old} to it."
        fc[new] = [commit]
lens = [(len(fc[final]),final) for final in fc]
lens = sorted(lens,reverse=True)
top3 = lens[:3]
print("\nTop 3 are :")
for x in top3:print(x[1],":",x[0],"commits")
top3 = [x[1] for x in top3]
top3_commits = [fc[x] for x in top3]
for i,final_name in enumerate(top3):
    commits = top3_commits[i]
    f = open("STTLab4/cs202_miner/Flask_results/" + final_name.split("/")[-1] + ".changes",'w')
    S = "\n".join([",".join([str(y) for y in x]) for x in commits])
    S = "commit_SHA,new_file path,new_file_MCC\n" + S
    f.write(S)
    f.close()
