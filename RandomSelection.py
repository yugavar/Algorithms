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


def randomselection(arr, start_index, end_index, order):
  """This method returns the ith smallest element in the array passed.

  Args:
    arr: Input Array.
    start_index: Starting index of the array.
    end_index: Length of the Array.
    order: Order of the statistic.

  Returns:
    ordered statistic.

  """
  print("-----------------------------------------------------------")
  print("Array:", arr)
  print("Order:", order)

  if start_index==end_index:
    return arr[start_index]
  pivot_position = pivot_partition(arr,start_index,end_index)
  print("Pivot Position:", pivot_position)
  if order == pivot_position:
    return arr[pivot_position]
  elif pivot_position > order:
    return randomselection(arr, start_index, pivot_position, order)
  else:
    return randomselection(arr, pivot_position+1, end_index, order)


