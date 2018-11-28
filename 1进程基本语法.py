# from time import sleep
#
# def run():
#     while True:
#         print("sunck is a nice man")
#         sleep(1.2)
#
# if __name__ == "__main__":
#     while True:
#         print("sunck is a good man")
#         sleep(1)
# #不会执行到run方法，只有上面的while循环结束才可以执行
#     run()
#

###############
'''
multiprocessing库
跨平台版本的进程模块，提供一个Process类代表一个进程对象
'''
from multiprocessing import Process
from time import sleep
import os

def run(str):
    while True:
        #os.getpid 获取主进程id号
        # os.getppid 获取单前进程的父进程id号
        print("sunck is a %s man--%s--%s"%(str,os.getpid(),os.getppid()))
        sleep(1.2)

if __name__ == "__main__":
    print("主（父）进程启动")
    #创建子进程
    # target说明进程执行的任务
    p = Process(target=run,args=("nice",))
    p.start()
    while True:
        print("sunck is a good man")
        sleep(1)


###############
#父子进程执行先后顺序
def run(str):
    print("子进程启动")
    sleep(3)
    print("子进程结束")
if __name__ == "__main__":
    print("主（父）进程启动")
    p = Process(target=run,args=("nice",))
    p.start()
    #父进程的结束不能影响子进程，让父进程等待子进程结束再执行父进程
    p.join()
    print("主（父）进程结束")


###############
#全局变量在多个进程中不能共享

from multiprocessing import Process
from time import sleep
num = 100
def run():
    print("子进程开始")
    global num
    num = num + 1
    print(num)

    print("子进程开始")
    print("子进程结束")

if __name__ == "__main__":
    print("父进程开始")
    p = Process(target=run)
    p.start()
    p.join()
    #在子进程中修改全局变量对父进程中的全局变量没有影响
    #在创建子进程时对全局变量做了一个备份，父进程与子进程中的num是两个完全不同的变量
    print("父进程结束%s"%(num))

###############
from  multiprocessing import Pool
import os,time,random
def run(name):
    print("子进程%s启动--%s"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("子进程%d结束--%s --耗时%.2f"%(name,os.getpid(),end-start))

    print("子进程结束")
if __name__ == "__main__":
    print("父进程启动")
    #创建多个进程
    #进程池
    #表示可以同时执行的进程数量
    #Pool默认大小是CPU核心数
    pp = Pool(2)
    for i in range(5):
        #创建进程池，放入进程统一管理
        pp.apply_async(run,args=(i,))
    #在调用join之前，必须先调用close，调用close之后不能在继续添加新的进程
    pp.close()
    #进程池对象调用join,会等待进程池中所有的子进程结束完毕再去执行父进程
    pp.join()
    print("父进程结束")




###############
def copyFile(rpath,wpath):
    fr = open(rpath,"rb")
    fw = open(wpath,"rb")
    contxet = fr.read()
    fw.write(contxet)
    fr.close()
    fw.write()


path  = ""
topath = ""
filelist = os.listdir(path)
start = time.time()
for filename in filelist:
    copyFile(os.path.join(path,filename),os.path.join(topath,filename))
end = time.time()
print("总耗时：%0.2f"%(end-start))

###############
from multiprocessing import Pool
if __name__ == "__main__":
    filelist = os.listdir(path)
    start = time.time()
    #启动两个进程池
    pp = Pool(2)
    for filename in filelist:
        pp.apply_async(copyFile,args=(os.path.join(path,filename),os.path.join(topath,filename)))
    pp.close()
    # 进程池对象调用join,会等待进程池中所有的子进程结束完毕再去执行父进程
    pp.join()
    end = time.time()
    print("父进程结束%s"%(end-start))

