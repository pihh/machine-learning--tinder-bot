import json
import pynder
import urllib.request
from .facebook_token import FacebookSession

fbSession = FacebookSession()

class TinderSession(object):
  loc=[38.679, -9.1569]
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TinderSession, cls).__new__(cls)
      cls.instance.myLocation()
      cls.instance.load()
    return cls.instance
  
  #def __init__(self):

    #self.myLocation()
    #self.load()

  def myLocation(self):
    url="http://ipinfo.io/json"
    response= urllib.request.urlopen(url)
    data = json.load(response)

    
    self.loc = data['loc'].split(',')
    self.loc[0] = float(self.loc[0])
    self.loc[1] = float(self.loc[1])
    print(self.loc,'loc')

  def load(self):

    XAuthToken = fbSession.xauth
    
    session = pynder.Session(594665617, XAuthToken=XAuthToken)
    #session.update_location(self.loc[0],self.loc[1])
    #38.679, -9.1569
    session.update_location(55.671865, 12.483533)
    self.session = session
    print(session)
    print('will get neaby_users')
    users = session.nearby_users()
    print('did get nearby_users')
    print(users)
    """
    for user in users:
        print("user")
        print(user)
        photos = []
        photos = user.get_photos()
        cnt = 0
        for photo in photos:
            image_name = "data/downloads/" + user.name + "_" + str(cnt) + "_" + str(user.age) + "_" + user.id + ".jpg"
            urllib.request.urlretrieve(photo, image_name)
            cnt += 1
            print(image_name)
    """
    self.users = users
"""
singleton = TinderSession()
new_singleton = TinderSession()
 
print(singleton is new_singleton)
 
singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)
"""


