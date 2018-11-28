###############
###############
from multiprocessing import Pool
import os,time
def copyFile(rpath,wpath):
    fr = open(rpath,"rb")
    fw = open(wpath,"rb")
    contxet = fr.read()
    fw.write(contxet)
    fr.close()
    fw.write()

if __name__ == "__main__":

    path  = ""
    topath = ""
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