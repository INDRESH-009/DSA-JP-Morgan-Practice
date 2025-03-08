#Problem : Find the First Missing Positive Integer
#Statement: Given an unsorted array of integers, find the smallest missing positive integer.
""" 
Input: [3, 4, -1, 1]
Output: 2

my thinking : 
1. i will first sort the array 
2. then at index 0 i will mave the min val and at last index i will have max value 
3. now i will run a loop from min to max incrementing by 1 and check if the number is in the list 
4. if not i will print the number 
"""
def missing_positive(arr):
    arr.sort()
    n = len(arr)
    for i,num in enumerate(arr):
        if num>0:
            positive_index = i
            break
    for i in range(positive_index,n-1):
        if i not in arr:
            return i
    return []
print(missing_positive([3,-1,1,4]))