"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։
num = 1
for i in range(3):
    for j in range(3):
        print(f'{num*num} ', end='')
        num += 1
    print()
print('█' * 100)
# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։
num = 1
list=[]
for i in range(3):
    for j in range(3):
        list.append(num*num)
        num += 1
print(list, '\n', '█' * 100, sep='')
# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։
nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
total=0
for char in nonsense:
    if char == 'b' or char == 'B':
        total += 1
print(total, '\n', '█' * 100, sep='')
# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։
fnum = int(input('Input number: '))
fact = 1
for u in range(1, fnum+1):
    fact *= u
print(fact, '\n', '█' * 100, sep='')