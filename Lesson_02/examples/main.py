# %%
# Data Types
type("Hello, World!")
type(17)
type(3.2)
type("17")
type("3.2")

# %%
int(3.14)
int(3.9999)
int(3.0)
int(-3.9999)
int(115 / 60)
int("2345")

# %%
print(int("23 bottles"))

# %%
type("This is a string.")
type("And so is this.")
type("""and this.""")
type("""and even this...""")

# %%
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')

# %%
message = """This message will
span several
lines."""
print(message)

# %%
42000
42, 000

# %%
# Variables
n = 17
pi = 3.14159

# %%
day = "Thursday"
day = "Friday"
day = 21
print(day)

# %%
# Operators
5**2

# %%
minutes = 645
hours = minutes / 60
hours

# %%
7 / 4

# %%
7 // 4

# %%
hours = minutes // 60
hours

# %%
remaining_minutes = minutes % 60
remaining_minutes

# %%
fruit = "banana"
baked_good = " nut bread"
print(fruit + baked_good)

# %%
n = input("Please enter your name: ")

# %%
response = input("What is your radius? ")
r = float(response)
area = 3.14159 * r**2
print("The area is ", area)

# %%
r = float(input("What is your radius? "))
print("The area is ", 3.14159 * r**2)

# %%
print("The area is ", 3.14159 * float(input("What is your radius?")) ** 2)
