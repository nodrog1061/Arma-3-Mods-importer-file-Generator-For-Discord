import requests
import json
import html
from decouple import config

def getColection(colectionId = config('DEFAULT-COLLECTION-ID')):

    colectionUrl = 'https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/'
    itemUrl = 'https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/?'

    colectionVars = {'collectioncount': '1', 'publishedfileids[0]': [str(colectionId)]}
    colection = requests.post(colectionUrl, data = colectionVars)
    colectionResponce = json.loads(colection.text)

    colectionIds = colectionResponce['response']['collectiondetails'][0]['children']
    colectionCount = len(colectionIds)
    colectionIdsExtracted = {'itemcount': str(colectionCount)}

    for x in range(colectionCount):
        colectionIdsExtracted['publishedfileids['+str(x)+']'] = colectionIds[x]["publishedfileid"].split()

    items = requests.post(itemUrl, data = colectionIdsExtracted)
    itemsResponce = json.loads(items.text)
    itemsIds = itemsResponce['response']['publishedfiledetails']
    itemIdsExtracted={'itemcount': str(colectionCount)}
    # itemIdsExtracted={}

    for x in range(colectionCount):
        try:
            itemIdsExtracted[html.escape(itemsIds[x]["title"])] = 'http://steamcommunity.com/sharedfiles/filedetails/?id='+str(itemsIds[x]["publishedfileid"])
        except:
            itemIdsExtracted["TFM Addons"] = 'http://steamcommunity.com/sharedfiles/filedetails/?id=1561414049'
    
    return(itemIdsExtracted)
