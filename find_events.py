import json
import requests
from datetime import datetime

baseUrl = 'http://api.eventful.com/json/'
apiToken = 'QbrjjMLKRc8Dj4tS'
# params = {}

def getEvent(cityName, date):
    o = open('test_ev_list.txt', 'w+')


    datee = datetime.strptime(date, '%b %d, %Y')
    s = datetime.strftime(datee, '%Y%m%d')
    prms = {'app_key':'QbrjjMLKRc8Dj4tS', 'l': cityName, 't':s+'00'+'-'+s+'00', 'c':'music'}
    # prms = {'app_key':'QbrjjMLKRc8Dj4tS'}
    # r = requests.get(url = baseUrl + "categories/list",  params = prms)

    r = requests.get(url = baseUrl + "events/search",  params = prms)
    data = r.json()
    # print(data['events']['event'][0])
    a = data['events']['event']
    # print(a)
    evList = []
    evDict = {}
    for i in a:
        name = i['title']
        evList.append(name)
        date = datetime.strptime(i['start_time'], '%Y-%m-%d %H:%M:%S')
        date = date.strftime("%#I %p")
        evDict[name] = {'url': i['url'], 'venue' : i['venue_name'], 'start': date,
            'stop': i['stop_time']}
    return evList, evDict

    # for i in data['events']:
    #     print(i['event'])
        # o.write(i['event'] +', ')
    # for i in data['category']:
        # o.write(str(i['name']).replace('amp;', '') + ', ')
# if r.status_code == 200:
