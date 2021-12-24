import threading
import queue
import math

q = queue.Queue()
threads = []


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(math.factorial(item))
        q.task_done()
        # we use the function
        # task_done of the queue, in order to signal that the element was processed.


for x in range(5):
    t = threading.Thread(
        target=worker
    )
    t.start()
    threads.append(t)

zahlen = [134000, 14, 5, 300, 98, 88, 11, 23]

for item in zahlen:
    q.put(item)
q.join()

for i in range(5):
    q.put(None)
