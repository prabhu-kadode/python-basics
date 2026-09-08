strName  = "ab"
searchStr = "ab"

def printAll(i):
    # if i == searchStr:
    #     print(i,searchStr)
    print(i)
    if i == searchStr:
        print(i,searchStr)

    if len(i)>=len(strName):
        return 
    for n in strName:
        printAll(i+n)
       
    

printAll("")
