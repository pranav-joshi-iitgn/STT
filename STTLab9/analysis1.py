import json
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
with open('/home/hp/STT/STTLab9/pandas_deps.json', 'r') as file:data = json.load(file)

print("Making Graph")
A = {x:data[x].get("imports",[]) for x in data} # Adjacency matrix
G = nx.DiGraph(A)
l = len(A)
print(l,"modules found")

print("Making DataFrame")
L = []
cols = ['name', 'fan-in', 'fan-out', 'bacon']
for x in data:
    y = data[x]
    z = [y['name'],len(y.get('imported_by', [])),len(y.get('imports', [])),y.get('bacon', 0)]
    L.append(z)
df = pd.DataFrame(L, columns=cols).dropna()

print("importance of a module")
ranks = nx.pagerank(G)
df["rank"] = [ranks[x] for x in df["name"].values]

print("instability")
df["instability"] = df["fan-out"]/(df["fan-out"] + df["fan-in"])
df.sort_values(by='instability', ascending=False, inplace=True)

print("saving")
df.to_csv('pandas_deps.csv', index=False)

print("Computing Cycles")
C = nx.simple_cycles(G)
C = [c for c in C if len(c) > 1] # list of all simple cycles
C = sorted(C,key=lambda c:len(c))
f = open("pandas_deps_cycles.txt",'w')
f.write("\n".join([" --> ".join(c) for c in C]))
f.close()

print("Unused or less used modules")
df.loc[(df["fan-in"]<=1).values].to_csv("pandas_deps_unused.csv", index=False)

print("calculating transition matrix")
modules = [x for x in A]
module_num = {x:i for i,x in enumerate(modules)}
p = 0.5/(1+df["fan-in"].max())
print("p is",p)
P = [[0]*l for i in range(l)]
print("memory assigned")
for x in A:
    for y in A[x]:
        P[module_num[x]][module_num[y]] = p
P = np.array(P)
print("P calculated")
X = np.identity(l) - P
print("X calculated. Shape:",X.shape)
d = np.linalg.det(X)
print("det(X) =",d)
if d !=0 : 
    Xinv = np.linalg.inv(X)
    effect = Xinv.T
else:
    XTX = X.T @ X
    print("XTX calculated. Shape:",XTX.shape)
    XTXinv = np.linalg.inv(XTX)
    print("XTXinv calculated. Shape:",XTXinv.shape)
    XTXinvXT = XTXinv @ X.T
    effect = XTXinvXT.T
effect = effect - np.identity(l)
print("effect calculated. Shape:",effect.shape)
L = [["modules"] + modules]
for i in range(l):
    L.append(
        [modules[i]] + 
        [str(x) for x in effect[i]]
        )

L = [",".join(row) for row in L]
L = "\n".join(L)
f = open('pandas_deps_effect.csv','w')
f.write(L)
f.close()

plt.imshow(effect,cmap="Grays")
plt.xticks(range(l),modules,rotation=90,size=6)
plt.yticks(range(l),modules,size=6)
plt.tight_layout()
plt.savefig("pandas_deps_effect.png",format="png")
plt.close()

print("getting ordering")
ordering = {}
for i in range(l):
    effects = effect[i]
    ind = sorted(list(range(l)),key= lambda j : effects[j],reverse=True)
    victims = [modules[j] for j in ind]
    ordering[modules[i]] = victims
total = [sum(row) for row in effect]
ord_tot = sorted(list(range(l)),key=lambda i:total[i],reverse=True)
ord_tot = [modules[i] for i in ord_tot]
ordering = {x:ordering[x] for x in ord_tot}

print("writing JSON string")
L = []
for x in ordering:L.append(repr(x) + " : " + repr(ordering[x]))
L = ",\n".join(L)
L = "{\n" + L + "\n}"
L = L.replace("'","\"")
f = open("pandas_deps_effect.json",'w')
f.write(L)
f.close()

print("condensation")
plt.figure()
H = nx.condensation(G)
nx.draw(H,with_labels=True)
plt.savefig("pandas_deps_cond.png",format="png")
plt.close()
f = open("pandas_deps_cond.json",'w')
groups = H.nodes.data()
L={x[0]:list(x[1]["members"]) for x in groups}
f.write(json.dumps(L,indent=4))
f.close()