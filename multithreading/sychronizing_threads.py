# Basically, one
# thread is locking all of the other threads and they can only continue to work
# when the lock is removed.

import threading
import time

x = 8192

lock=threading.Lock() # comment to get the difference

# Here we have two functions and the variable x that starts at the value 8192 .
# The first function halves the number as long as it is greater than one, whereas
# the second function doubles the number as long as it is less than 16384 .

def halve():
    global x,lock # comment 'lock' to get the difference
    lock.acquire() # comment to get the difference
    while (x > 1):
        x /= 2
        print(x)
        time.sleep(1)
    print('END!')
    lock.release() # comment to get the difference
    


def double():
    global x,lock # comment 'lock' to get the difference
    lock.acquire() # comment to get the difference
    while(x < 16384):
        x *= 2
        print(x)
        time.sleep(1)
    print('End!')
    lock.release() # comment to get the difference

t1=threading.Thread(target=halve)
t2=threading.Thread(target=double)

t1.start()
t2.start()

# With locking we can now let one function finish before the next function
# starts.
