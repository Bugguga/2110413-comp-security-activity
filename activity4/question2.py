import sys

def main():
    
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 question2.py <arg1> <arg2>")
        return
    table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # Get the arguments
    key = (sys.argv[1])
    text = (sys.argv[2])

    cipher_text = ''

    for i in range(len(text)):
        location = table.index(text[i]) + table.index(key[i%len(key)])
        cipher_text += table[location%26]
    print(cipher_text)
        


if __name__ == "__main__":
    main()
