import threading

# printing the text “HELLO WORLD!”
# 500,000 times. But what you will notice is that the last print statement gets
# executed immediately after our thread starts and not after it ends.

def function():
    for x in range(50):
        print('HELLO SENSEI!')

# t1=threading.Thread(target=function())
# t1.start()
print('THIS IS THE END!')

# By using the join function here, we wait for the thread to finish before we
# move on with the last print statement. If we want to set a maximum time that
# we want to wait, we just pass the number of seconds as a parameter

t1=threading.Thread(target=function())
t1.start()
t1.join(5)