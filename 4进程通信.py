# -*- coding:UTF-8 -*-
from multiprocessing import Process,Queue
import os,time

def write(q):
    print("启动写子进程%s"%(os.getpid()))#获取当前进程id
    for chr in ['A','B','C','D']:
        q.put(chr)
        time.sleep(1)
    print("启动写子进程结束%s"%(os.getpid()))
def read(q):
    print("启动读子进程%s" % (os.getpid()))  # 获取当前进程id
    while True:
        value = q.get(True)
        print('value='+ value)
    print("结束读子进程%s" % (os.getpid()))  # 获取当前进程id
if __name__ == "__main__":
    q= Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    #pw进程是个死循环，无法等待其结束，只能强行结束
    pr.terminate()
    print("父进程结束")
