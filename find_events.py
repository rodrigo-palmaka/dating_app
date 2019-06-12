import json
import requests

baseUrl = 'http://api.eventful.com/json/'
apiToken = 'QbrjjMLKRc8Dj4tS'
# params = {}

def getEvent(cityName, date):
    s = datetime.strftime(date, '%Y%m%d')
    prms = {'authentication':'QbrjjMLKRc8Dj4tS', 'location': cityName, 'date':s+'00'+'-'+s+'00'}

    r = requests.get(url = baseUrl + "events",  params = prms)
# if r.status_code == 200:
