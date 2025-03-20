import random
# NOTES - I CAN EXPANED THE FUNCTIONALITY TO MAKING BETS
from art import LOGO, RULES

print(f"Our Game House Rules\n\n{RULES}")
print(LOGO)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# function - random card generator form the list of cards
def generateCard(cards_list):
    return random.choice(cards_list)


# Function to handle ace conversion for both player and computer
def handle_ace(cards_list, total_sum):
    """
    Check if there are any aces (11) in the cards list and convert them to 1 if needed to avoid busting.
    Returns the new sum after any necessary conversions.
    """
    # Make a copy of the list to avoid modifying the original directly during iteration
    for i in range(len(cards_list)):
        # If sum is over 21 and there's an ace (11) in the hand, convert it to 1
        if total_sum > 21 and cards_list[i] == 11:
            cards_list[i] = 1
            total_sum -= 10
    return total_sum


# function that gives computer new cards when needed and calculates sum
def computerTurn(cards_list, pc_cards, pc_sum):
    while pc_sum <= 16:
        new_card = generateCard(cards_list)
        pc_cards.append(new_card)
        pc_sum += new_card
        # Handle ace conversion for computer
        pc_sum = handle_ace(pc_cards, pc_sum)
    return pc_sum

# gameplay
ongoing_game = True
while ongoing_game:
    # set everything to the starting postions
    player_cards = []
    computer_cards = []
    sum_of_player = 0
    sum_of_computer = 0

    # Continuously ask for input until valid
    while True:
        play = input("Do you want to play Blackjack? Type 'y' or 'n': ").lower()
        if play == 'y':
            br = 0
            # generate 2 cards for player, and add to sum
            while (br < 2):
                player_card = generateCard(cards)
                player_cards.append(player_card)
                sum_of_player = sum_of_player + player_card
                br += 1

            # generate a card for PC and add to sum
            computer_card = generateCard(cards)
            sum_of_computer = sum_of_computer + computer_card
            computer_cards.append(computer_card)
            break  # Exit the input loop and continue with the game
        elif play == 'n':
            ongoing_game = False
            break  # Exit the input loop
        else:
            print("Wrong input! Please type 'y' or 'n'.")
            # Loop continues to ask again

    # If user chose not to play, break out of the main game loop
    if not ongoing_game:
        break

    print(f"Your cards: {player_cards}, current score: {sum_of_player}")
    print(f"Computer's first card: {computer_cards}\n")

    # trace user to hit or stand and see who wins at the end
    hit_or_stand = True
    while hit_or_stand:
            # sum_of_player = 21  # temporary value for checking
        if sum_of_player == 21:
            if sum_of_player == 21:
                print("BLACKJACK!!!")
            new_pc_sum = computerTurn(cards, computer_cards, sum_of_computer)
            print(f"Your final hand: {player_cards}, final score: {sum_of_player}")
            print(f"Computer's final hand: {computer_cards}, final score {new_pc_sum}")
            if sum_of_player < new_pc_sum and new_pc_sum<=21:
                print('You lose! :(')
            elif sum_of_player > new_pc_sum or new_pc_sum>21:
                print('You win!!!! :)')
            elif sum_of_player == new_pc_sum:
                print('Draw')
            break
        add_cards = input("Type 'h' to get another cards, type 's' to pass: ").lower()
        if add_cards=='h':
            new_card = generateCard(cards)
            player_cards.append(new_card)
            sum_of_player += new_card
            #switch 11 to 1 when needed
            for card in player_cards:
                if sum_of_player> 21 and card==11:
                    index = player_cards.index(card)
                    player_cards[index]= 1
                    sum_of_player-=10

            print(f"Your cards: {player_cards}, current score: {sum_of_player}")
            print(f"Computer's first card: {computer_cards}\n")
            if sum_of_player>21:
                print(f"Your final hand: {player_cards}, final score: {sum_of_player}")
                print(f"Computer's final hand: {computer_cards}, final score {sum_of_computer}")
                print('You went over , you lose.')
                break
        elif add_cards=='s':
            new_pc_sum = computerTurn(cards, computer_cards, sum_of_computer)
            print(f"Your final hand: {player_cards}, final score: {sum_of_player}")
            print(f"Computer's final hand: {computer_cards}, final score {new_pc_sum}")
            if sum_of_player < new_pc_sum and new_pc_sum <= 21:
                print('You lose! :(')
            elif sum_of_player > new_pc_sum or new_pc_sum > 21:
                print('You win')
            elif sum_of_player == new_pc_sum:
                print('Draw')
            break
        else:
            print('Wrong input, try again!')