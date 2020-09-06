import threading,queue
import conf
from conf import segment_io

import time



'''
gpiolist[gpionum,off,...]
'''
def exe(gpiolist):
    for i in range(len(gpiolist)//2):
        ## todo on off
        pass
    pass

class ANIMETION:
    def __init__(self) -> None:
        self.now_anime_state=0
        #　変化フレーム数
        self.max_anime_frame=500
        # 1フレームあたりの変化秒数（何秒で変化するか）
        self.frame_sec=1
        self.start_time=time.time()

        self.reset()

        ## 秒:[gpio_num,on off ,gpio_num2, on off],
        self.anime_state={1:[]}

    '''gpio resetを含む'''
    def reset(self):
        self.now_anime_state=0

    def next_anime(self,gpios:list):

        if (time.time()-self.start_time)<self.frame_sec:
            return

        d=self.anime_state.get(self.anime_state)
        if d is not None:
            exe(d)

        self.start_time=time.time()
        self.now_anime_state=(self.now_anime_state+1)%self.max_anime_frame


class wait(ANIMETION):
    def __init__(self) -> None:
        pass

class mesurering(ANIMETION):
    def __init__(self) -> None:
        pass

class number(ANIMETION):
    def __init__(self,num:int) -> None:
        pass



class seven_segment:
    def __init__(self,segment_num=4) -> None:
        super(seven_segment,self).__init__()
        self.queue=queue.Queue()
        self.segment_mat=[segment_io[i] for i in range(segment_num)]

    def get_controller(self)-> queue.Queue:
        return self.queue

    def start(self):
        anime=wait
        while True:
            
            if not self.queue.empty():

                nanime=self.queue.get()
                if type(nanime)!=type(anime):
                    anime=nanime()

            anime.next_anime()

            time.sleep(0.01)





def start_segment():
    seven=seven_segment()
    q=seven.get_controller()
    threading.Thread(target=seven.start).start()
    return q


