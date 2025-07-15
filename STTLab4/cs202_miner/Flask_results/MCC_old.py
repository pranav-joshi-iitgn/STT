import pandas as pd
pd.set_option("max_colwidth",10)
data = pd.read_csv("STTLab4/cs202_miner/Flask_results/commits_info_hist.csv")
old_id = data[["parent commit SHA","old_file path"]]
old_id.columns = ["commit SHA","new_file path"]
data.set_index(["commit SHA","new_file path"],inplace=True)
old_id = [tuple(x) for x in old_id.values]
ind= data.index
ind = set(ind)
Comp = data["new_file_MCC"]
val = [Comp[x].values[0] if x in ind else pd.NA for x in old_id]
data["old_file_MCC"] = val
data.to_csv("STTLab4/cs202_miner/Flask_results/commits_info_comp.csv")
data.dropna(subset=['new_file_MCC'],inplace=True)
print(len(data))
data.to_csv("STTLab4/cs202_miner/Flask_results/commits_info_comp_clean.csv")
print(data.head())