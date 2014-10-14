#70 Pt
def turnIntoList(n1,n2,n3):
    list1 = [n1,n2,n3]
    return list1

#80 Pt
def getFirstInList(list2):
     return list2[0]

#90 Pt
def getLastInList(list3):
    lastpos = len(list3) - 1
    return list3[lastpos]

#100 Pt
def swapFirstAndLast(list4):
    lastpos2 = list4[len(list4) - 1]
    temp1 = list4[0]
    list4[0] = lastpos2
    list4[len(list4) - 1] = temp1
    return list4
    
    
