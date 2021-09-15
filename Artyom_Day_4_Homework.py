"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։
num = 1
lst_1 = []
lst_2 = []
for i in range(0, 3):
    for j in range(0, 3):
        lst_2.append(num * num)
        num += 1
    lst_1.append(list(lst_2))
    lst_2.pop()
    lst_2.pop()
    lst_2.pop()
print(lst_1)
print('█' * 100)
# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։
lst_1 = [[[num**2 for num in range(1, 10)] for j in range (1, 4) ] for i in range(1, 4)]
print(lst_1)
print('█' * 100)
# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։
nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
total = 0
for char in nonsense:
    if char == 'b' or char == 'B':
        total += 1
print(total, '\n', '█' * 100, sep='')
# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։
fnum = int(input('Input number: '))
fact = 1
for u in range(1, fnum + 1):
    fact *= u
print(fact, '\n', '█' * 100, sep='')
