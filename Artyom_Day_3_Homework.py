"""IF, ELIF, ELSE"""
import random
# 1. Enter your name, then find the sum of the ASCII values of the letters in your name. If that number is larger than
# 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.
name = input('Enter your name: ')
summary = 0
for i in range(0, len(name)):
    summary += ord(name[i])
if summary > 500:
    print('I\'ve got a great name!\n', '█' * 100)
else:
    print('I\'ve got a fancy name!\n', '█' * 100)

# 2. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input is not a string, print "Why are you doing this to me?".

film = input('Enter film name: ')
letter = ord(film[0])
if 65 <= letter <= 90:
    print('Great title!', '\n', '█' * 100)
elif 61 <= letter <= 122:
    print('Title start with capital letters...', '\n', '█' * 100)
else:
    print('Why are you doing this to me?', '\n', '█' * 100)

# 3. Ask the user to input his/her age. If the user is older than 18, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.

age = int(input('Enter your age: '))
if age >= 18:
    print('You\'re eligible to vote.', '\n', '█' * 100)
else:
    print('You\'re not eligible to vote.', '\n', '█' * 100)

# 4. Write a program that will tell us whether a given year is a leap year or not.

year = int(input('Enter year: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Year is leap.', '\n', '█'*100)
        else:
            print('Year isn\'t leap.', '\n', '█'*100)
    else:
        print('Year is leap.', '\n', '█' * 100)
else:
    print('Year isn\'t leap.', '\n', '█' * 100)
# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.

num = int(random.randint(-1000, 1000))
if num >= 0:
    print('Positive', '\n', '█' * 100)
else:
    print('Negative', num*-1, '\n', '█' * 100)
