#Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

def longestWord(text):
    i=0
    m=0
    while i<len(text):
        word=''
        while 'a'<=text[i]<='z' or 'A'<=text[i]<='Z':
            word=word+text[i]
            i+=1
            if i==len(text):
                break
        if len(word)>m:
            w=word
            m=len(word)
        i+=1
        
    return w

print(longestWord("Ready, steady, go!"))
