###############
#二次封装
from multiprocessing import Process
import os,time
class SunckProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name = name
    def run(self):
        print("子进程%s - %s启动"%(self.name,os.getpid()))
        time.sleep(3)
        print("子进程%s - %s结束" % (self.name, os.getpid()))