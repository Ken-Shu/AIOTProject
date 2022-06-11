import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#抓取認證碼
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://d1mini-console-default-rtdb.firebaseio.com/'
})

temp = db.reference('/temp').get()
print('temp:', temp)


def listener_temp(event):
    print("temp:", event.data)


def listener_temphic(event):
    print("temp hic:", event.data)


def listener_humi(event):
    print("humi:", event.data)

if __name__=='__main__':
    # listener
    firebase_admin.db.reference("/temp").listen(listener_temp)
    firebase_admin.db.reference("/temp_hic").listen(listener_temphic)
    firebase_admin.db.reference("/humi").listen(listener_humi)