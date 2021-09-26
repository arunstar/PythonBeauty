import threading
import time
import timeit
def do_something():
    for i in range(5):
        time.sleep(1)
        print(i+1)


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

print(timeit.timeit())
t1.start()
t2.start()

t1.join()
t2.join()
print("Done")