import pynder
import urllib.request
from .facebook_token import FacebookSession

fbSession = FacebookSession()

def main():
    XAuthToken = fbSession.xauth
    session = pynder.Session(XAuthToken=XAuthToken)
    session.update_location(55.671865, 12.483533)

    users = session.nearby_users()
    for user in users:
        photos: []
        photos = user.get_photos()
        cnt = 0
        for photo in photos:
            image_name = "data/downloads/" + user.name + "_" + str(cnt) + "_" + str(user.age) + "_" + user.id + ".jpg"
            urllib.request.urlretrieve(photo, image_name)
            cnt += 1
            print(image_name)


if __name__ == "__main__":
    main()