my_set = {1, 2, 3, 4, 5} 

set() # Set
{}    # Dictionary

my_set.add(6)
print(my_set) # {1, 2, 3, 4, 5, 6}

my_set.remove(4) #if the element is not present, it raises a KeyError
print(my_set) # {1, 2, 3, 5, 6
my_set.discard(4) #if the element is not present, it does nothing
print(my_set) # {1, 2, 3, 5, 6

my_set.clear() # clears the set
print(my_set) # set()



my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False if your_set has an element that is not in my_set, otherwise True
print(my_set.issuperset(your_set)) # False if my_set has an element that is not in your_set, otherwise True


print(my_set.isdisjoint(your_set)) # False if my_set and your_set have at least one common element, otherwise True
# iki setteki ortak eleman varsa False, yoksa True

my_set | your_set # {1, 2, 3, 4, 5, 6} # iki setin birleşimi, ortak elemanlar sadece bir kez yazılır
my_set & your_set # {2, 3, 4} # iki setin kesişimi, sadece ortak elemanlar yazılır
my_set - your_set # {1, 5} # iki setin farkı, sadece bir sette bulunan elemanlar yazılır
my_set ^ your_set # {1, 5, 6} # iki setin simetrik farkı, sadece bir sette bulunan elemanlar yazılır


"""
A |= B   →   A = A | B
A &= B   →   A = A & B
A -= B   →   A = A - B
A ^= B   →   A = A ^ B
"""

my_set -= your_set # my_set = my_set - your_set # {1, 5}
print(my_set) # {1, 5}

