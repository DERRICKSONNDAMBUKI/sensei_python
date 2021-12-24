# So-called daemon threads are a special kind of thread that runs in the
# background. This means that the program can be terminated even if this
# thread is still running. Daemon threads are typically used for background
# tasks like synchronizing, loading or cleaning up files that are not needed
# anymore.

import threading
import time

path = './test_file.txt'
text=''

def readFile():
    global path,text
    while True:
        with open(path) as file:
            text=file.read()
            print('Reading the file...')
        time.sleep(3)

def printLoop():
    global text
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile,daemon= True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()
# So, here we have two functions. The first one constantly reads in the text from
# a file and saves it into the text variable. This is done in an interval of three
# seconds. The second one prints out the content of text every second but only
# 30 times.