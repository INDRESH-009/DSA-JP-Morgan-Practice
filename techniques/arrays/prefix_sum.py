""" 
Prefix sum - used for range queries 
allows fast sum retrival in subarrays 

Prefix sum method steps :
    1. make a prefix array which is initalised with zeros and its size is equal to len(arr)+1
    2. now loop over the given arr and for each value arr[i] , add it to the existing number in the prefix[i] for the next position prefix[i+1]
    3. finally return the prefix 
"""
def prefix_sum(arr):
    prefix = [0]*(len(arr)+1)
    for i in range(len(arr)):
        prefix[i+1] = prefix[i]+arr[i]
    return prefix

prefix = prefix_sum([1,2,3,4,5])
print(prefix)  #[0,1,3,6,10,15]

#find sum of sumarray [1,3] - sum from 1 to 3 index - 2+3+4 = 9
# sum till 4 - sum till 1 = 10-1 = 9
print(prefix[4]-prefix[1])

