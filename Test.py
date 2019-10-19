print( str(5) + "  hey")
print(round(3.5))
friends = [34, "hey", 55.8]

print(friends)
friends2 = friends.copy()
friends[0] = 12
print(friends)
print(friends2)

dictionary = {
    "one" : 1,
    "two" : 2,
    "three" : 3
}

print(dictionary["one"])

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

def hi():
    print('cats', 'dogs', 'mice', sep=',')
    return 5


# print('=====================')
# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))
#
# def spam(divideBy):
#     return 42 / divideBy
# try:
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#     print('Error: Invalid argument.')

# # This is a guess the number game.
# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')
# # Ask the player to guess 6 times.
# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input())
#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high.')
#     else:
#         break # This condition is the correct guess!
# if guess == secretNumber:
#     print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))


a = input("Insert somthing")
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotate(grid):
    test = "hi"
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            print(grid[row][col], end="")
        print()

