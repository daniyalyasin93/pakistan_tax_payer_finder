import pandas as pd
import numpy as np
import getopt, sys


opts, args = getopt.getopt(
    sys.argv[1:],
    'hn:f:',
    ['help', 'names', 'file'],
)
names=[]
local_paths =  []
file = None
for opt, arg in opts:
    if opt in ('-n', '--names'):
        names.append(arg.upper())
        #print(opt + ': ' + arg)
    if opt in ('-f', '--file'):
        file=arg
        #print(opt + ': ' + arg)
    if opt in ('-h', '--help'):
        print ("Usage: -f<Path To xlsx file> -n<Search strings> -n<Search strings>")

if (len(names) == 0 or file is None):
    exit()

print('names: ' + str(names))
print('file: ' + str(file))


def search_taxpayer(df_dict, names):
     results = []
     for part in df_dict.keys():
            masks = (df_dict[part]['NAME'].str.contains(stringtosearch, regex=False).fillna(False) for stringtosearch in names)
            combined_mask = np.vstack(masks).all(axis=0)
            results.append(df_dict[part][combined_mask])
     return results


df = pd.read_excel(file, engine='openpyxl', sheet_name=None)

print(search_taxpayer(df, names));