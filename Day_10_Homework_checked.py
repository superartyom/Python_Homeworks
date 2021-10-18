# """MODULES"""
import random
import os
from datetime import datetime
# # 1. Hangman!
# # Create the hangman game. A list containing random words is provided. Each time the program runs, one random word must
# # be selected. Then the user will try to guess the letters of the word. They will have lives equal to the length of the
# # word. Now, about the formatting. Say we have the word car. The program must then output underscores equal to the
# # length of the word.
#
# # Guess a letter!
# # _ _ _
# #
# # if we input 'a', the program will output:
#
# # Guess a letter!
# # _ a _
#
# # and so on.
#
# # Ստեղծում ենք մեր սեփական "Կախաղան" խաղը։ Ծրագիրը պահելու է պատահական բառ տրված "random_words" ֆայլից: Խաղացողը պետք է
# # գուշակի տառ։ Եթե տառը բառի մեջ գոյություն չունի, խաղացողը կորցնում է "կյանք" (կյանքերը բառի երկարության չափ են): Եթե
# # տառը կա, այն բացվում է և խաղացողը անցնում է հաջորդ տառը գուշակելուն։ Ծրագրի աշխատանքը պետք է հետևյալ տեսքն ունենա։
# # Ենթադրենք բառը car է։ Կոնսոլում հետևյալ տեսքստն ենք տեսնելու
#
# # Guess a letter!
# # _ _ _
#
# # Եթե ներմուծենք a, կստանանք հետևյալ տեսքստը
#
# # Guess a letter!
# # _ a _
#
# # և այդպես շարունակ։ Եթե խաղացողի կյանքերը սպառվեն, տեղեկացրեք նրան և խաղից դուրս եկեք։ Հաղթելու դեպքում տպեք
# # շնորհավորանք
# lst_1_1 = []
# file = open('random_words.txt', 'r')
# for word in file.readlines():
#     lst_1_1.append(word)
# file.close()
#
# lst_1_2 = list(random.choice(lst_1_1))
# if lst_1_2[-1] == '\n':
#     lst_1_2 = lst_1_2[0:-1]
# lives = len(lst_1_2)
# lst_1_3 = []
#
#
# def check(character):
#     global lives
#     for x in range(0, len(lst_1_2)):
#         if lst_1_2[x] == character and lst_1_3[x] == '_':
#             lst_1_3[x] = str(character)
#             return
#     print('-Life')
#     lives -= 1
#     return
#
#
# for ind in range(0, lives):
#     lst_1_3.append('_')
#     lives += 1
# while True:
#     if lives == 0:
#         print('You Lose', lst_1_2)
#         break
#     if lst_1_3.count('_') == 0:
#         print('You Win!', lst_1_3)
#         break
#     print('Guess a letter!\n')
#     ch = str(input(''))
#     check(ch)
#     print(str(lst_1_3), '\n', lives)
print('\n', '_' * 100)
# # 2. Write a function that will return the longest word in the random words file from the previous exercise.
# # Գրել ֆունկցիա, որը կվերադարձնի "random_words" ֆայլի ամենաերկար բառը։
lst_2 = []
file = open('random_words.txt', 'r')
for word in file.readlines():
    lst_2.append(word)
file.close()


def lword(lst_2_2):
    max_2 = 0
    c_2 = ''
    for c in lst_2_2:
        if len(c) > max_2:
            max_2 = len(c)
            c_2 = c
    return c_2


print(lword(lst_2), '_' * 100)
# 3. Write a function that will take a string containing the path to a file as an argument and return its size in
# kilobytes.
# Գրել ֆունկցիա, որը կվերցնի սթրինգ արգումենտ։ Սթրինգը պետք է լինի որոշակի ֆայլի path-ը։ Ապա վերադարձնել այդ ֆայլի
# չափսերը կիլոբայթերով։ Հուշում՝ օգտվել os մոդուլից:
path = r"./random_words.txt"
print(os.path.getsize(path) * 1024)
print('_' * 100)


# # 4. Create a random number generator without using random module. The implementation is up to you. You may use
# # current timestamp as a random seed.
# # Գրել ֆունկցիա, որը կվերադարձնի պատահական թիվ։ Պատահական թվերի գեներատոր պարունակող մոդուլ չօգտագործել։ Իմպլեմենտացիան
# # կախված է ձեզնից։ Մտածեք որոշակի ալգորիթմ և ըստ դրա գեներացրեք թիվ։ Կարող եք օգտագործել մեր անցած seed-ի գաղափարը։
def randum():
    today = datetime.today()
    x = today.year + today.month + today.second + today.minute
    return x // (today.year + today.second // 3)


print(randum())  # Ամեն անգամ 1 եմ ստանում
print('_' * 1000)
# # 5. Create a file and put your shopping list in it. The file must start with current day's date.
# # Ստեղծել ֆայլ, որը կպահի ձեր գնումների ցուցակը (ինչ ապրանք։ քանի հատ)։ Ֆայլը պետք է սկսվի տվյալ օրվա ամսաթվով։
mdict_5 = {'karag': 5, 'havi bud': 2}
# gnumner = open('./Gnumner.txt', 'x')  # Եթե ուզում ես ստուգել արդյոք ֆայլը կա արդեն, թե ոչ, ավելի լավ է os մոդուլն
# օգտագործել
# gnumner.close()
gnumner = open('./Gnumner.txt', 'w')
for k, v in mdict_5.items():  # mdict_5.items() պիտի լինի, չէ՞
    gnumner.writelines(f'{k}:{v} hat\n')
gnumner.close()
