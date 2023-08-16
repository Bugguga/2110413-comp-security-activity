import hashlib

lis = []
words = set()
substitutions = {
    'o': '0',
    'l': '1',
    'i': '1',
}


def transform(word):
    lis = [0] * len(word)
    combi(len(word), lis, 0, word)


# def dfs(l,w,i):
#     if(i == len(l)):
#         return
#     if w[i].lower() in substitutions and l[i]==1:
#         new_word = w[:i] + substitutions[w[i].lower()] + w[i+1:]
#         words.append(new_word)
#         l[i] = 2
#         dfs(l,new_word,i+1)
#     if l[i] == 1 or l[i] == 2:
#         dfs(l,w,i+1)
#     else :
#         l[i]=1
#         new_word = w[:i] + w[i].upper() + w[i+1:]
#         words.append(new_word)
#         dfs(l, new_word, i+1)

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
    if "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7" == hashlib.sha1((word).encode('utf-8')).hexdigest() or "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7" == hashlib.md5((word).encode('utf-8')).hexdigest():
        print(word)
