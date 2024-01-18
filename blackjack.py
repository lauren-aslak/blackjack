"""The program as a whole runs a game with multiple rounds of blackjack. The user is first asked for a password to access the game. After the password is entered correctly the user is welcomed to the game and prompted to hit or stay (get a new card or end the round). The user is repeatedly asked until either their hand goes over the score of 21 or they choose to stay. If they choose to stay their hand is compared to the dealer's and a winner is decided based off that. After this the user has the option to play again or quit. If the user chooses to quit they will be thanked for playing and are prompted if they would like to see their statistics. Once the statistics are either denied or shown the program ends completely."""

import random
import time
hit_stay = 0
pos_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card = 0
player_total = 0
player_hand = []
phys_cards = []
dealer_total = 0
#possible dealer totals are adjusted for real life probabilities
pos_dealer_totals = [17, 18, 18, 19, 19, 20, 21]
restart = 0
win_streak_count = 0
highest_streak = 0
black_jack_counter = 0
win_counter = 0
game_counter = 0

def password_check(PASSWORD):
    """Limits user to six attempts to enter password correctly by using a while loop. If user reaches limit program ends without running anything else after function is called."""
    
    print('Password Authentication Program\n')
    attempts = 0
    
    while attempts < 6:
        user_pass = input('Enter your password: ')
        
        if user_pass == PASSWORD:
            print('Correct password! Access granted.')
            return
        else:
            attempts = attempts + 1
            print('Incorrect password. Please try again.\n')
            
    print('Incorrect password. Maximum number of attempts reached. Access denied.')
    #in other environments gives user 10 seconds to view statement and then exit() kicks in
    time.sleep(10)
    exit()

def ascii_card(card):
    """works in conjuction with phys_card and player_hand lists to print out a playing card"""
    
    if card == 1:
        print(""" ---------
| A       |
|         |
|         |
|       A |
 ---------""")
    elif card == 100:
        print(""" ---------
| A       |
|         |
|         |
|       A |
 ---------""")
    elif card == 2:
        print(""" ---------
| 2       |
|         |
|         |
|       2 |
 ---------""")
    elif card == 3:
        print(""" ---------
| 3       |
|         |
|         |
|       3 |
 ---------""")
    elif card == 4:
        print(""" ---------
| 4       |
|         |
|         |
|       4 |   
 ---------""")
    elif card == 5:
        print(""" ---------
| 5       |
|         |
|         |
|       5 |   
 ---------""")
    elif card == 6:
        print(""" ---------
| 6       |
|         |
|         |
|       6 |   
 ---------""")
    elif card == 7:
        print(""" ---------
| 7       |
|         |
|         |
|       7 |   
 ---------""")
    elif card == 8:
        print(""" ---------
| 8       |
|         |
|         |
|       8 |   
 ---------""")
    elif card == 9:
        print(""" ---------
| 9       |
|         |
|         |
|       9 |   
 ---------""")
    elif card == 10:
        print(""" ---------
| 10      |
|         |
|         |
|      10 |   
 ---------""")
    elif card == 11:
        print(""" ---------
| J       |
|         |
|         |
|       J |   
 ---------""")
    elif card == 12:
        print(""" ---------
| Q       |
|         |
|         |
|       Q |   
 ---------""")
    elif card == 13:
        print(""" ---------
| K       |
|         |
|         |
|       K |   
 ---------""")

def new_card():
    global player_total
    global player_hand
    global pos_cards
    global card
    global phys_cards
    global temp_card
    """Prints all previous cards and new card, adds new card to player_hand list. Sum of player's hand is also calculated."""
    
    card = random.choice(pos_cards)
    if card > 10:
        #only for jacks, queens, kings
        temp_card = 10
        player_hand.append(temp_card)
        phys_cards.append(card)
    elif card == 1:
        #only for aces
        ace_value = int(input('Your next card is an ace, would you like it to be worth 1 or 11: '))
        card = ace_value
        player_hand.append(card)
        if card == 11:
            phys_cards.append(100)
            #100 represents the ace ascii graphic that goes along with an ace value of 11
            card = 14
        elif card == 1:
            phys_cards.append(card)
    else:
        player_hand.append(card)
        phys_cards.append(card)
    
    #displaying physical cards
    for i in range(len(player_hand)):
        #only jacks, queens, and kings should pass through first if statement
        if player_hand[i] == 10 and 14 > phys_cards[i] > 10:
            ascii_card(phys_cards[i])
        #only aces should pass through second if statement
        elif phys_cards[i] == 1 or phys_cards[i] == 100:
            ascii_card(phys_cards[i])
        else:
            ascii_card(player_hand[i])
    
    #finding total of player's hand
    if card == 11 or card == 12 or card == 13:
        #only for jacks, queens, kings
        player_total = player_total + temp_card
    elif card == 14:
        #only for aces with a value of 11
        player_total = player_total + 11
    else:
        player_total = player_total + card

