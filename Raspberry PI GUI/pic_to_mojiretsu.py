import io
from PIL import Image
import base64

def img_to_binary(image_str):
    with open(image_str, 'rb') as image_file:# PNGファイルをバイナリモードで読み込む
        image_data = image_file.read()
        contents = base64.b64encode(image_data) # Base64エンコード
        #print(contents)#表示
        return contents


def binary_to_img(image_binary):
    #バイナリ文字列としてやる場合はこんな感じ
    imgbytes_str = image_binary
    img_from_str = Image.open(io.BytesIO(imgbytes_str))
    img_from_str.save('image_from_str2.png')

# bin_string = img_to_binary("I-POST_icon.png")
# binary_to_img(bin_string)
