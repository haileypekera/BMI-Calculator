currentNum=1
priorNum1=0
priorNum2=1
counter=1
#counter keeps track of the number in the sequence becuase we only want 25
while(counter<=25):
	print (str(counter)+": " + str(currentNum))
	currentNum= priorNum1 + priorNum2
	priorNum1= priorNum2
	priorNum2= currentNum
	counter= counter + 1
	