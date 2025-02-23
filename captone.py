import random
attempts_list=[]
def show_score():
    if len (attempts_list) <= 0:
        print('Ther is no high score at the moment')
    else:
        print('the current high score is {} attemps'.format((attempts_list)))  
def start_game():
    random_number = int(random.randint(1,10))  
    print('Welcome to the game')
    player_name=input('Enter your name to start the game')
    Wanna_play= input('Do you wanna play now,{}? Enter Yes/No'.format(player_name))
    attempts = 0
    show_score()
    while Wanna_play.lower()=='yes':
        try:
            guess = int(input("pick a number between 1 and 10"))
            if int(guess) < 1 or  int(guess)> 10:
                raise ValueError('Please guess a number in range of 1 to 10')
            elif int(guess) == random_number:
                print('Congarts!,you got it!')
                attemtps=+1
                attempts_list.append(attemtps)
                print('it toke you{}attempts'.format(attemtps))
        
                play_again = input('Would you like to retry')   
                if play_again.lower() == 'no':
                    print('its okay, have a sigma day')
                    break
                else :
                    attempts =0
                    random_number =random.randint(1,10)
                    show_score()
             
            elif guess > random_number:
                 print('Its lower')
                 attempts =-1
        
            elif guess < random_number:
                print('Its higher') 
                attempts =+1
        except ValueError:
            print('thats not a valid value try again') 
            
# if __name__ == '__nain__':
start_game()                  