#Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

def sortByHeight(a):
    li_num=[]
    for i in range (len(a)):
        if a[i]!=-1:
            li_num.append(a[i])
    li_num.sort()
    pos=0
    for i in range (len(a)):
        if a[i]!=-1:
            a[i]=li_num[pos]
            pos+=1
    return a

print(sortByHeight([-1,150,190,170,-1,-1,160,180]))
