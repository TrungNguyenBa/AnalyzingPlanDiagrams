import os

path = os.getcwd()

folder_name = 'sql_query8_output_json'
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)

with open('process_sql_query8_command.sh','w') as file:
    file.write('#!/bin/bash\n')
    for i in range(101):
        for j in range(101):
            file.write('psql -h localhost -d tpch_sf1 -U trung -p 5432 -a -q -f {}/sql_query8/query8s{}_l{}.sql -o {}/sql_query8_output_json/query8s{}_l{}.json\n'.format(path,i,j,path,i,j))

folder_name = 'sql_query2_output_json'
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)

with open('process_sql_query2_command.sh','w') as file:
    file.write('#!/bin/bash\n')
    for i in range(101):
        for j in range(101):
            file.write('psql -h localhost -d tpch_sf1 -U trung -p 5432 -a -q -f {}/sql_query2/query2p{}_ps{}.sql -o {}/sql_query2_output_json/query2p{}_ps{}.json\n'.format(path,i,j,path,i,j))
