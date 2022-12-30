# kadane's algorithm to find maximum sub array

def max_sub_array(arr):
    n = len(arr)
    cur_sum = 0
    max_sum = arr[0]
    for i in range(0, n):
        cur_sum = cur_sum+arr[i]

        if cur_sum < 0:
            cur_sum = 0
        if cur_sum > max_sum:
           max_sum = cur_sum

    return max_sum



arr=[7,5,2,-7,3,15]
print("the maximum sub array is ", max_sub_array(arr))


