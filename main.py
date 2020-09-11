import distance_sensor

import sensor_temp
import sevenSeg

import thirmal_sensor
import time

## 温度センサ初期化
Temp_sensor=sensor_temp.get_tmp

## 距離センサ初期化
distance_sensor.init_sensors(temp_sensor_func=Temp_sensor)

## 体温センサ初期化
thirmal_sensor=thirmal_sensor.sensor_amgx()

#7セグ初期化
sevenSeg.setup()
sevenSeg.start_segment()

sevenQue=sevenSeg.digit_que

nexter_str=sevenSeg.CHR_state()

import conf

KEEP_TIME=conf.keep_time
zyuri_KEEP_TIME=conf.zyuri_KEEP_TIME

#print("chk1")
while True:
    next_str=next(nexter_str)
    sevenQue.put(next_str)
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
        print("zyuri 1")
        zyuri_time=time.time()
        ## showAnime(mesurering_thirmal)
        ## avg_dur回の平均値を出す。規定温度にならない場合、なるまでcontinue
        while count>0 :
            arr=thirmal_sensor.get_tmp_8x8()
            arr[arr<35.0]=0
            arr[arr>43.0]=0
            thirmal_temp=arr.max()
            print(thirmal_temp,"zyuri 2")
            if thirmal_temp==0:
                if time.time()-zyuri_time > zyuri_KEEP_TIME:
                    total=-1
                    break
                continue
            
            else:
                count-=1
                total+=thirmal_temp
        
        if total==-1:
            continue
        avg=total/conf.avg_dur
        sevenQue.put(str("%.2fC"%(avg/10)))
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
        print("fu zyuri",distance,"cm")
        time.sleep(0.2)

        

        

        

        



