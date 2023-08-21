import hashlib
import csv
import time

start = time.time()

lis = []
words = set()
dic = dict()

substitutions = {
    'o': '0',
    'l': '1',
    'i': '1',
}


def transform(word):
    lis = [0] * len(word)
    combi(len(word), lis, 0, word)


def combi(n, sol, leng, w):
    if (leng < n):
        sol[leng] = 0
        combi(n, sol, leng+1, w)

        if (w[leng].isalpha()):
            sol[leng] = 1
            combi(n, sol, leng+1, w)

        if (w[leng] in substitutions):
            sol[leng] = 2
            combi(n, sol, leng+1, w)
    else:
        for i in range(len(sol)):
            if (sol[i] == 1 and w[i].isalpha()):
                w = w[:i] + w[i].upper() + w[i+1:]
            elif sol[i] == 2:
                w = w[:i] + substitutions[w[i]] + w[i+1:]
        words.add(w)


with open('10k-most-common.txt', 'r') as file:
    dictionary_words = [line.strip() for line in file]

for word in dictionary_words:
    transform(word)

data = []
for word in words:
    data.append((word, hashlib.sha1((word).encode('utf-8')).hexdigest()))


csv_file = "rainbow.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["substituded", "hash"])
    writer.writerows(data)

end = time.time()

elapse = end - start
print(f"Elapsed time: {elapse:.6f} seconds")
print("CSV file created and data added.")
