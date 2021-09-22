"""FUNCTIONS"""

# 1. We'll say that an element in an array is "alone" if there are values before and after it, and those values are
# different from it. Return a version of the given array where every instance of the given value which is alone is
# replaced by whichever value to its left or right is larger.
import random


def alch(lst_1):
    for i in range(1, len(lst_1) - 1):
        if lst_1[i] != lst_1[i - 1] and lst_1[i] != lst_1[i + 1]:
            lst_1[i] = max(lst_1[i - 1], lst_1[i + 1])
    return lst_1


print(alch([1, 2, 3, 4, 5, 5, 7, 8, 6, 9]))


# 2. Write a function to create and print a list where the values are square of numbers between 1 and 30
# (both included).
def sq():
    lst_2 = []
    for x in range(1, 31):
        lst_2.append(x ** 2)
    print(lst_2)
    return


sq()


# 3. Write a function which will take one argument n. Return a list of size n, that will contain random numbers
# from (-100, 400).
def rnum(n: int) -> list:
    lst_3 = []
    for x in range(0, n):
        lst_3.append(random.randint(-100, 400))
    return lst_3


print(rnum(int(input('Enter number of elements: '))))
# 4. Write a function, that will take a list as an argument and return all the words in the list that start with a
# vowel.

poem = '''All that is gold does not glitter,
Not all those who wander are lost;
The old that is strong does not wither,
Deep roots are not reached by the frost.
From the ashes a fire shall be woken,
A light from the shadows shall spring;
Renewed shall be blade that was broken,
The crownless again shall be king.'''


def ach(lst_4):
    lst_4_1 = []
    for x in lst_4:
        if x[0] == 'a' or x[0] == 'A':
            lst_4_1.append(x)
    return lst_4_1


print(ach(poem.split()))


# 5. We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Write a function to return the number of small bars to use, assuming we always use big bars before small bars. Return
# -1 if it can't be done.
def choc(n: int):
    kk = 0
    tot = 0
    while kk < n:
        kk += 5
        if kk == n:
            break
        kk += 1
        tot += 1
        if kk == n:
            break
    else:
        tot = -1
    return tot


print(choc(int(input('Enter how much chocolate we need to eat: '))))


# 6. Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more.
def st(a: int, b: int, c: int) -> bool:
    if (b - 1 == a or b + 1 == a or b == a) and ((a - 1 > c or a + 1 < c) and (b - 1 > c or b + 1 < c)):
        return True
    else:
        return False


print(st(5, 6, 8))
# 7. Write a function that gets a numerical list as an argument. Find the sum of the elements. If a certain element is
# 13 stop the count and return whatever was the sum before that.
example_list = [4, 1, 2253, 32, 13, 64, 1, 90]


# 8. Write down the following functions in a lambda form

def square(x):
    return x ** 2


def circle_area(r, pi=3.14):
    return pi * r ** 2


def sum_to_power(x, y, p):
    return (x + y) ** p

# 9. Create a list from 1-100. Using the filter function, return a new list containing only the numbers ending with 7.

# 10. Create a function that will take a string as an argument. Return a new string which is the original string with
# each letter doubled. For example 'cat' will become 'ccaatt'
