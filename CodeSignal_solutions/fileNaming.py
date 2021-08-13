# You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.
#Return an array of names that will be given to the files.

def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[0:i]:
            ii=i-1
            found=False
            while not(found):
                if names[i]==names[ii][0:len(names[i])]:
                    if len(names[i])==len(names[ii]):
                        num=1
                        while names[i]+'('+str(num)+')' in names[:i]:
                            num+=1
                        names[i]=names[i]+'('+str(num)+')'
                        found=True
                    else:
                        #how many pairs of brackets
                        if names[ii][len(names[i])]=='(':
                            p_br=0
                            br_ind=0
                            for j in range(len(names[i]),len(names[ii])):
                                if names[ii][j] == '(':
                                    p_br+=1
                                    br_ind=j
                            if p_br==1:
                                s=names[ii][br_ind+1:len(names[ii])-1]
                                num=int(s)
                                num+=1
                                while names[i]+'('+str(num)+')' in names[:i]:
                                    num+=1
                                names[i]=names[i]+'('+str(num)+')'
                                found=True
                ii-=1
    return(names)
names = ["doc", "doc", "image", "doc(1)", "doc"]

print(fileNaming(names))
