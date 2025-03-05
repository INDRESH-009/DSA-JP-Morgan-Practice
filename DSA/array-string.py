# DYNAMIC ARRAYS OR LISTS

l = [1,2,3,4,5]
print(l)

#insert at end - on average O(1)
l.append(10)
print(l)

#pop at end - O(1)
l.pop()
print(l)

#insert not at end - O(n) - use .insert(index,value)
l.insert(0,20)
print(l)

#modify element at a particular index - O(1)
l[2] = 30
print(l)

#accessing element at a given index - O(1)
print(l[0])

#Check if an element is in a array - searching through all elements - O(n)
if 10 in l:
    print(True)
else:
    print(False)
    
# Find length of a array - it stores lenth as a property so time is - O(1)
print(len(l))


# STRINGS 

#Append to end of the string - copy prev string and add the new piece - O(n)
str = "abc"
b = str + "def"
print(b)

#Check if something in the string - O(n)
str = "abc"
if 'e' in str:
    print(True)
else:
    print(False)

#Access the characters in the string - O(1)
print(str[2])

# Find length of a string - it stores lenth as a property so time is - O(1)
print(len(str))
