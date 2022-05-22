from multiprocessing import Process, Lock, Value
from time import sleep
import os, random


def worker(msg, counter, lock):
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
  
    for i in range(0, 30):
        #lock.acquire()
        with counter.get_lock():
            counter.value += 1
        print(msg, end='', flush=True)
        #lock.release()
        wait = random.randint(1,2) * 0.1
        sleep(wait)


def main():
    print('Starting')
    print('process id:', os.getpid())
    lock = Lock()
    counter = Value('i', 0)
    t2 = Process(target=worker, args=('A', counter, lock))
    t3 = Process(target=worker, args=('B', counter, lock))
    t4 = Process(target=worker, args=('C', counter, lock))
    t2.start()
    t3.start()
    t4.start()
    t2.join()
    t3.join()
    t4.join()
    print('\nDone counting: ' + str(counter.value))

if __name__ == '__main__':
    main()