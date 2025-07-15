import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("STTLab3/cs202_miner/Flask_results/commits_info_full.csv")
file_names = data["new_file path"].values
file_extensions =[x.split(".")[-1] if isinstance(x,str) else None for x in file_names]
Matches = data["Matches"].values
Ext ={
'json':"data",
'yaml':"data",
'yml':"data",
'png':"data",
'rst':"doc",
'md':"doc",
'txt':"doc",
'editorconfig':"config",
'ini':"config",
'in':"config",
'toml':"config",
'gitignore':"config",
'py':"code",
'sh':"code",
'cfg':"code",
'html':"code",
'flake8':"code",
}
matches = {Type:0 for Type in list(Ext.keys())+["data","config","doc","non-code","code","full"]}
mismatches = {Type:0 for Type in list(Ext.keys())+["data","config","doc","non-code","code","full"]}
for i,m in enumerate(Matches):
    ext = file_extensions[i]
    if ext is None:continue
    if m:
        matches[ext] += 1
        matches[Ext[ext]] += 1
        matches["full"] +=1
        if ext != "code":matches["non-code"] += 1
    else:
        mismatches[ext] += 1
        mismatches[Ext[ext]] += 1
        mismatches["full"] += 1
        if ext != "code":mismatches["non-code"] += 1
T = []
for Type in matches:
    eq = matches[Type]
    neq = mismatches[Type]
    T.append([Type,eq,neq,100*neq/(eq + neq)])
T = pd.DataFrame(T,columns = ["type","matches",'mis-matches',"% mis-match"])
print(T)
plt.bar(T["type"],T["% mis-match"],color = ["green"]*(len(matches)-6) + ["blue"]*3 + ["red"]*2 + ["black"])
plt.xlabel("file type")
plt.xticks(T.index,labels = [" "*(30-len(str(x))) + str(x) for x in T["type"].values],rotation=90,fontsize=6)
plt.ylabel("% mis-match")
plt.savefig("STTLab3/cs202_miner/Flask_results/mismatch_percentage.png",format='png')
plt.pie(list(mismatches.values())[:-4],labels=list(mismatches.keys())[:-4],labeldistance=0.7,textprops={'fontsize': 6})
plt.savefig("STTLab3/cs202_miner/Flask_results/pie.svg",format='svg')