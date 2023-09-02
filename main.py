import random
maxn = 10
attempts = 0
score = 0
penalty = 1
maxAttempts = 10
n = random.randint(1, maxn)
print('Welcome to guess the number game!')
print('Guess the number from 1 to %d' % maxn)
guess = None

def game():
    global attempts
    if attempts < maxAttempts:
        guess = int(input('Your try: '))
        attempts += 1
        if guess == n:
            print('Congratulations, you won!')
            print('Number of Attempts: ', attempts)
            score = (maxAttempts - attempts + 1) * 10
            print('Final Score: ', score)
            return
        elif guess > n:
            print('Too high')
            remainingAttempts = maxAttempts - attempts;
            score = (remainingAttempts + 1) * 10 - (penalty * (attempts - 1));
            game()
        elif guess < n:
            print('Too low')
            remainingAttempts = maxAttempts - attempts;
            score = (remainingAttempts + 1) * 10 - (penalty * (attempts - 1));
            game()
        else:
            pass
    return 

game()
val = ''
while val.lower() != 'n':
    val = input("Want to Play Again ? Y/N: ")
    if val.lower() == 'y':
        n = random.randint(1, maxn)
        attempts = 0
        score = 0
        game()
    else:
        print("Thanks For Playing!")\
