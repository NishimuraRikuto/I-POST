import json
import requests
from pic_to_mojiretsu import img_to_binary
from picture_minimizer import compress
import re

I_POST_SERVER = "https://ipost-server-eh2trxntfa-an.a.run.app/"

def get_message():
    r1 = requests.get(I_POST_SERVER + "/machine/messages/" + "all")
    r1 = r1.json()
    filename = 'inbox.json'  # use the file extension .json
    with open(filename, 'w') as file_object:
        json.dump(r1, file_object)  # json.dump() function to store
    with open(filename, 'r') as file_object:
        data = json.load(file_object)
        return data

def send_message(send_name):
    # Send ボタン押されたら
    #"I_POST-icon"　の代わりに撮った手紙の画像を入れる
    compress("I-POST_icon.PNG")
    compressed_img = "image-file-compressed.PNG"
    msg = img_to_binary(compressed_img)
    input_string = str(msg)
    pattern = r"b'([A-Za-z0-9+/=]+)'"# 正規表現パターン
    matches = re.findall(pattern, input_string)#マッチした部分の文字列をリストで取得
    mess = matches[0]
    payload = {'imageUrl': mess, "senderId": "222", "senderName": send_name}
    r = requests.post(I_POST_SERVER + "/machine/messages", data=payload)
    return "Sent"
