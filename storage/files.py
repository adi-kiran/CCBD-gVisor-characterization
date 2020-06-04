#!/usr/bin/python
import time

# Open and close a file
start = time.time()
for i in range(100000):
    fo = open("test.txt", "w+")
    fo.close()
time_taken = time.time() - start
print(time_taken/100000)