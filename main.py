import random

from art import LOGO
print(LOGO)

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards = []
sum_of_player = 0
computer_cards = []
sum_of_computer = 0
br=0
while(br<2):
    player_start = random.choice(cards)
    player_cards.append(player_start)
    br+=1

computer_start = random.choice(cards)

computer_cards.append(computer_start)
for card in player_cards:
    sum_of_player = sum_of_player+card

print(f"Your cards: {player_cards}, current score: {sum_of_player}")
print(f"Computer's first card: {computer_start}")

