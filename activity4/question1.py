cipher = "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE"

mapChar = dict()

for char in cipher.strip():
    if char in mapChar:
        mapChar[char]+=1
    else:
        mapChar[char]=1

sortedMap = dict(sorted(mapChar.items(), key=lambda item: item[1]))
for char, count in sortedMap.items():
    print(char+"="+str(count))
