import random
play = True
num = str(random.randint(1,20))
print('A number between 1 to 20 will be generated, you, have to guess it')
print('The game ends when you guess correctly')

while play:
    guess = input('Give your guess')
    if num == guess:
        print('Congratulations you won!') 
        print('the number was : ', num)
        break
    else:
        print('Try again')   