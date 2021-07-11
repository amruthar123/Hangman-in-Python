from random import randint, choice
turns = 10
word_list = ['python', 'java', 'cpp', 'javascript', 'hello', 'world']
s = choice(word_list)
guessed = ''
while True:
    print('\nYou have ', turns, ' turns left')
    turns =turns -1
    char = input('Your guess : ')
    if char in s:
        guessed += char
    remaining_letters = 0
    for i in s:
        if i in guessed:
            print(i, end='')
        else:
            remaining_letters += 1
            print('*', end='')
    if remaining_letters == 0:
        print('\nYayyy!!! You won')
        break
        
    if turns == 0:
        print('\nYou lose')
        break