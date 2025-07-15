import sys,csv,os
from pydriller import Repository
columns = ["old_file path","new_file path","commit SHA","parent commit SHA","commit message"]
if sys.argv[3]=="hist":hist = True
elif sys.argv[3]=="myers":hist = False
else:raise ValueError("Give proper arguments")
columns.append(f"diff_{sys.argv[3]}")
columns.extend(["new_file_MCC"])
rows = []
count=0
last_n=3000
commits = []
Repo = Repository(sys.argv[1],only_no_merge=True,order='reverse',num_workers =1,histogram_diff = hist,skip_whitespaces=True)
for x in Repo.traverse_commits():
  if (x.in_main_branch==True):
    count=count+1
    commits.append(x)
    if count == last_n:break
in_order = []
for value in range(len(commits)):in_order.append(commits.pop())
commits=in_order
for i,commit in enumerate(commits):
  print('[{}/{}] Mining commit {}.{}'.format(i+1,len(commits),sys.argv[1],commit.hash))
  diff = []
  try:
    for m in commit.modified_files:
      if len(commit.parents) > 1:continue
      row = [m.old_path,m.new_path,commit.hash,commit.parents[0],repr(commit.msg),repr(m.diff),m.complexity]
      rows.append(row)
  except:pass
try:os.mkdir(sys.argv[2]+'_results')
except:pass
f = open(sys.argv[2]+'_results/commits_info_'+sys.argv[3]+'.csv', 'w')
f.write("")
f.close()
with open(sys.argv[2]+'_results/commits_info_'+sys.argv[3]+'.csv', 'a') as csvFile:
  writer = csv.writer(csvFile)
  writer.writerow(columns)
  writer.writerows(rows)
