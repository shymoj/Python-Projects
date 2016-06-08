def selection(arr):
	for i in range(0,len(arr)-1):
		min = i
		for j in range(i+1,len(arr)):
			if arr[j] < arr[min]:
				min = j
			small = arr[min]
			arr[min] = arr[i]
			arr[i] = small
	print arr

arrs = [5,3,2,4,1]
selection(arrs)





