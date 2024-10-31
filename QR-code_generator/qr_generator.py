'''
import pyqrcode
import pypng

print("1.URLを入力してください")
URL = str(input())
print("2.任意のファイル名を入力してください\npngファイルが出力されます")
filename = str(input())
FILE_PNG_A = filename + ".png"

# QRコードの作成
code = pyqrcode.create(URL, error='L', version=5, mode='binary')
code.png(FILE_PNG_A, scale=5, module_color=[0, 0, 0, 128], background=[255, 255, 255])

'''
from PIL import Image, ImageDraw
import qrcode
import os
import datetime


def generate_qr_code(url, filename, folder_name):
    # QRコードのインスタンスを生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # QRコードを画像として生成
    img = qr.make_image(fill_color="black", back_color="white")

    # 画像を保存
    img.save(folder_name + '/' + filename)

if __name__ == "__main__":
    print("1.URLを入力してください。(入力したらEnter)")
    url_to_encode = str(input())
    print("2.任意のファイル名を入力してください\npngファイルが出力されます。(入力したらEnter)")
    filename = str(input()) + ".png"
    print("3.保存先を指定してください。(入力したらEnter)\n※指定しない場合(未入力の場合)は実行ファイルと同じ階層に生成されます。")
    print("※絶対パスで入力してください。")
    h_path = str(input())
    h_foldername = "新規QRコード"

    # 出力フォルダ作成(フォルダ名:頭文字＿年月日時分)
    folder_name = h_foldername + "_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
    path = h_path + folder_name
    os.makedirs(path, exist_ok=True)
    generate_qr_code(url_to_encode, filename, folder_name)