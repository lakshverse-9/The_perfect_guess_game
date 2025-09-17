import random

a=random.randint(1,10)

print ("Hey! Welcome to the perfect guess game")
print ("The instructions of the game are defined below:")
print ("1)You have to guess a random number between 1 and 10\n2)The number of guesses you will take to guess the actual number will be displayed\n3)The lower the number of guesses ,the higher is your score and vice-versa")


guesses=0


while True:
    b=int(input("Enter your guessed number:"))
    if b<1 or b>10:
        print ("Enter number between 1 and 10 only!")
        continue
    guesses+=1
    
    if b==a:
        print (f"Wow! You guessed it right in {guesses} number of guesses")
        break
    elif b<a:
        print ("Higher number please!")
    elif b>a:
        print ("Lower number please!")
















