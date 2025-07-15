import pandas as pd
from pydriller import Repository
import os
import matplotlib.pyplot as plt
#from staticfg import CFGBuilder #This is whate p2cfg takes most of its code from
from py2cfg import CFGBuilder
import ast,re,traceback
def render_as_CFG(code_file="trial.py",graph_file="trial"):
    f = open(code_file,'r')
    src = f.read()
    f.close()
    AST = ast.parse(src)
    builder = CFGBuilder()
    C = builder.build(graph_file,AST)
    g = C._build_visual()
    g.node_attr["width"] = "4"
    g.node_attr["height"] = "4"
    g.node_attr["fontsize"] = "0.1"
    g.graph_attr["dpi"] = "50"
    g.graph_attr["ranksep"] = "0.76"
    g.graph_attr["ratio"] = "compress"
    g.render(graph_file,view=False,format='jpeg')
top = "STTLab4/cs202_miner/Flask_results/helpers.py.changes"
changes = pd.read_csv(top)
y = changes["new_file_MCC"].values
n = len(y)
x = range(1,n+1)
plt.plot(x,y)
plt.title("Flask : `helpers.py` cylomatic complexity")
plt.xlabel("commit number")
plt.ylabel("cyclomatic complexity")
plt.xlim(1,n)
plt.savefig("STTLab4/cs202_miner/Flask_results/helpers.py.changes.png")
changes = changes.iloc[0:n:n//10]
Repo = Repository("https://github.com/pallets/flask",
only_no_merge=True,num_workers =1,histogram_diff = True,
only_commits = list(changes["commit_SHA"].values),)
folder = "STTLab4/cs202_miner/Flask_results/helpers.py.changes.cfgs"
try:os.mkdir(folder)
except:pass
i = 0
for commit in Repo.traverse_commits():
    C = [x for x in commit.modified_files if x.new_path == "flask/helpers.py"]
    if not C :
        print("no file found")
        continue
    C = C[0]
    C = C.source_code
    if C is None:
        print("src is None")
        continue
    filepath = folder + f"/commit{i}:{commit.hash}.py"
    graphpath = folder + f"/commit{i}:{commit.hash}"
    f = open(filepath,'w')
    f.write(C)
    f.close()
    try:
        render_as_CFG(filepath,graphpath)
        print(i,"done")
    except:print("skipped",i)
    i += n//10
