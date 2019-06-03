def pivot_partition(arr,left_index, right_index):
	"""It will identify the pivot and put the elements accordingly.
	
	It will put the elements less than pivot left side and greater than pivot right side.
	"""
	pivot = arr[left_index]
	pivot_position = left_index + 1
	for j in range(left_index+1, right_index):
		if arr[j] <= pivot:
			(arr[pivot_position], arr[j]) = (arr[j], arr[pivot_position])
			pivot_position += 1
	arr[left_index], arr[pivot_position-1] = arr[pivot_position-1], pivot
	return pivot_position-1

def quicksort(arr,left_index,right_index):
	"""Method to add the quick sort"""
	if not left_index==right_index:
		pivot_position = pivot_partition(arr,left_index,right_index)
		quicksort(arr,left_index,pivot_position)
		quicksort(arr,pivot_position+1,right_index)


