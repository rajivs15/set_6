n=int(input())
summ=0
while (n>0):
	dig=n%10
	summ=summ+dig
	n=n//10
print(summ)
