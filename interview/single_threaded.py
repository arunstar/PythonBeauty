
import time
from threading import Thread

COUNT =  100000000

def countdown():
    # while n > 0:
    #     n -= 1
    for _ in range(5):
        time.sleep(1)

start = time.time()
# t1 = Thread(target=countdown(COUNT//2))
# t2 = Thread(target=countdown(COUNT//2))

t1 = Thread(target=countdown)
t2 = Thread(target=countdown)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print("Time taken {}".format(end-start))