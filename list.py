numbers = [1, 2, 3, 4, 5]
numbers.append(6) # append adds an element to the end of the list
print(numbers) # [1, 2, 3, 4, 5, 6]


numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]


numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers) # extend adds each element of the iterable to the end of the list
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]


numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5) # insert adds an element at a specific index, in this case, 2.5 is added at index 2

print(numbers) # [1, 2, 2.5, 3, 4, 5]

numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50) # remove removes the first occurrence of the specified value, in this case, the first 50 is removed from the list

print(numbers) # [10, 20, 30, 40, 50]


numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned and removed from the list
print(numbers) # [1, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]
numbers.pop() # The number 5 is returned and removed from the list
print(numbers) # [1, 2, 3, 4]


numbers = [1, 2, 3, 4, 5]
numbers.clear() # clear removes all elements from the list, leaving it empty

print(numbers) # []


numbers = [19, 2, 35, 1, 67, 41]
numbers.sort() #sort sorts the list in ascending order by default

print(numbers) # [1, 2, 19, 35, 41, 67]


numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers) # sorted returns a new list that is sorted, leaving the original list unchanged

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]


numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse() # reverse reverses the order of the elements in the list

print(numbers) # [1, 2, 3, 4, 5, 6]


programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1



########################################################
