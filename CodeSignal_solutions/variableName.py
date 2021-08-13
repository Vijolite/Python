#Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
#Check if the given string is a correct variable name.

def variableName(name):
    b=True
    if ord('0')<=ord(name[0])<=ord('9'):
        b=False
    if b:    
        for i in range (len(name)):
            if not (ord('0')<=ord(name[i])<=ord('9') or ord('a')<=ord(name[i])<=ord('z')or ord('A')<=ord(name[i])<=ord('Z')or ord(name[i])==ord('_')):
                b=False
    return b
print(variableName('var_1__Int'))
