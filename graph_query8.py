import os
import difflib
import matplotlib.pyplot as plt
import numpy as np
Z = np.zeros((101,101))



input_folder = 'sql_query8_output_parsed_json'
listdiff =[]
for i in range(101):
    for j in range(101):
        file_name = 'query8s{}_l{}.json'.format(i,j)
        json_file = open(os.path.join(input_folder,file_name),'r')
        for text in json_file:
            if not text in listdiff:
                Z[i,j]=len(listdiff)
                listdiff+=[text]
            else:
                Z[i,j]=listdiff.index(text)
        json_file.close()


plt.pcolor(Z)
plt.colorbar()
plt.show()
