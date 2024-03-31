import random
name = input("What is your name? \n")

print ("Wish you all the very best!", name)

words = ['computer', 'laptop', 'python',
         'processer', 'network', 'compiler',
         'maths', 'programmer', 'lifestyle',
         'confidence', 'connections', 'money']

words = random.choice(words)

print ("Guess the characters\n")

guesses = ''

turns = 12

while turns > 0:
    failed = 0

    for char in words:

        if char in guesses:
            print (char, end="")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print ("You win")
        print ("The word is:", words)
        break

    print() 
    guess = input ("Guess a character:")
    guesses += guess

    if guess not in words:

        turns -= 1

        print ("Wrong")

        print ("You have", + turns, 'more guesses')

        if turns == 0:
            print ("You Loose")

