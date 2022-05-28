import requests

token = ""
line_url = "https://notify-api.line.me/api/notify"


def sendMessage(msg):
    header = {
        "Authorization": "Bearer " + token
    }
    payload = {"message": msg}
    r = requests.post(line_url, headers=header, params=payload)
    return r.status_code

def sendMessageAndImageFile(msg, imageURL):
    header = {
        "Authorization": "Bearer " + token
    }
    payload = {"message": msg}
    file = {'imageFile': open(imageURL, 'rb')}
    r = requests.post(line_url, headers=header, params=payload, files=file)
    return r.status_code


if __name__ == '__main__':
    # code = sendMessage('Hello 哈囉!')
    code = sendMessageAndImageFile('Hello 哈囉!', 'door_open.jpg')
    print('回應碼 :', code)
