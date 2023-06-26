!pip install pandas gitpython
!pip install pandas as ps

import os
import json
import pandas as pd
import git
import glob
git.Repo.clone_from("https://github.com/phonepe/pulse.git", "/content/pulse")

def process_json_files(root_dir):
    data_list=[] #initialize an empty list to store processed data

    #Use glob to find all JSON files within the root directory and its subdirectories
    json_files= glob.glob(os.path.join(root_dir, '**/*.json'), recursive=True)

    #iterate over the JSON files
    for json_file in json_files:

        with open(json_file) as f:
            data =json.load(f)
        # Extract relevant information from the data and append it to the data_list
            for item in data['data']:
                state_dir= os.path.basename(os.path.dirname(os.path.dirname(json_file)))
                year_dir =os.path.basename(os.path.dirname(json_file))
                quarter= int(os.path.splitext(os.path.basename(json_file))[0])
                row_dict={
                    'State': state_dir,
                    'Year': year_dir,
                    'Quarter': quarter,
                    'Data': item
                }
                data_list.append(row_dict)

    df = pd.DataFrame(data_list) 
    return df  




r1 ='/content/pulse/data/aggregated/transaction/country/india/state'
r2= '/content/pulse/data/aggregated/user/country/india/state'
r3= '/content/pulse/data/map/transaction/hover/country/india/state'
r4 ='/content/pulse/data/map/user/hover/country/india/state'
r5 ='/content/pulse/data/top/transaction/country/india/state'
r6 ='/content/pulse/data/top/user/country/india/state'

df1 =process_json_files(r1)
df2 =process_json_files(r2)
df3 =process_json_files(r3)
df4 =process_json_files(r4)
df5 =process_json_files(r5)
df6= process_json_files(r6)

df1.drop_duplicates().to_csv('agg_trans.csv',index=False)
df2.drop_duplicates().to_csv('agg_user.csv',index=False)
df3.drop_duplicates().to_csv('map_tran.csv', index=False)
df4.drop_duplicates().to_csv('map_user.csv',index=False)
df5.drop_duplicates().to_csv('top_tran.csv',index=False)
df6.drop_duplicates().to_csv('top_user.csv',index=False)
