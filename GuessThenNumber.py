import random 
n = random.randint(1,9)
guess = int(input('Guess a number within 1 to 9:'))
print(f'The number was',n)
if guess == n:
    print('Number matched')
else:
    print('Try again')
    