"""RECURSION"""

import string
# 1. Write a recursive function to calculate the sum of reciprocals of powers of 2. Try increasing the n and see the
# magic.
# Գրել ռեկուրսիվ ֆունկցիա, որը կհաշվի երկրաչափական գումարը, որտեղ r = 1 / 2 է։ Փորձեք բացրձրացնել n-ի արժեքը հետաքրքիր
# արդյունք ստանալու համար։

def rp(n_1, a_1, r_1):
    if n_1 == 0:
        return 1
    return a_1 + rp(n_1-1, a_1, r_1) * r_1
print (rp(2, 1, 0.5))
# 2. Write a recursive function to calculate n-th power of a.
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կհաշվի a-ի n աստիճանը։
def pw(a, n):
    if n == 0:
        return 1
    return a * pw(a, n - 1)


print(pw(5, 3))
# 3. Write a recursive function that evaluates a mathematical expression. Example input - "5 + 6"
# Գրել ռեկուրսիվ ֆունկցիա, որը կհաշվի մաթեմատիկական արտահայտություն փոխանցված սթրինգի միջոցով։ Օրինակ՝ "5 + 6"

# 4. Write a recursive function that reverses a string
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կշրջի և կվերադարձնի փոխանցված սթրինգը։
# str_4_2 = ""
# def rev(str_4):
#     if not str_4:
#         return ''
#     return str_4_2 + str(list(str_4).pop(-1)) + rev(str_4)
# print(rev("lakiaon"))
# 5. Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved
# to the end of the string.
# Գրել ռեկուրսիվ ֆունկցիա, որը որպես արգումենտ կվերցնի սթրինգ և կվերադարձնի նոր սթրինգ, որտեղ օրիգինալ սթրինգում գտնվող
# բոլոր x-երը տեղափոխվել են սթրինգի ամենավերջը։

# """OLD STUFF"""

# 6. Write a function that sorts a list in ascending. Additionally, the function may take a keyword argument that will
# reverse the sort (without recursion is fine).
# Գրել ֆունկցիա, որը կսորտավորի դրան փոխանցված լիստը աճման կարգով։
# Կարելի է ֆունկցիային նաև ավելացնել kwarg, որը փոփոխելիս
# կկարողանանք լիստը սորտավորել նաև նվազման կարգով։
# def srt(lst_6):
#     for x in range(1, len(lst_6)):
#         if lst_6[x] < lst_6[x-1]:
#             t = lst_6[x]
#             lst_6 = list(lst_6[0:x]) + list(lst_6[x+1:-1]) + list(lst_6[-1])
#             for y in range(1, len(lst_6)):
#                 if t < lst_6[y] and t > lst_6[y-1]:
#                     lst_6 = list(lst_6[0:y]) + [t] + list(lst_6[y+1: -1]) + list(lst_6[-1])
#     return lst_6
# print(srt([5, 2, 3]))
# ays xndiry error e berum im mot, sxals chem gtnum
# 7. Write a function that will take 4 arguments. First two are tuples and represent 2D coordinates of two circles.
# The others are the radii of our circles. The function must tell us whether one of the circles is inside the other, or
# do circles intersect, or are they far apart.
# Գրել ֆունկցիա, որը կվերցնի 4 արգումենտ։ Առաջին երկուսը tuple են, որոնք իրենցից ներկայացնելու են 2-չափ տարածության մեջ
# շրջանագծերի կենտրոնների կոորդինատներ։ Մյուս երկուսը լինելու են integer տիպի և ներկայացնելու են վերոնշյալ շրջանագծերի
# շառավիղները։ Ֆունկցիան պետք է տպի արդյո՞ք օղակները հատվում են, կամ մեկը մյուսի մեջ է, կամ իրարից հեռու են։
#ays xndri hamar matemi inch vor banadzeva petq imanal vory es chgitem, interentum el chem karoxanum gtnel
# """OPTIONAL"""

# 8. Write a program to combine two dictionaries adding values for common keys.
# Գրել ծրագիր, որը կմիացնի երկու dictionary։ Համընկնող բանալիների արժեքները պետք է գումարվեն։
dict_8_1 = {5:6, 7:8, 10:21}
dict_8_2 = {7:3, 3:6, 5:10}
dict_8_3 = {}
for k, v in dict_8_1.items():
    for k2, v2 in dict_8_2.items():
        if k == k2:
            dict_8_3.update({k:v+v2})
        else:
            dict_8_3.update({k2: v2})
print(dict_8_3)
#es xndirnel sxala ashxatum chem gtnum inchna sxals
# 9. Write a program to create a dictionary from a string. The letters are the keys and the values are the counts of
# the corresponding letters.
# Սթրինգից ստեղծել dictionary: Սթրինգի տառերը հանդես են գալու որպես բանալիներ, իսկ սթրինգում դրանց քանակը որպես արժեքներ
str_9 = 'tacocat'
dict_9={}
count = 0
for x in str_9:
    for y in str_9:
        if y == x:
            count+= 1
    dict_9.update({x:count})
    count = 0
print(dict_9)