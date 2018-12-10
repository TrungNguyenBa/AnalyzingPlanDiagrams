import json
import os
from utils import remove_item

folder_name = 'sql_query2_output_json'
output_folder_name = 'sql_query2_output_parsed_json'
if not os.path.isdir(output_folder_name):
    os.mkdir(output_folder_name)

for file_name in os.listdir(os.path.join(folder_name)):
    json_data=open(os.path.join(folder_name,file_name)).read()
    json_data = json_data.split()[3:-2]
    json_data = ''.join(json_data)
    json_data = json_data.replace('+','')
    data = json.loads(json_data)
    remove_item(data)

    with open(os.path.join(output_folder_name,file_name),'w') as outfile:
        json.dump(data, outfile)
