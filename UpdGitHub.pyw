import os
import sys
import subprocess
import urllib.request 
import requests
import zipfile
import shutil
    


url = 'https://github.com/PixlGalaxy/DurazznoMini/archive/refs/heads/main.zip'
r = requests.get(url, allow_redirects=True)
open('DurazznoMini-main.zip', 'wb').write(r.content)


with zipfile.ZipFile("DurazznoMini-main.zip", 'r') as zip_ref:
    zip_ref.extractall("")

import shutil
import os 



src = "C:/Galaxy_Apps/DurazznoMini/DurazznoMini-main"

dest = "C:/Galaxy_Apps/DurazznoMini"

src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)

os.startfile("DMSCU.pyw")
