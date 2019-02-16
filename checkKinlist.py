N,K=map(int,(input().split()))
m=list(map(int,input().split()))
count=0
if len(m)==N:
	for i in range (0,N):
		if m[i]==K:
			count=count+1
if count ==0:
	print('no')
else:
	print('yes')
