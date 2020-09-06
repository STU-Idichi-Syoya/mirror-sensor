import time
import busio
import board,cv2

import adafruit_amg88xx

# import matplotlib.pyplot as plt


# cv2.namedWindow('s', cv2.WINDOW_NORMAL)
# #cv2.resizeWindow("img_title",1280,720)
# cv2.setWindowProperty('s', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)



# I2Cバスの初期化
i2c_bus = busio.I2C(board.SCL, board.SDA)

# センサーの初期化
sensor = adafruit_amg88xx.AMG88XX(i2c_bus)

# センサーの初期化待ち
time.sleep(.1)

# # 8x8ピクセルの画像とbicubic補間をした画像を並べて表示させる
# #plt.subplots(figsize=(8, 4))
# import numpy as np
# mat=np.zeros((500,500,3),dtype="uint8")
# # ループ開始
# while True:
#     # データ取得
#     s= sensor.pixels

#     s=np.array(s,dtype="float16")
#     s=((s-25)/(37.5-25))*(250)
#     print(np.count_nonzero(s>250))
#     sn=s.astype("uint8")


#     sn=cv2.applyColorMap(sn,cv2.COLORMAP_HOT)
#     s=cv2.resize(sn,(500,500),cv2.INTER_CUBIC)

#     cv2.imshow("s",s)
#     cv2.waitKey(10)
import numpy as np
class sensor_amgx:
    def __init__(self) -> None:
        # I2Cバスの初期化
        i2c_bus = busio.I2C(board.SCL, board.SDA)

        # センサーの初期化
        self.sensor = adafruit_amg88xx.AMG88XX(i2c_bus)

        time.sleep(0.1)

    def get_tmp_8x8(self,caliblation=5.5)->np.array:
        arr=np.asfarray(self.sensor.pixels)+caliblation

        return arr

    def  get_resized_img(self,img):
        return cv2.resize(img,(256,256),cv2.INTER_CUBIC)

    def tmp_img_thermal(self,img:np.ndarray,MAX_TMP=37.5,MIN_TMP=35.0):
        img=self.get_tmp_8x8()
        img=cv2.resize(img,(500,500),cv2.INTER_CUBIC)

        img=((img-MIN_TMP)/(MAX_TMP-MIN_TMP))*(255)

        img[img>255]=255
        img[img<0]=0
        img=img.astype("uint8")
        img=cv2.applyColorMap(img,cv2.COLORMAP_HOT)

        
        return img
