import random
from collections import Counter

words = '''tiger lion giraffe elephant
    zebra deer bear monkey gorilla leopard'''

words = words.split(' ')

word = random.choice(words)

if __name__ =='__main__':
    print("Guess the word! HINT: Word is a name of wild animals")

    for i in word:
        print("_", end='')
    print()

    play = True
    letterGuessed = ''
    attempts = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (attempts != 0) and flag == 0:
            print()
            attempts -=1
            
            try:
                guess = str(input("Enter a letter to guess: "))
            except: 
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print("Enter only a Single Letter")
            elif guess in letterGuessed:
                print("You have already guessed that letter")
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print("The word is: ", end='')
                    print(word)
                    flag = 1
                    print('Congratulation, You won!')
                    break
                    break
                else:
                    print('_', end='')

            if attempts <= 0 and (Counter(letterGuessed) != Counter(word)):
                print()
                print('You lost! Try again..')
                print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()

