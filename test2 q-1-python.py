
numbers = [10, 20, 30, 40, 50, 20, 30, 60, 70, 80, 90]

#Use append() to add [100, 110] as a single element. 
numbers.append([100, 110])
print(numbers)

# Use extend() to add elements 120, 130 separately
numbers.extend([120, 130])
print(numbers)

# Insert 25 at index 2 using insert(). 
numbers.insert(2, 25)
print(numbers)
#	Remove the first occurrence of 20 using remove(). 
numbers.remove(20)
print(numbers)

#Remove the last element using pop() and store it. 
numbers.pop()
print(numbers)

#Find index of first 40 using index(). 
print(numbers.index(40))

#Count how many times 30 appears using count(). 
print(numbers.count(30))

#Reverse the list using reverse(). 
numbers.reverse()
print(numbers)

#Flatten [70, 80] and merge into main list (advanced logic + methods). 
numbers.remove(70)
numbers.remove(80)
numbers.extend([70, 80])
print(numbers)

#Sort only the top-level elements (ignore nested list) using sort() — explain issue.
nums_only = [x for x in numbers if not isinstance(x, list)]
nums_only.sort()
print(nums_only)
# The list contains both integers and a nested list ([100, 110]).pyton’s sort() cannot compare different data types like int and list, so it raises a TypeError.solve this, we first filter out the nested list and keep only the top-level integer elements.then we applsort() on this filtered list.



