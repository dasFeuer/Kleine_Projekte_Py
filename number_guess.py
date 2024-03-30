import random

num = random.randint (1, 100)
guess = 0
print ("If you want to quit the game then TYPE: 404 and enter.")
while guess != num:
    guess = int(input("Guess the number betweem 1 to 100: "))
    if (guess == num):
        print ("Congratulation! you have guess the right number")
        print ("You haved guessed", guess,"and the answer was also", num )
        break
    elif ( guess > num):
        print ("Try again, think of lower number")
        
    elif (guess < num):
        print("Try again, think of higher number")
    
else:
    while True:
        if guess == 404:
            print("You have quit the game. Thank you for playing.")
            break

   
        

     