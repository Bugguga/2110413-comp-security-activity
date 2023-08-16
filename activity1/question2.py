import hashlib

lis = []
words = []
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

        sol[leng] = 1
        combi(n, sol, leng+1, w)

        if (w[leng] in substitutions):
            sol[leng] = 2
            combi(n, sol, leng+1, w)
    else:
        print("รอแปปนึงไอเวร")
        for i in range(len(sol)):
            if (sol[i] == 1):
                w = w[:i] + w[i].upper() + w[i+1:]
            elif sol[i] == 2:
                w = w[:i] + substitutions[w[i]] + w[i+1:]
        words.append(w)


with open('10k-most-common.txt', 'r') as file:
    dictionary_words = [line.strip() for line in file]

for word in dictionary_words:
    transform(word)


for word in words:
    dic[word] = hashlib.sha1((word).encode('utf-8')).hexdigest()