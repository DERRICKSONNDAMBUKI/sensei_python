# With events we can manage our threads even better. We can pause a thread
# and wait for a certain event to happen, in order to continue it.

import threading

event=threading.Event()

def function():
    print('Waiting for event...')
    event.wait()
    print('Continuing!')

thread= threading.Thread(target=function())
thread.start()

x=input('Trigger event?')
if(x=='yes'):
    event,set()
    
# To define an event we use the Event class of the threading module. Now we
# define our function which waits for our event. This is done with the wait
# function. So we start the thread and it waits.

# Then we ask the user, if he wants to trigger the event. If the answer is yes, we
# trigger it by using the set function. Once the event is triggered, our function
# no longer waits and continues with the code.