import pandas as pd

df = pd.read_csv("areas.csv",sep=";")

i = 2
for index, row in df.iterrows():
  filename = "%02d-%s.Rmd" %(i,row["key"])
  text = "# %s {#%s}" %(row["Name"],row["key"])

  with open(filename, mode = "w", encoding='utf8') as f:
    f.write(text)
  i = i+1

