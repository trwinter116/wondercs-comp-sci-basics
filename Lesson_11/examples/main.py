# %%
ps = [10, 20, 30, 40]
qs = ["spam", "bungee", "swallow"]

# %%
zs = ["hello", 2.0, 5, [10, 20]]

# %%
vocabulary = ["apple", "cheese", "dog"]
numbers = [17, 123]
an_empty_list = []
print(vocabulary, numbers, an_empty_list)

# %%
numbers[0]

# %%
numbers[9-8]

# %%
numbers[1.0]

# %%
numbers[2]

# %%
horsemen = ["war", "famine", "pestilence", "death"]

for h in horsemen:
    print(h)

# %%
"pestilence" in horsemen

# %%
students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

counter = sum("CompSci" in subjects for name, subjects in students)
print("The number of students taking CompSci is", counter)

# %%
# List operations
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
c

# %%
# Slices
a_list = ["a", "b", "c", "d", "e", "f"]
a_list[1:3]

# %%
# Mutable
fruit = ["banana", "apple", "quince"]
fruit[0] = "pear"
fruit[2] = "orange"
fruit

# %%
a_list = ["a", "b", "c", "d", "e", "f"]
a_list[1:3] = ["x", "y"]
a_list

# %%
a_list = ["a", "b", "c", "d", "e", "f"]
a_list[1:3] = []
a_list

# %%
a_list = ["a", "d", "f"]
a_list[1:1] = ["b", "c"]
a_list[4:4] = ["e"]
a_list

# %%
# Deletion
a = ["one", "two", "three"]
del a[1]
a

# %%
# References
a = "banana"
b = "banana"
a is b

# %%
a = [1, 2, 3]
b = [1, 2, 3]
a == b

# %%
a is b

# %%
a = [1, 2, 3]
b = a
a is b

# %%
b[0] = 5
a

# %%
a = [1, 2, 3]
b = a[:]
b
# %%
b[0] = 5
a

# %%
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)

# %%
mylist.insert(1, 12)
mylist

# %%
mylist.count(12)

# %%
mylist.extend([5, 9, 5, 11])
mylist

# %%
mylist.index(9)

# %%
mylist.reverse()
mylist

# %%
mylist.sort()
mylist

# %%
mylist.remove(12)
mylist

# %%
xs = list("Crunchy Frog")
xs

# %%
"".join(xs)

# %%
# Demo List comprehension
