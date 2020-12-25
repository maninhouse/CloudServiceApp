import requests

def notify(msg, image_url):
    url = ('https://maker.ifttt.com/trigger/Warning/with/'+'key/cEQpmS1N785KvCnzcnxwNQ' 
    +'?value1='+str(msg)+'&value3=' + str(image_url))
    r = requests.get(url)      
    if r.text[:5] == 'Congr':  
        print('成功推送 (' +str(msg)+') 至 Line')
    return r.text

    