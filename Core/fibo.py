__author__ = 'N05F3R4TU'
import time

def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

start = time.time()
for c in range(0, 9099):
    print(fibonacci(c))
end = time.time()
total = end - start
print("Total Elapsed", total)