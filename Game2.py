import random

words_list = ('road', 'fuel', 'UFO', 'Plane', 'Lib', 'Olimpic', 'Winter', 'Palm')

secret_word = random.choice(words_list)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

# gamer_word[2] = 'b'
# print(''.join(gamer_word))

while True:
    letter = input("Insert a letter: ")
    if len(letter) != 1 or not letter.isalpha():
        print('Try again')
        continue

    print('Your letter: ', letter)

print('play again!')

#My First commit

#Test new feature