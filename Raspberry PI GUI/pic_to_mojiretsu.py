import io
from PIL import Image

def img_to_binary(image_str):
#バイナリにしたい画像を読み込み
    tmpimg = Image.open(str(image_str))
    with io.BytesIO() as output:
        tmpimg.save(output,format="PNG")
        contents = output.getvalue()#バイナリ取得
        # print(contents)#表示
        return contents
        # tmpimg2 = Image.open(io.BytesIO(contents))#バイナリから画像に変換
        # tmpimg2.save('image_from_str.png')


def binary_to_img(image_binary):
    #バイナリ文字列としてやる場合はこんな感じ
    imgbytes_str = image_binary
    img_from_str = Image.open(io.BytesIO(imgbytes_str))
    img_from_str.save('image_from_str2.png')

# bin_string = img_to_binary("I-POST_icon.png")
# binary_to_img(bin_string)