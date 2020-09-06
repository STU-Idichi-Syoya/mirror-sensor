import distance_sensor

import sensor_temp
import sevenSeg
import sevenSeg
import thirmal_sensor
import time

## 温度センサ初期化
Temp_sensor=sensor_temp.temp_sensor()

## 距離センサ初期化
distance_sensor.init_sensors(temp_sensor_instance=Temp_sensor)

## 体温センサ初期化
thirmal_sensor=thirmal_sensor.sensor_amgx()

#7セグ初期化
seven=sevenSeg.seven_segment()
sevenQue=seven.get_controller()

import conf
KEEP_TIME=conf.keep_time

while True:
    temp=sensor_temp.get_temp()
    distance=distance_sensor.get_distance()
    stime=time.time()
    e=0

    ## showAnime(wait)
    while 35<=distance<=45 and (e-stime)<KEEP_TIME:
        e=time.time()
        ## showAnime(mesurering)
        distance=distance_sensor.get_distance()
    

    total=0
    ## avg_dur回の平均を出す
    count=conf.avg_dur

    ## 受理
    if (e-stime)>=KEEP_TIME:
        ## showAnime(mesurering_thirmal)
        ## avg_dur回の平均値を出す。規定温度にならない場合、なるまでcontinue
        while count>0 :
            arr=thirmal_sensor.get_tmp_8x8()
            arr[arr<35.0]=0
            arr[arr>43.0]=0
            thirmal_temp=arr.max()
            if thirmal_temp==0:
                continue
            else:
                count-=1
                total+=thirmal_temp
        
        
        avg=total/10
        if avg>37.5:
            #alart()
            pass
        else:
            #alart()
            pass
        ## todo 表示
        ## shownumber(avg)

        time.sleep(2.0)

    ## 不受理
    else:
        time.sleep(0.2)

        

        

        

        