def hit_or_stay():
    global hit_stay
    """While true loop allows program to ask the user for hit_stay input until the input is an integer, user input will be used to trigger either giving a new card or ending the round."""
    
    while True:
        try:
            hit_stay = int(input('1 to hit, 2 to stay: '))
        except ValueError or TypeError:
            print('Not a valid input. Please enter 1 or 2.')
        else:
            break

def restart_game():
    global restart
    """While true loop allows program to ask the user for restart input until the input is an integer, user input will be used to trigger either the start of a new round or end of the game."""
    
    while True:
        try:
            restart = int(input('1 to play again, 2 to quit: '))
        except ValueError or TypeError:
            print('Not a valid input. Please enter 1 or 2.')
        else:
            break

def reset():
    """resets all values that are changed during the game so code is able to be reused for next game"""
    
    global player_total
    global player_hand
    global restart
    global phys_cards
    restart = 0
    player_total = 0
    player_hand = []
    phys_cards = []

def win_streak(win_lose):
    global win_streak_count
    global highest_streak
    """Tracks number of games the user has played and how many of those they have won. This data is used for the stats shown at the end of the game."""
    
    if win_lose == 'win':
        win_streak_count = win_streak_count + 1
        print('Win Streak:', win_streak_count, '\n')
        #checks every time if highest streak has been broken
        if win_streak_count > highest_streak:
            highest_streak = win_streak_count
    else:
        win_streak_count = 0
        print('Win Streak:', win_streak_count, '\n')

def stay():
    global restart
    global black_jack_counter
    global win_counter
    global game_counter
    """At the end of each round function compares player and dealer totals to identify a winner."""
    
    if player_total > 21:
        print('\nBust! You lose.')
        win_streak('lose')
        restart_game()
        game_counter = game_counter + 1
    
    elif player_total == 21:
        print('\nBlack Jack! You win.')
        win_streak('win')
        restart_game()
        black_jack_counter = black_jack_counter + 1
        game_counter = game_counter + 1
        win_counter = win_counter + 1
    
    else:
        dealer_total = random.choice(pos_dealer_totals)
        print('\nDealer total:', dealer_total, '\nYour total:', player_total)
        game_counter = game_counter + 1
        
        if player_total >= dealer_total:
            print('\nYou win!')
            win_streak('win')
            restart_game()
            win_counter = win_counter + 1
        else:
            print('\nYou lose!')
            win_streak('lose')
            restart_game()

def player_stats():
    global win_counter
    global game_counter
    win_percent = (win_counter/game_counter)*100
    """If chose by the user function will print statistics including number of games played, win percentage, highest win streak, and number of blackjacks."""
    
    while True:
        try:
            stats = int(input('Press 1 to see your stats, 2 to quit: '))
        except ValueError or TypeError:
            print('Not a valid input. Please enter 1 or 2.')
        else:
            break
    
    if stats == 1:
        #uses if statements to implement proper grammar
        if black_jack_counter == 1 and game_counter == 1:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('\nYou played', game_counter, 'game\nYou won '+ str(format(win_percent, '.1f')) + '% of your games\nYour highest win streak was', highest_streak,'\nYou had', black_jack_counter, 'blackjack\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif black_jack_counter == 1:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('\nYou played', game_counter, 'games\nYou won '+ str(format(win_percent, '.1f')) + '% of your games\nYour highest win streak was', highest_streak,'\nYou had', black_jack_counter, 'blackjack\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif game_counter == 1:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('\nYou played', game_counter, 'game\nYou won '+ str(format(win_percent, '.1f')) + '% of your games\nYour highest win streak was', highest_streak,'\nYou had', black_jack_counter, 'blackjacks\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('\nYou played', game_counter, 'games\nYou won '+ str(format(win_percent, '.1f')) + '% of your games\nYour highest win streak was', highest_streak,'\nYou had', black_jack_counter, 'blackjacks\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def main():
    global player_total
    global restart
    global highest_streak
    global game_counter
    global hit_stay
    """Begins with a password authentication, then moves onto using a while true loop to call the function hit_or_stay which is the driving function for the program. To break the while true loop user must input 2 to the restart prompt."""
    
    PASSWORD = 'python23'
    password_check(PASSWORD)
    print('\n~~~Welcome to Blackjack~~~\n')
    while True:
        hit_or_stay()
        if hit_stay == 1:
            new_card()
            print('Your total:', player_total)
        elif hit_stay == 2:
            stay()
        
        #continuously checks after every new card is played
        if player_total > 21:
            game_counter = game_counter + 1
            print('\nBust! You lose.')
            win_streak('lose')
            restart_game()
            
        if restart == 2:
            print('\nThank you for playing!\n')
            player_stats()
            break
        if restart == 1:
            reset()




main()