import multiprocessing
import time
def delayValue(num):
    time.sleep(1-num/10)
    return num

def callback(res):
    print(res)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)

    for i in range(11):
        result = pool.apply_async(delayValue, args=(i,), callback=callback)
    result.get()

    print("finished")