programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)
    """Rust
Java
Python
C++
"""

for char in 'code':
    print(char)
    """c
o
d
e
"""


categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

"""
Fruit Apple
Fruit Carrot
Fruit Banana
Vegetable Apple
Vegetable Carrot
Vegetable Banana
"""


secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

"""
Guess the number (1-5): 2
Wrong! Try again.
Guess the number (1-5): 1
Wrong! Try again.
Guess the number (1-5): 3
You got it!
"""



developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break # break exits the loop when the condition is met, so the loop will stop iterating once it reaches 'Naomi'
    print(developer)


developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue # continue skips the current iteration when the condition is met, so the loop will skip printing 'Naomi' but will continue iterating through the rest of the list
    print(developer)



words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")

"""
'sky' has no vowels
'apple' contains the vowel 'a'
'rhythm' has no vowels
'fly' has no vowels
'orange' contains the vowel 'o'
"""


for num in range(3):
    print(num)
#range(start, stop, step) generates a sequence of numbers starting from the start value (inclusive) to the stop value (exclusive) with a step value. If start is not provided, it defaults to 0, and if step is not provided, it defaults to 1. In this case, range(3) generates the numbers 0, 1, and 2.