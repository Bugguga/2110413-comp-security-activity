characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_text = (
    "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."
)
import enchant
dictionary = enchant.Dict("en_US")
def find_plain_text_with_all_keys(key, length,target):
    if length == target:
        cipher_disc = dict()
        start=target
        for i in range(length):
            cipher_disc[key[i]] = characters[i].lower()
        for char in characters:
            if char not in key:
                cipher_disc[char]=characters[start].lower()
                start+=1                
        suspected_plain_text = ""
        for char in cipher_text:
            if char != " " and char != ".":
                suspected_plain_text += cipher_disc[char]
            else:
                suspected_plain_text += char
        checked_word = suspected_plain_text.split(" ")
        count = 0
        for word in checked_word:
            if dictionary.check(word.replace(".", "")):
                count+=1
        if count == len(checked_word):
            print("key: "+(key)+" validation: "+str(count/len(checked_word)*100)+ "%")
            print(suspected_plain_text)
            exit(0)
        else:
            print("key: "+(key)+" validation: "+str(count/len(checked_word)*100) + "%")
            return
    else:
        for cipher_character in characters:
            if cipher_character not in key:
                find_plain_text_with_all_keys(
                    key+cipher_character, length+1, target)

for i in range(1,27):
    find_plain_text_with_all_keys('', 0, i)
