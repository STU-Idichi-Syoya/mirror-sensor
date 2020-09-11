import smbus
import time
 
i2c = smbus.SMBus(1)
address = 0x5c


dur_temp_sensor=0.5

stime=time.time()

btemp=15

# センサsleep解除
def get_tmp():
    global stime
    global btemp
    
    slptime=time.time()-stime


    if slptime<dur_temp_sensor:
        return btemp
    
    stime=time.time()
    try:
        i2c.write_i2c_block_data(address,0x00,[])
    
      # 読み取り命令
      time.sleep(0.003)
      i2c.write_i2c_block_data(address,0x03,[0x00,0x04])

      # データ受取
      time.sleep(0.015)
      block = i2c.read_i2c_block_data(address,0,6)
      hum = float(block[2] << 8 | block[3])/10
      tmp = float(block[4] << 8 | block[5])/10
    except :
     print("get_tmp()::ERR!")
     return btemp
    btemp=tmp
    return tmp


if __name__ =="__main__" :
    while True:
      t=get_tmp()
      print(t)
  
    
