import os
import time
import json
localfile = open('./config.json')
data = json.load(localfile)
fileLoc = data["diretorioINPUT"]
tmp_list = []
def open_file(fileLocation: str):
    return os.listdir(fileLocation)
def start():
    while True:
        files = open_file(fileLoc)
        for f in files:
            File = open(fileLoc+f, 'r')
            for line in File:
                if "Press: KHome" in line:
                    if line not in tmp_list:
                        print(f'\n{f} : {line}')
                        tmp_list.append(line)
                elif "Press: KInsert" in line:
                    if line not in tmp_list:
                        print(f'\n{f} : {line}')
                        tmp_list.append(line)
            time.sleep(0.1)
    
            

        