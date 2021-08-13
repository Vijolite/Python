#Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

def areSimilar(a, b):
    a_s=a.copy()
    b_s=b.copy()
    a_s.sort()
    b_s.sort()
    if a_s==b_s:
        diff=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                diff+=1
        if diff>2:
            return False
        else:
            return True
    else:
        return False

a=[1,2,2]
b=[2,1,1]
if areSimilar(a,b):
    print('yes')
else:
    print('no')
