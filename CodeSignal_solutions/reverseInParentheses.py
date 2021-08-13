#Write a function that reverses characters in (possibly nested) parentheses in the input string.
#Input strings will always be well-formed with matching ()s.

def reverseInParentheses(inputString):
    s=inputString
    while ')' in s:
        f_pos=s.find(')')
        s_pos=f_pos
        while s[s_pos]!='(':
            s_pos-=1
        part=s[s_pos+1:f_pos]
        part=part[-1::-1]
        s=s[:s_pos]+part+s[f_pos+1:]
    return s        

print(reverseInParentheses("foo(bar(baz))blim"))
