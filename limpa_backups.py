#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import datetime

folder_path = 'H:\Meu Drive\_DevBakcup2022' # caminho para a pasta 
file_extension = '.zip' # extensão do arquivo

most_recent_file = None
most_recent_timestamp = datetime.datetime.min

for file_name in os.listdir(folder_path):
    if file_name.endswith(file_extension):
        file_path = os.path.join(folder_path, file_name)
        timestamp = os.path.getmtime(file_path)
        timestamp = datetime.datetime.fromtimestamp(timestamp)
        if timestamp > most_recent_timestamp:
            most_recent_timestamp = timestamp
            most_recent_file = file_path

for file_name in os.listdir(folder_path):
    if file_name.endswith(file_extension):
        file_path = os.path.join(folder_path, file_name)
        if file_path != most_recent_file:
            os.remove(file_path)
            print(f'Arquivo {file_name} deletado com sucesso.')


# In[ ]:





# In[ ]:




