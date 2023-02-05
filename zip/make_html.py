import os

folder_path = os. getcwd()
url="https://github.com/psykkz/psykkz.github.io/raw/main/zip"
#url="https://github.com/psykkz/psykkz.github.io/raw/main/zip/save_kod/plugin.video.vstream/iptv.db
#plugin.video.sendtokodiU2P/iptv.db"
for path, dirs, files in os.walk(folder_path):
    print(dirs)
    dossier=path.replace(folder_path,'')
    text='<!DOCTYPE html>'
    if len(dirs)>0:
        for dir in dirs:
            text+=f'<a href="{dir}">/{dir}/</a></br>\n'
    if len(dossier.split('\\'))>1:
        for filename in files:
            #print(f"{dossier}\{filename}")
            text+=f'<a href="{filename}">{filename}</a></br>\n'
        fichier=open(path+'\index.html','w')
        fichier.write(text)
        fichier.close()