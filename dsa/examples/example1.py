marks = [1,2,2,2,3,4,3,4,5,5,6,1]

numDict = {}
count = 0
for item in marks:
    if item in numDict:
       if numDict[item]==1:
           count = count+1

       numDict[item] = numDict[item]+1
    else:
        numDict[item] = 1
print(numDict,count)