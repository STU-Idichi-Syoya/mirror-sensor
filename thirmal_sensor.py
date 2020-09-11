import time
import busio
import board,cv2

import adafruit_amg88xx


# I2Cバスの初期化
i2c_bus = busio.I2C(board.SCL, board.SDA)

# センサーの初期化
sensor = adafruit_amg88xx.AMG88XX(i2c_bus)

# センサーの初期化待ち
time.sleep(.1)


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

## we don't use opencv 
#     def tmp_img_thermal(self,img:np.ndarray,MAX_TMP=37.5,MIN_TMP=35.0):
#         img=self.get_tmp_8x8()
#         img=cv2.resize(img,(500,500),cv2.INTER_CUBIC)

#         img=((img-MIN_TMP)/(MAX_TMP-MIN_TMP))*(255)

#         img[img>255]=255
#         img[img<0]=0
#         img=img.astype("uint8")
#         img=cv2.applyColorMap(img,cv2.COLORMAP_HOT)

        
        return img
if __name__ =="__main__" :
    while True:
        print(sensor_amgx().get_tmp_8x8().max())

