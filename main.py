import random
#NOTES - I CAN EXPANED THE FUNCTIONALITY TO MAKING BETS
from art import LOGO,RULES
print(f"Our Game House Rules\n\n{RULES}")
print(LOGO)

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#function - random card generator form the list of cards
def generateCard(cards_list):
    return random.choice(cards_list)
#function that gives computer new cards when needed and calculates sum
def computerTurn(cards_list, pc_cards, pc_sum):
    while pc_sum<=16:
        new_card = generateCard(cards_list)
        pc_cards.append(new_card)
        pc_sum += new_card
    return pc_sum


#gameplay
ongoing_game = True
while ongoing_game:
    #set everything to the starting postions
    player_cards = []
    computer_cards = []
    sum_of_player=0
    sum_of_computer=0

    play = input("Do you want to play Blackjack? Type 'y' or 'n': ").lower()
    if play=='y':
        br = 0
        #generate 2 cards for player, and add to sum
        while (br < 2):
            player_card = generateCard(cards)
            player_cards.append(player_card)
            sum_of_player = sum_of_player + player_card
            br += 1

        #generate a card for PC and add to sum
        computer_card = generateCard(cards)
        sum_of_computer = sum_of_computer + computer_card
        computer_cards.append(computer_card)

    #if user typed n(no) for playing a Blackjack terminate the program
    elif play=='n':
        break
    else:
        print("wrong input!")
        break

    print(f"Your cards: {player_cards}, current score: {sum_of_player}")
    print(f"Computer's first card: {computer_cards}\n")

#trace user to hit or stand and see who wins at the end
    hit_or_stand = True
    while hit_or_stand:
        sum_of_player=21#temporary value for checking
        if sum_of_player==21 or add_cards=='s':
            if sum_of_player==21:
            	print("BLACKJACK!!!")
            new_pc_sum = computerTurn(cards, computer_cards, sum_of_computer)
            print(f"Your final hand: {player_cards}, final score: {sum_of_player}")
            print(f"Computer's final hand: {computer_cards}, final score {new_pc_sum}")
            break
            if sum_of_player==new_pc_sum:
                print('draw')
            break
#todo - upadated hit and stand functionality, see if works
        add_cards = input("Type 'h' to get another cards, type 's' to pass: ").lower()
        if add_cards == 'h':
        	new_card = generateCard(cards)
        	player_cards.append(new_card)
        	sum_of_player += new_card
        	print(f"Your cards: {player_cards}, current score: {sum_of_player}")
        	print(f"Computer's first card: {computer_cards}\n")
        else:
            print('wrong input, try again')
            