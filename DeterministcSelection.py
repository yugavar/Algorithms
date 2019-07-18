from MergeSort import *

def sorted_median(array):
    """This method will return the median of the array after sorting"""
    array_length = len(array)
    index = (array_length//2) + (array_length%2)
    return merge_sort(array)[index-1]


# def get_pivot(arr):
#     """This method will give the pivot which is median of medians"""
#     if len(arr)<5:
#         return sorted_median(arr)
#     else:
#         medians = []
#         for i in range(0,len(arr),5):
#             medians.append(sorted_median(arr[i:i+5]))
#         return get_pivot(medians)

def get_pivot_position(pivot,arr):
    """It will identify the pivot and put the elements accordingly.
    
    It will put the elements less than pivot left side and greater than pivot right side.
    """
    pivot_position = 0
    for j in range(0, len(arr)):
        if arr[j] < pivot:
            (arr[pivot_position], arr[j]) = (arr[j], arr[pivot_position])
            pivot_position += 1
        elif arr[j] == pivot:
            equal_position = pivot_position
            (arr[pivot_position], arr[j]) = (arr[j], arr[pivot_position])
            pivot_position +=1
    arr[equal_position], arr[pivot_position-1] = arr[pivot_position-1], pivot
    return pivot_position-1

# def deterministic_selection(arr, start_index, end_index, order):
#     """This method returns the i th smallest element in the array passed.

#     Arguments:
#         arr: Input Array.
#         start_index: Starting index of the array.
#         end_index: Length of the Array.
#         order: Order of the statistic.

#     Returns:
#         ordered statistic.
#     """
#     if start_index==end_index:
#         return arr[start_index]
#     pivot = get_pivot(arr[start_index:end_index])
#     pivot_position = get_pivot_position(pivot, arr,start_index, end_index)
#     if order == pivot_position:
#         #print("arr",arr)
#         return arr[pivot_position]
#     elif pivot_position > order:
#         return deterministic_selection(arr, start_index, pivot_position, order)
#     else:
#         return deterministic_selection(arr, pivot_position+1, end_index, order)


def d_select(array, order):

    print("------------------------------------------------------")
    print("Array:" , array)
    print("Order", order)
    if len(array)==1:
        return array[0]
    
    medians = []
    for i in range(0,len(array),5):
        medians.append(sorted_median(array[i:i+5]))
    pivot = d_select(medians, len(array)//10)
    pivot_position = get_pivot_position(pivot, array)
    print("Pivot", pivot)
    print("Pivot Postion", pivot_position)
    if (order == pivot_position):
        return pivot
    elif pivot_position > order:
        return d_select(array[0:pivot_position],order)
    else:
        return d_select(array[pivot_position+1:], order-pivot_position-1)

