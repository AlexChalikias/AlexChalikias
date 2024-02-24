def BynarySearch2(a,key):
	pos=-1
	first=0
	last=len(a)-1
	while pos==-1 and first<=last:
		mid=(first+last)/2
		if a[mid]==key:
			pos=mid
		elif key>a[mid]:
			first=mid+1
		else:
			last=mid-1
	return pos
