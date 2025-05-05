# Tricksy Battle: Card Game

# Import necessary libraries
import random

# User selects to  start new game or read the rules
def start_game():
    print("1. Start New Game")
    print("2. Ask for help")
    choice = input("Please select an option (1 or 2): ")
    if choice == "1":
        print("Starting a new game...")
        # Call function to start a new game
    elif choice == "2":
        print("Refer to the README file for the rules of the game or how to run the code.")
        # Call function to read the rules
    else:
        print("Invalid selection. Please try again.")


# Function to start a new game
def new_game():
    print("Starting a new game...")
    # Call function to deal cards
    # Computer vs. Player

# Function to deal cards
def deal_cards():
    print("Dealing cards...")
    # Create a deck of cards with the Kings removed (48 cards)

# Function to start round
def play_round(cards):
    print("Starting round...")
    # Random player chosen to go first
    if player_turn == "Player 1":
        print("Player 1 plays.")
    else:
        print("Player 2 plays.")
    
    print(player_turn, ": Are you ready to see your hand?")
    # Show player their hand
    input("Press enter to see your hand.")
    print("Your hand:", player_one_hand if player_turn == "Player 1" else player_two_hand)

    player_one_play = ""
    player_two_play = ""
    if player_turn == "Player 1":
        player_one_play = input("Player 1 select a card to play (for example, 7♣ or 11♢): ")
        print("Player 1 plays:", player_one_play)
        # Remove the card from Player 1's hand
        player_one_hand.remove(player_one_play)
        print("Player 2: Are you ready to see your hand?")
        input("Press enter to see your hand.")
        print("Your hand:", player_two_hand)
        player_two_play = input("Player 2 select a card to play (for example, 7♣ or 11♢): ")
        print("Player 2 plays:", player_two_play)
        # Remove the card from Player 2's hand
        player_two_hand.remove(player_two_play)

        if player_one_play[-1] != player_two_play[-1]:
            print("Player 1 wins the round!")
            player_one_points += 1
            player_turn = "Player 1"
        else:
            if player_one_play[:-1] > player_two_play[:-1]:
                print("Player 1 wins the round!")
                player_one_points += 1
                player_turn = "Player 1"
            else:
                print("Player 2 wins the round!")
                player_two_points += 1
                player_turn = "Player 2"


    else: 
        player_two_play = input("Player 2 select a card to play (for example, 7♣ or 11♢): ")
        print("Player 2 plays:", player_two_play)
        # Remove the card from Player 2's hand
        player_two_hand.remove(player_two_play)
        print("Player 1: Are you ready to see your hand?")
        input("Press enter to see your hand.")
        print("Your hand:", player_one_hand)
        player_one_play = input("Player 1 select a card to play (for example, 7♣ or 11♢): ")
        print("Player 1 plays:", player_one_play)
        # Remove the card from Player 1's hand
        player_one_hand.remove(player_one_play)

        if player_one_play[-1] != player_two_play[-1]:
            print("Player 2 wins the round!")
            player_two_points += 1
            player_turn = "Player 2"
        else:
            if player_one_play[:-1] > player_two_play[:-1]:
                print("Player 1 wins the round!")
                player_one_points += 1
                player_turn = "Player 1"
            else:
                print("Player 2 wins the round!")
                player_two_points += 1
                player_turn = "Player 2"

    # Removed card from the deck
    removed_card = cards[0]
    # Remove one card from the deck
    del cards[0]
    # Show the card that was removed
    print("Removed card:", removed_card)

    # Count players cards
    if times_happened < 2:
        if len(player_one_hand) <= 4 and len(player_two_hand) <= 4:
            # Deal 4 cards to each player
            player_one_hand = cards[:4]
            player_two_hand = cards[4:8]
            # Remove the dealt cards from the deck
            del cards[:8]
            times_happened += 1



    # If one player reaches 9 points and the other player has at least 1 point, end the game
    if player_one_points == 9 and player_two_points >= 1:
        print("Player 1 wins! Ending the game...")
        return True
    elif player_two_points == 9 and player_one_points >= 1:
        print("Player 2 wins! Ending the game...")
        return True
    return False

def main():
    player_one_points = 0
    player_two_points = 0
    print("Welcome to Tricksy Battle!")
    start_game()
    new_game()
    deal_cards()
    cards = ["1♡", "2♡", "3♡", "4♡", "5♡", "6♡", "7♡", "8♡", "9♡", "10♡", "11♡", "12♡", "1♢", "2♢", "3♢", "4♢", "5♢", "6♢", "7♢", "8♢", "9♢", "10♢", "11♢", "12♢", "1♣",
"2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "11♣", "12♣", "1♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "11♠", "12♠",]
    random.shuffle(cards)
    player_one_hand = cards[:8]
    player_two_hand = cards[8:16]
    del cards[:16]
    player = ("Player 1", "Player 2")
    player_turn = random.choice(player)
    print (player_turn, "goes first.")
    times_happened = 0
    

# End game after 16 rounds
    end = False
    for _ in range (16):
        end = play_round(cards)
        if end:
            break

    # If the game ends 16 to 0, the player with zero points has “shot the moon”, and immediately scores 17 points
    if player_one_points == 0 and player_two_points == 16:
        print("Player has shot the moon! Player scores 17 points.")
        player_one_points += 17
    elif player_two_points == 0 and player_one_points == 16:
        print("Player has shot the moon! Player scores 17 points.")
        player_two_points += 17


    # If the game ends in a tie, show final points and ask if players want to play again
    if player_one_points == player_two_points:
        print("The game ends in a tie!")


    # If the game ends with one player winning, show final points and ask if players want to play again
    if player_one_points > player_two_points:
        print("Player 1 wins the game!")
        # Show final points
        print("Player 1 points:", player_one_points)
        print("Player 2 points:", player_two_points)
    elif player_two_points > player_one_points:
        print("Player 2 wins the game!")
        # Show final points
        print("Player 1 points:", player_one_points)
        print("Player 2 points:", player_two_points)


# Ask if players want to play again?
    # play_again = input("Do you want to play again? (yes or no): ")
    # if play_again.lower() == "yes":
        # start_game()
    # else:
        # print("Thank you for playing Tricksy Battle!")
        # exit()
