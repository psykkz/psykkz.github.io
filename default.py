import xbmcgui, xbmcaddon, xbmcvfs
import requests, os

__scriptid__ = "script.psykkbkp"
addon = xbmcaddon.Addon(id=__scriptid__)

headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
         'accept-encoding': 'gzip, deflate, br',
         'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
         'cache-control': 'max-age=0',
         'dnt': '1',
         'if-none-match': 'W/"63e037ca-a05"',
         'referer': 'https://psykkz.github.io/zip/save_kod/',
         'sec-ch-ua': '"Chromium";v="108", "Opera";v="94", "Not)A;Brand";v="99"',
         'sec-ch-ua-mobile': '?0',
         'sec-ch-ua-platform': '"Windows"',
         'sec-fetch-dest': 'document',
         'sec-fetch-mode': 'navigate',
         'sec-fetch-site': 'same-origin',
         'sec-fetch-user': '?1',
         'upgrade-insecure-requests': '1',
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0'
    }

url='https://psykkz.github.io/zip/save_kod/'
url_abs='https://github.com/psykkz/psykkz.github.io/raw/main/zip/save_kod/'
r = requests.get(url, allow_redirects=True)
dossiers=r.text.split('a href="')
rep=[]
for dossier in dossiers:
    #print(dossier)
    if '">/' in dossier:
        d=dossier.split('">/')[1]
        #print(d)
        if '/'in d:
            rep.append(d.split('/')[0])
            
#Installation des fichiers dans les differents dossiers
for dossier in rep:
    chemin=xbmcvfs.translatePath('special://userdata'+f'/addon_data/{dossier}')
    if not(os.path.exists(chemin)):
        os.mkdir(chemin)
    xbmc.executebuiltin(f'Notification(BackuPsykk-{dossier}, Cette operation peut durer un certain temps suivant la vitesse de votre connexion, merci de patienter,10000,'')')
    #xbmcgui.Dialog().ok(f'{dossier}', 'Attendez le message final installation reussie pour lancer une extension')
    recup_fichier=url+f'{dossier}/index.html'
    r = requests.get(recup_fichier, allow_redirects=True)
    contenu=(r.content)
    contenu=str(contenu).split('a href="')[1:]
    pDialog=xbmcgui.DialogProgress()
    pDialog.create('Installation PsykkBackup', dossier)
    k=0
    for fichier in contenu:
        pDialog.update(round(int(100*k/len(contenu)),0), 'Installation en cours... Merci de patienter ...')
        adresse_fichier=f"""{url_abs}/{dossier}/{fichier.split('"')[0]}"""
        #xbmc.executebuiltin(f'Notification({dossier}, {adresse_fichier},10000,'')')
        chemin_complet=xbmcvfs.validatePath(chemin+'/'+fichier.split('"')[0])
        xbmc.executebuiltin(f'Notification({dossier},{chemin_complet},10000,'')')
        r = requests.get(adresse_fichier, allow_redirects=True, headers=headers)
        
        open(chemin_complet, 'wb').write(r.content)
        k+=1
        
    pDialog.close()
    #xbmcgui.Dialog().ok(f'{dossier} - Installation OK', 'Fait')
 
xbmcgui.Dialog().ok('Installation Finie', 'En esperant que tout se soit bien passe')
