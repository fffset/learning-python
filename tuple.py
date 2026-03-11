developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a') 

programming_languages = ('Python', 'Java', 'C++', 'Rust')

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False


developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'



developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']


programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2 



programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count()

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: tuple.count() takes exactly one argument (0 given)
"""

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java') # 1


programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('JavaScript')

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: tuple.index(x): x not in tuple
"""


programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5 


programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2 2 starts the search at index 2 and ends at index 5, so it finds the first occurrence of 'Python' at index 2


numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]


programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']


programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']