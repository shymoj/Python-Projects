def bsort(arr):
	for i in xrange(len(arr)):
		for j in xrange(i+1, len(arr)):
			if arr[j] < arr[i]:
				arr[i], arr[j] = arr[j], arr[i]
	print arr

				
arrs = [5,1,2,8,7,9,6]
bsort(arrs)



			
