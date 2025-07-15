import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os,ast

def findfile(typename):
    pack = typename + ".java"
    os.system("find tablesaw -name " + pack + "> temp")
    f = open("temp",'r')
    s =f.read().strip()
    if "test" in s : s = ""
    f.close()
    return s.strip()

def getsource(file):
    os.system("cat " + file + "> temp")
    f =open("temp",'r')
    s = f.read()
    f.close()
    s = s.split("\n")
    s = [x for x in s if x.strip() and x.strip()[:6] != "import"]
    s = "\n".join(s)
    s = repr(s)
    return s

# Clean and find file names
df = pd.read_csv("TypeMetrics.csv")
df.drop("Project Name",axis=1,inplace=True)
TypeNames = df["Type Name"].values
Files = [repr(findfile(x)) for x in TypeNames]
df["file"] = Files
df.sort_values("YALCOM",inplace=True,ascending=False)
df = df.where(df["file"]!="''")
df = df.where(df["YALCOM"]>-0.5)
df.dropna(inplace=True)
df.to_csv("TypeMetricsClean.csv",index=False)
top5 = df.head().copy()

# write Top5.csv
files = top5["file"].values
codes = [getsource(file) for file in files]
top5["JAVA code"] = codes
req = ["Type Name","Package Name","JAVA code","LCOM1","LCOM2","LCOM3","LCOM4","LCOM5","YALCOM"]
top5 = top5.loc[:,req]
top5.to_csv("Top5.csv",index=False)

# Make html tables
head = "\n".join(["<tr>","\n".join(["<td>" + x + "</td>" for x in req[2:]]),"</tr>"])
L = ["<table>",head]
for row in top5.values:
    toadd = [
        f"<td>\nclass:{row[0]}<br>\npackage:{row[1]}<pre><small>\n" + 
        ast.literal_eval(row[2]).replace("<","&lt;").replace(">","&gt;") + 
        "\n</small></pre></td>"
    ] + [f"<td>{x}</td>" for x in row[3:]]
    toadd = ["<tr>"] + toadd + ["</tr>"]
    toadd = "\n".join(toadd)
    L.append(toadd)
L.append("</table>")
L = "\n".join(L)
f = open("Top5.html",'w')
f.write(L)
f.close()