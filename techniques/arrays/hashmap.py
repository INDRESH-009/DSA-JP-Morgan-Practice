""" 
Hashmaps are used in arreay problems when we want to :
    1. helps to track the frequncy of elements 
    2. helps to check the unique occurance of a element in the list 
    
How to apply and use hashmaps in questions :
    1. initialise an empty hashmap if u are going to use it -  hash_map = {}
    2. use an enumerate method while looping over the list to keep track of index of the element if thats what u need to return , else dont need to use enumerate 
    3. The syntax for enumerate method in iterable is :
        for i,num in enumerate(arr):
    4. What this will do is it will return an enumerate object where while looping the arrays value is given and it is connected to its index i in the above code , so if u want to store the index in the hashmap for further retrival is thats what you want to return then it will be useful 
        
"""

# Two sum for unsorted arrays can be solved using hashmaps where we store the number we have encountered and then sub that num from the target to find is that number is in the hashmap , is its present its index is retured along wit the current items index , as they add up to the target , else the number is added along with its index to the hashmap 

def two_sum(arr,target):
    hash_map = {}
    for i,num in enumerate(arr):
        complement = target - arr[i]
        if complement in hash_map:
            return [hash_map[complement],i]
        hash_map[num] = i
    return []

print(two_sum([10,1,3,2,30,40,23],70))
