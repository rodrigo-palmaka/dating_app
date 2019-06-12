import json
import requests
from datetime import datetime

baseUrl = 'http://api.eventful.com/json/'
apiToken = 'QbrjjMLKRc8Dj4tS'
# params = {}

def getEvent(cityName, date):
    datee = datetime.strptime(date, '%b %d, %Y')
    s = datetime.strftime(datee, '%Y%m%d')
    prms = {'authentication':'QbrjjMLKRc8Dj4tS', 'location': cityName, 'date':s+'00'+'-'+s+'00'}

    r = requests.get(url = baseUrl + "events",  params = prms)
    data = r.json()
    print(data)
# if r.status_code == 200:
