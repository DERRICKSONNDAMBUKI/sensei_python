# Sometimes we don’t want to completely lock a resource but just limit it to a
# certain amount of threads or accesses. In this case, we can use so-called
# semaphores .

import threading
import time

semaphore = threading.BoundedSemaphore(value=5)


def access(thread_number):
    print('{}: Trying access...'.format(thread_number))
    semaphore.acquire()

    print('{}:Access granted!'.format(thread_number))

    print('{}:waiting 5 seconds...'.format(thread_number))
    time.sleep(5)
    semaphore.release()

    print('{}:Releasing!'.format(thread_number))


for thread_number in range(10):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    
# We first use the BoundedSemaphore class to create our semaphore object.
# The parameter value determines how many parallel accesses we allow. In this
# case, we choose five.
# With our access function, we try to access the semaphore. Here, this is also
# done with the acquire function. If there are less than five threads utilizing the
# semaphore, we can acquire it and continue with the code. But when it’s full,
# we need to wait until some other thread frees up one space.
# When we run this code, you will see that the first five threads will
# immediately run the code, whereas the remaining five threads will need to
# wait five seconds until the first threads release the semaphore.
# This process makes a lot of sense when we have limited resources or limited
# computational power in a system and we want to limit the access to it.
