import random

# Function to create a deck of cards
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card, suit in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            ace_count += 1
            value += 11
        else:
            value += int(card)
    
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    
    return value

# Function to display the hand
def display_hand(hand, player_name):
    print(f"{player_name}'s hand: {', '.join([f'{card} of {suit}' for card, suit in hand])}")

# Function to check for blackjack
def check_blackjack(hand):
    return calculate_hand_value(hand) == 21

# Function to play the game
def play_blackjack():
    deck = create_deck()
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    # Check for initial blackjack
    if check_blackjack(player_hand):
        display_hand(player_hand, 'Player')
        print("Player has a blackjack! Player wins!")
        return
    if check_blackjack(dealer_hand):
        display_hand(dealer_hand, 'Dealer')
        print("Dealer has a blackjack! Dealer wins!")
        return
    
    # Player's turn
    while True:
        display_hand(player_hand, 'Player')
        player_value = calculate_hand_value(player_hand)
        print(f"Player's hand value: {player_value}")
        
        if player_value > 21:
            print("Player busts! Dealer wins.")
            return
        
        action = input("Do you want to (h)it or (s)tand? ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")
    
    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    display_hand(dealer_hand, 'Dealer')
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Dealer's hand value: {dealer_value}")
    
    if dealer_value > 21:
        print("Dealer busts! Player wins.")
    elif dealer_value > player_value:
        print("Dealer wins.")
    elif dealer_value < player_value:
        print("Player wins.")
    else:
        print("It's a tie!")

# Play the game
if __name__ == "__main__":
    play_blackjack()
    

# Main game loop
def main():
    while True:
        play_blackjack()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()