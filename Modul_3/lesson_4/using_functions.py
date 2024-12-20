import time
from os import getpid
from multiprocessing import Pool

start = time.time()
def temp(a):
    print(f"Process ID: {getpid()} - Task {a} started")
    time.sleep(2)
    print(f"Process ID: {getpid()} - Task {a} finished")



if __name__ == "__main__":
    with Pool(100) as p:
        p.map(temp, range(1, 100))



    print(time.time() - start)