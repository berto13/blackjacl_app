#BlackJack_App


import random

initialCards = []
dealerCards = []
playerCards = []

for i in range(2):
    card = random.randint(2, 11)
    initialCards.append(card)

class BJApp:

    def __init__(self, dealer_card1, dealer_card2, player_card1, player_card2):
        dealerCards.append(dealer_card1, dealer_card2)
        playerCards.append(player_card1, player_card2)

    def dealer_cards_func(self):
        total_dealer = sum(self.dealerCards)
        print('Dealer cards:', '?', self.dealerCards[1])
        return self.dealerCards, total_dealer

    def player_cards_func(self):
        check_for_ace = 0

        if 11 in self.playerCards:
            check_for_ace = 1
        total_value = sum(self.playerCards)
        if total_value > 21 & check_for_ace == 1:
            for c in range(len(self.playerCards)):
                if self.playerCards[c] == 11:
                    self.playerCards[c] = 1
        total_value = sum(self.playerCards)
        print(self.playerCards)
        print(total_value)
        return self.playerCards, total_value


card_shuffle = BJApp(initialCards[0], initialCards[1], initialCards[2], initialCards[3])

dealer_shuffle, total = dealer_cards_func(dealer)
player_shuffle, ply_total = player_cards_func()
if ply_total > 21:
    print('Bust')
    
while ply_total < 21:
    ask_player = str(input('Do you want another card (Y/N):'))
    if ask_player == 'Y':
        card = random.randint(2,11)
        player_shuffle.append(card)
        ply_total = sum(player_shuffle)
    elif ask_player == 'N':
        break
    print(ply_total)
    if ply_total > 21:
        print('Bust')


print(dealer_shuffle)
print(total)

if ply_total > 21:
    print('Dealer won!')
elif total > ply_total:
    print('Dealer won!')
elif total == ply_total:
    print('It was a draw.')
else :
    print('You won!')




