# %%
import math

age = 15
old_enough_to_get_driving_license = age >= 17

print(old_enough_to_get_driving_license)
print(type(old_enough_to_get_driving_license))


# %%
x = int(input("Give us a number:"))
if x % 2 == 0:
    print(f'{x} is even.')
    print('Did you know that 2 is the only even number that is a prime?')
else:
    print(f'{x} is odd.')
    print(
        'Did you know that multiplying two odd numbers always gives an odd result?'
    )


# %%
x = int(input("Give us a positive number, to determine it's square root:"))
if x < 0:
    raise ValueError
print(f'The square root of {x} is {math.sqrt(x):.2f}.')

# %%
