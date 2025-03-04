#core concepts for solving interview questions in python from neetcode video titled : "Python for Coding Interviews - Everything you need to Know"

""" 
INDEX : 
1.Lists/Arrays
2.Sorting
3.List comprehension
4.2d arrays 
"""
#-----------------------------------------------------------------------
# 1. Lists (Similar to array)

import enum


arr = [1,2,3,4,5]
print(arr)

#Arrays in python are dynamic arrays by default - size is variable like vectors so since they are dynamic arrays they can be used as stacks (we can push,pop..)

arr.append(10)
print(arr)

arr.pop()           #pops last element
print(arr)
arr.pop(2)          #pop element from index 2          
print(arr)

arr.insert(1,7)     #insert at middle - 7 at index 1
print(arr)

#reading the array using index
arr[0] = 100
print(arr[0])

#initialise an array of variable size n(say 7) with al elements as 10
n = 7
arr = [10]*7
print(arr)
print(len(arr))

#negative indexing -> index form the last 
print(arr[-1])
print(arr[-2])

#Getting sublsits from a list (aka slicing) - list[start:stop:step] - 
l = [10,20,30,40,50]
#slice from 2nd number to 4th number 
print(l[1:4])
#slice from 1st to last number only even index
print(l[::2])
#reverse the list - slice from 1st to last in reverse 
print(l[::-1])

#Unpacking 
#All the elements of a list can be unpacked and assigned to a variable , make sure the variable in the LHS is equal to no.of elements in the list
a,b,c = [1,2,3]
print(a,b,c)

#loping through lists
nums = [1,2,3,4]
#using index
for i in range(len(nums)):
    print(nums[i])
#directly over the values of the list 
for n in nums:
    print(n)
# if we need both the index and the value then use enumerate function
for i,n in enumerate(nums):
    print(i,n)

#loop through multiple arrays simultaneously