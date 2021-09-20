"""DATA STRUCTURES"""

# 1. Write a program to multiply all the items in a list.
# Գրել ծրագիր, որը կբազմապատկի լիստի բոլոր թվերը։
lst_1 = []
lst_1 = [x * x for x in lst_1]
# 2. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։
tot_2 = 0
lst_2 = []
for str_2 in lst_2:
    if len(str_2) >= 2 and str_2[0] == str_2[-1]:
        tot_2 += 1
# 3. Write a program that will remove duplicates from a list. DO NOT use set() method directly on the list.
# Գրել ծրագիր, որը կջնջի դուպլիկատները լիստից։ ՉՕԳՏԱԳՈՐԾԵԼ set() մեթոդը։
lst_3 = ['a', 'b', 'a']
lst_3.sort()
for t in range(1, len(lst_3) - 1):
    if lst_3[t] == lst_3[t - 1]:
        lst_3.pop(t)
print(lst_3)
# 4. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից
num_4 = 0
lst_4 = []
for inum in range(0, 5):
    lst_4.append(input(f'Enter {inum} number: '))
# 5. Write a program to print the given list after removing the 2nd, 4th and 5th elements.
# Գրել ծրագիր, որը կջնջի տրված լիստի 2-րդ, 4-րդ և 5-րդ էլեմենտները։

lst_5 = ['Rock', 'Pop', 'Metal', 'Hip-Hop', 'Rap']
lst_5.pop(4)
lst_5.pop(3)
lst_5.pop(1)
print(lst_5)
# 6. Given a list of ints, print True if the array contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։
lst_6 = []
for rnum_6 in range(1, len(lst_6) - 1):
    if lst_6[rnum_6] == lst_6[rnum_6 - 1] and lst_6[rnum_6] == 2:
        print(True)
# 7. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:
lst_7 = []
checc = False
for rnum_7 in range(1, len(lst_7) - 1):
    if lst_7[rnum_7] == 1 or lst_7[rnum_7] == 4:
        checc = True
print(checc)
# 8. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ
mdict = {'key': 'Value'}
inkey = input('Enter something: ')
checc_8 = False
for x in mdict.keys():
    if x == inkey:
        Checc_8 = True
if not checc_8:
    mdict.update({inkey: 'something'})
# 9. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։
mdict_9 = {'key': 'Value'}
lst_9 = [n9 for n9 in range(len(mdict_9.values()) - 1)]
# 10. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։
mdict_10 = {}
for num_10 in range(1, 16):
    mdict_10.update({num_10: num_10 ** 2})
print(mdict_10)
