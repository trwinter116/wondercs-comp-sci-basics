from test_helper import test


# Exercise 1
# Write a function called add_vectors which takes two lists of numbers of the same length
# and returns a new list containing the sums of the corresponding elements of each.
def add_vectors(u, v):
    pass


test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


# Exercise 2
# Write a function called scalar_mult which takes a number 's' and a list 'v'
# and returns the scalar multiple of 'v' by 's'.
def scalar_mult(s, v):
    pass


test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
