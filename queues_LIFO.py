# An alternative to the FIFO queues would be the LIFO queues . That stands
# for last in first out . You can imagine this queue like some sort of stack. The
# element you put last on top of the stack is the first that you can get from it.

import queue

print('\n# LIFO Queues\n')
q=queue.LifoQueue()

numbers = [1,2,3,4,5]

for x in numbers:
    q.put(x)

while not q.empty():
    print(q.get())