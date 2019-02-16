N=int(input())
summ=0
while N>0:
	dig=N%10
	summ=summ+dig
	N=N//10
print(summ)
