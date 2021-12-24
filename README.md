### Multithreading
A thread has a beginning or a start, a working sequence and an end. But it can
also be stopped or put on hold at any time. The latter is also called sleep .
There are two types of threads: Kernel Threads and User Threads . Kernel
threads are part of the operating system, whereas user threads are managed by
the programmer. That’s why we will focus on user threads in this book.
In Python, a thread is a class that we can create instances of. Each of these
instances then represents an individual thread which we can start, pause or
stop. They are all independent from each other and they can perform different
operations at the same time.