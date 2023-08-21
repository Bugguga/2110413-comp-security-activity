import time
import hashlib
import math

string = "password"
sum = 0
for i in range(100000):
    start = time.time()

    hased = hashlib.sha1((string).encode('utf-8')).hexdigest()

    end = time.time()

    elapsed = end-start
    sum += elapsed
# assume elapsed time for hashing 1 to n chars of string are equal.
avg_hashed = sum/100000
print(avg_hashed)

# for question5
# print(math.log((31556926*(61)/(avg_hashed)/62)+1, 62))
