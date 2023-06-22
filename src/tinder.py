import json
import urllib
import requests
from .environment import ENVIRONMENT
from .facebook_token import FacebookSession

fbSession = FacebookSession()

class TinderApi:
    HEADERS = {
        "content-type": "application/json",
        "Accept": "application/json"
    }
    VERBOSE = False
    loc = [0,0]


    def __init__(self, verbose = False):
        self.VERBOSE = verbose
        self.__load()

    def __load(self):
        self.__login(fbSession.long_token)
        self.__update_my_location()
    
    def __log(self,message):
        if(self.VERBOSE):
            print(message)

    def __find_my_location(self):
        url="http://ipinfo.io/json"
        response= urllib.request.urlopen(url)
        data = json.load(response)

        self.loc = data['loc'].split(',')
        self.loc[0] = float(self.loc[0])
        self.loc[1] = float(self.loc[1])
        
        self.__log('My coordinates: {}'.format(self.loc))

    def __update_my_location(self):
        self.__find_my_location()
        print('')

    def __login(self, token=ENVIRONMENT['FACEBOOK_LONG_TOKEN']):
        data = {"token":token, "facebook_id": ENVIRONMENT['FACEBOOK_ID']}
        url ="https://api.gotinder.com/v2/auth/login/facebook"
        request = requests.post(url, headers=self.HEADERS, json=data)
        response = request.json()
       
        self.token = response['data']['api_token']
        self.HEADERS['X-Auth-Token'] = self.token

        self.__log('Login response: {}'.format(response))

    def get_users(self):
        url ="https://api.gotinder.com/v2/recs/core?locale=en"
        request = requests.get(url, headers=self.HEADERS)
        response = request.json()
        return response
    
    def get_photos(self):
        photos = []
        users = self.get_users()
        for user in users['data']['results']:
            if user['type']=="user":
                for photo in user['user']['photos']:
                    try:
                        photo_url = photo['processedFiles'][0]['url']
                        photos.append(photo_url)
                        urllib.request.urlretrieve(photo['processedFiles'][0]['url'],'./data/unclassified/'+user['user']['_id']+'__'+photo['id']+'.jpg' )     
                    except:
                        print('failed to fetch photo')
        
        return photos

