# queues are structures that take in data in a certain order to then
# output it in a certain order. The default queue type is the so-called FIFO
# queue . This stands for first in first out and the name describes exactly what it
# does. The elements that enter the queue first are also the elements that will
# leave the queue first.

import queue

print('\n# Queues default FIFO')
q= queue.Queue()

for x in range(5):
    q.put(x)

for x in range(5):
    print(q.get(x))