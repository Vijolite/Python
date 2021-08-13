#You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.
#Assuming that your hunch is correct, decode the message.

def messageFromBinaryCode(code):
    string_decoded=''
    for i in range (0,len(code),8):
        char_binary=code[i:i+8]
        print(char_binary)
        num=0
        for j in range(8):
            if char_binary[j]=='1':
                print(j)
                num=num+2**(7-j)
        string_decoded+=chr(num)
    return string_decoded

print(messageFromBinaryCode("010010000110010101101100011011000110111100100001"))
