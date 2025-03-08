#Kandane's Algorithm :
""" 
This problem asks: given an array of integers (positive and negative), find the contiguous subarray with the largest sum.

The Algorithm : 

Kadane's algorithm uses dynamic programming with a clever twist. We only need to keep track of two values:
 - The maximum sum ending at the current position
 - The overall maximum sum found so far

Here's how it works:

1. We traverse the array once, from left to right
2. For each element, we decide whether to:
    Start a new subarray at the current element (if the previous sum was negative)
    Extend the existing subarray (if the previous sum was positive)
3. We update our overall maximum whenever we find a better sum

"""

def subarray_with_largest_sum(arr):
    if not arr:
        return []
    current_max = arr[0]
    global_max = arr[0]
    for i in range(1,len(arr)):
        current_max = max(arr[i],current_max+arr[i])
        global_max = max(current_max,global_max)
    return global_max
x =subarray_with_largest_sum([-100,-23,-65,-100,-43,-98])
print(x)