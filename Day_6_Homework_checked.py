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
        if x[0] == 'a' or x[0] == 'A':  # Պետք է բոլոր ձայնավորների համար ստուգենք
            lst_4_1.append(x)
    return lst_4_1


print(ach(poem.split()))


# 5. We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Write a function to return the number of small bars to use, assuming we always use big bars before small bars. Return
# -1 if it can't be done.
def choc(n: int):  # Սահմանափակ են փոքր ու մեծ սալիկների քանակները։ Ընդհանրապես ֆունկցիայի սահմանումը այսպես պետք է լինի
    # def choc(small, big, n):
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
    if (b - 1 == a or b + 1 == a or b == a) and (a - 1 > c or a + 1 < c) and (b - 1 > c or b + 1 < c):
        return True
    else:
        return False


assert st(4, 1, 3) == True, 'The function is wrong'  # FIXME Այս թեստը չի անցնում, նայիր տես ինչն է խնդիրը
# 7. Write a function that gets a numerical list as an argument. Find the sum of the elements. If a certain element is
# 13 stop the count and return whatever was the sum before that.
example_list = [4, 1, 2253, 32, 13, 64, 1, 90]


def lsum(lst_7) -> int:
    sm = 0
    for x in lst_7:
        if x == 13:
            return sm  # Այսպես էլ սխալ չի։ Ուղղակի երկու անգամ return չգրելու համար կարող ենք այստեղ break անել։
            # Ինչքան քիչ կոդի կրկնություն, այնքան լավ :)
        else:
            sm += x
    return sm


print(lsum(example_list))


# 8. Write down the following functions in a lambda form

def square(x):
    return x ** 2


def circle_area(r, pi=3.14):
    return pi * r ** 2


def sum_to_power(x, y, p):
    return (x + y) ** p


sq = lambda n1: n1 ** 2
ca = lambda r1, pi=3.14: pi * r1 ** 2
stp = lambda n3, n4, n5: (n3 + n4) ** n5
print(sq(2), ca(3), stp(1, 2, 3))


# 9. Create a list from 1-100. Using the filter function, return a new list containing only the numbers ending with 7.
def f(t):
    if t % 10 == 7:
        return True
    else:
        return False


lst_9 = []
for y in range(1, 101):
    lst_9.append(y)
filtered = list(filter(f, lst_9))
print(filtered)


# 10. Create a function that will take a string as an argument. Return a new string which is the original string with
# each letter doubled. For example 'cat' will become 'ccaatt'
def sd(str_10: str):
    str_10_1 = ''
    for character in str_10:
        str_10_1 += character  # Կարող ենք միայն մի տողով սա անել։ str_10_1 += 2 * character
        str_10_1 += character
    return str_10_1


print(sd('Cat'))

"""Ընդհանուր լավ է Արտյոմ ջան"""
