'''Merge Sort'''
def merge_sort(input_array):
	'''Sort the input array in ascending order.

	Args:
		input_array: Array to be sorted.

	Returns:
		Sorted array.
	
	'''
	input_length = len(input_array)
	if input_length == 1:
		return input_array
	else:
		return merge(input_array,merge_sort(input_array[:input_length//2]), merge_sort(input_array[input_length//2:]))

def merge(input_array, left_side, right_side):
	'''Merges two arrays in ascending order.

	Args:
		left_side: Left Array.
		right_side: Right Array

	Returns:
		Merged array in ascending array.
	'''
	output_length = len(input_array)
	left_side_counter = 0
	right_side_counter = 0
	for i in range(output_length):
		if (left_side[left_side_counter] < right_side[right_side_counter]):
			input_array[i] = left_side[left_side_counter]
			left_side_counter += 1
			if(len(left_side) == left_side_counter):
				input_array[i+1:] = right_side[right_side_counter:]
				break
		else:
			input_array[i] = right_side[right_side_counter]
			right_side_counter += 1
			if(len(right_side) == right_side_counter):
				input_array[i+1:] = left_side[left_side_counter:]
				break
	return input_array