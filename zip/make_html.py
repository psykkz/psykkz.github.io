import os

folder_path = os. getcwd()

for path, dirs, files in os.walk(folder_path):
    dossier=path.replace(folder_path,'')
    text='<!DOCTYPE html>'
    if len(dossier.split('\\'))>1:
        for filename in files:
            print(f"{dossier}\{filename}")
            text+=f'<a href="{filename}">{filename}</a></br>\n'
        fichier=open(path+'\index.html','w')
        fichier.write(text)
        fichier.close()