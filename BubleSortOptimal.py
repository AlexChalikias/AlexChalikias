def BubbleSortOpttimal(a):
	n=len(a)
	p=0
	for i in range(n-1):
		sorted=True
		for j in range(n-1,i,-1):
			if a[j]<a[j-1]:
				a[j],a[j-1]=a[j-1],a[j]
				sorted=False
			p+=1
			if sorted:
				return
