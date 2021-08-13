#Given a string, return its encoding defined as follows:
#•	First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
#o	for example, "aabbbc" is divided into ["aa", "bbb", "c"]
#•	Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
#o	for example, substring "bbb" is replaced by "3b"
#•	Finally, all the new strings are concatenated together in the same order and a new string is returned.

def lineEncoding(s):
    i=0
    result=''
    while i < len(s):
        ch=s[i]
        i+=1
        if i==len(s):
            result +=ch
            break
        count=1
        while s[i]==ch:
            count+=1
            ch=s[i]
            i+=1
            if i==len(s):
                break
        if count >1:
            result+=str(count)+ch
        else:
            result +=ch
    return result
