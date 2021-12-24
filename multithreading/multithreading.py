import threading

def hello():
    print('Hello Ricky')
    
t1=threading.Thread(target=hello)
t1.start()

# we used the function start to put our thread to work. Another
# alternative would be the function run .
# When we use the run function to execute our threads, they run serially one
# after the other. They wait for each other to finish. The start function puts all
# of them to work simultaneously.

# When you run this script, you will notice that the output alternates between
# ONEs and TWOs . Now if you use the run function instead of the start
# function, you will see 1000 times ONE followed by 1000 times TWO . This
# shows you that the threads are run serially and not in parallel.
def function1():
    for x in range(1000):
        print('ONE')

def function2():
    for x in range( 1000):
        print('TWO')

t2=threading.Thread(target=function1())
t3=threading.Thread(target=function2())
t2.start()
t3.start()