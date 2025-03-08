""" 
Used in problems like :
    1. finding pairs 
    2. merging 
    3. detecting conditions effectively 

2 pointer technique :
    1. have 2 pointers , one at start and one at end 
    2. move the two pointers closer to each other wherever they meet certain condition till they meet each other 
"""

# Two sum problem : given a sorted array and a target , find the pair of indices in the array whose sum is equal to the target
def two_sum(arr,target):
    n = len(arr)
    left,right = 0,n-1
    while left<right:
        current_sum = arr[left]+arr[right]
        if current_sum==target:
            return [left,right]
        elif current_sum<target:
            left += 1
        else:
            right -= 1
    return []
print(two_sum([1,2,3,4,5,6,7],7))
