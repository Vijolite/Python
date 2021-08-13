#Given a rectangular matrix of characters, add a border of asterisks(*) to it.
def first_last_line(n):
    s=''
    for i in range(n):
        s=s+'*'
    return s
        
def addBorder(picture):
    new_pic=[]
    new_pic.append(first_last_line(len(picture[0])+2))
    for j in range (len(picture)):
        new_pic.append('*'+picture[j]+'*')
    new_pic.append(first_last_line(len(picture[0])+2))
    return new_pic

picture = ["abc",
           "ded"]
print(addBorder(picture))
