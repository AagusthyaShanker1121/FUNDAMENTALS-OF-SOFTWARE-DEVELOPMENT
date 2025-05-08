import pandas as pd
from pathlib import Path
# with open("FOSD\uniapp\data\startup_info.xlsx" , 'r') as f:
#     file_contents = f.read()

path = Path("FOSD")/"uniapp"/"data"/"startup_info.xlsx"
# file_contents = pd.read_excel("FOSD\\uniapp\\data\\startup_info.xlsx")
file_contents = pd.read_excel(path)
print(file_contents)
print(list(file_contents['Course']))
print(file_contents[['Admin', 'Admin_PW']].to_dict())

for a in file_contents[['Admin', 'Admin_PW']].itertuples():
    print(tuple(a[1:]))