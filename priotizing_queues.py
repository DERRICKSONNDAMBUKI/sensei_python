# prioritized queues,in this, every
# element gets assigned a level of priority that determines when they will leave
# the queue

import queue

q = queue.PriorityQueue()

q.put((8,'Some String'))
q.put((1,2023))
q.put((90,True))
q.put((2,10,23))

while not q.empty():
    print(q.get()[1]) # If you only want to access the actual value, you need to address the index one because it
    # is the second value of the tuple.
    
# When we put a
# new element into this queue, we need to pass a tuple as a parameter. The first
# element of the tuple is the level of importance (the lower the number, the
# higher the priority) and the second element is the actual object or value that
# we want to put into the queue.