myNum = int ( raw_input())                
myDict = {}                               
for i in range(0,myNum):                  
        myStr = raw_input()               
        myList = myStr.split()            
        myDict[myList.pop(0)] = myList    
mySearch = raw_input()
myL = myDict[mySearch]      
mySum = sum (float (i) for i in myL)
myT = mySum / len(myL)
print("%.2f" % myT)
