import random
import pickle

print("Welcome to Rock, Paper, Scissors!")
def main():
    print("\n1. Start New Game\n2. Load Game\n3. Quit\n")
    menu_choice = input("Enter number of choice: ")
    if menu_choice == str(1):
       new_game()
    elif menu_choice == str(2):
        load_game()  
    elif menu_choice == str(3):
        exit
    else:
        print("That was an invalid choice. Please try again.")
        main()

def new_game():
    user_name = input("\nWhat is your name? ")
    print("\nHello,", user_name + ".", "Let's play!")
    tie = 0
    computer_score = 0
    user_score = 0
    user_stats = [user_name, user_score, computer_score, tie]
    store_stats = open(str(user_name) + '.rps', 'wb')
    pickle.dump(user_stats, store_stats)
    store_stats.close()
    play_game(user_name)

def load_game():
    user_name = input("\nWhat is your name? ")
    try:
        load_stats = open(str(user_name) + '.rps', 'rb')
        pb = pickle.load(load_stats)
        load_stats.close()
        print("\nWelcome back", user_name + ".", "Let's play!")
        play_game(user_name)
    except:
        print(user_name + ",", "your game could not be found.")
        main()

def play_game(user_name):
    load_stats = open(str(user_name) + '.rps', 'rb')
    pb = pickle.load(load_stats)
    user_score = int(pb[1])
    computer_score = int(pb[2])
    tie = int(pb[3])
    round_num = 1 + computer_score + user_score + tie
    load_stats.close()
    print("\nRound", round_num)
    print("\n1. Rock\n2. Paper\n3. Scissors")
    user_choice = int(input("\nEnter number of choice: "))
    choices = [1, 2, 3]
    computer_choice = random.choice(choices)
    if user_choice in choices:
        if user_choice == computer_choice:
            print("Tie")
            tie += 1
        elif user_choice == 1:
            if computer_choice == 2:
                print("\nYou chose rock. The computer chose paper. You lose!")
                computer_score += 1
            elif computer_choice == 3:
                print("\nYou chose rock. The computer chose scissors. You win!")
                user_score += 1
        elif user_choice == 2:
            if computer_choice == 3:
                print("\nYou chose paper. The computer chose scissors. You lose!")
                computer_score += 1
            elif computer_choice == 1:
                print("\nYou chose paper. The computer chose rock. You win!")
                user_score += 1
        else:
            if computer_choice == 1:
                print("\nYou chose scissors. The computer chose rock. You lose!")
                computer_score += 1
            elif computer_choice == 2:
                print("\nYou chose scissors. The computer chose paper. You win!")
                user_score += 1
        round_num += 1
        stats(user_name, user_score, computer_score, tie)
        after_round_menu(user_name, user_score, computer_score, tie)
    else:
        print("\nThat was an invalid choice. Please try again.")
        play_game(user_name)

def stats(user_name, user_score, computer_score, tie):
    user_stats = [user_name, user_score, computer_score, tie]
    store_stats = open(str(user_name) + '.rps', 'wb')
    pickle.dump(user_stats, store_stats)
    store_stats.close()
    
def after_round_menu(user_name, user_score, computer_score, tie):
    print("\nWhat would you like to do?")
    print("\n1. Play Again\n2. View Statistics\n3. Quit")
    after_round_choice = int(input("\nEnter number of choice: "))
    if after_round_choice == 1:
        play_game(user_name)
    elif after_round_choice == 2:
        display_stats(user_name, user_score, computer_score, tie)
    elif after_round_choice == 3:
        end_game(user_name, user_score, computer_score, tie)
    else:
        print("\nThat was an invalid choice. Please try again.")
    
def display_stats(user_name, user_score, computer_score, tie):
    load_stats = open(str(user_name) + '.rps', 'rb')
    pb = pickle.load(load_stats)
    user_score = int(pb[1])
    computer_score = int(pb[2])
    tie = int(pb[3])
    print(user_name + ",", "here are your game play statistics...")
    print("Wins: ", str(user_score))
    print("Losses: ", str(computer_score))
    print("Ties: ", str(tie))
    try:
        win_loss_ratio = user_score / computer_score
        print("\nWin/Loss Ratio: ", str(format(win_loss_ratio, '.2f')))
    except ZeroDivisionError:
        print("\nWin/Loss Ratio: No losses!")
    load_stats.close()
    after_round_menu(user_name, user_score, computer_score, tie)

def end_game(user_name, user_score, computer_score, tie):
    try:
        stats(user_name, user_score, computer_score, tie)
        print(user_name + ",", "your game has been saved.")
        exit
    except Exception as e:
        print("\nSorry", user_name + ",", "the game could not be saved.")
        print(e)

main()
