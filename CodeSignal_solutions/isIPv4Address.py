#An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
#Given a string, find out if it satisfies the IPv4 address naming rules.

def isIPv4Address(inputString):
    l=inputString.split('.')
    b=True
    if len(l)==4:
        for i in range(4):
            print(l[i])
            if len(l[i])>0 and b:
                for j in range(len(l[i])):
                    if not(ord('0')<=ord(l[i][j])<=ord('9')):
                        b=False
                if b:
                    if l[i][0]=='0' and len(l[i])>1:
                        b=False
                    else:
                        x=int(l[i])
                        if not(0<=x<=255):
                            b=False        
    else:
        b=False
    return b
print(isIPv4Address(".254.255.0"))
