# Tricksy Battle: Card Game

# Inclusion of ADVANCED TOPICS: Add usage of random module
import random
# Inclusion of ADVANCED TOPICS: Time of steps
import time
# Inclusion of ADVANCED TOPICS: Use of pandas and seaborn
import pandas as pd
import seaborn as sns

# Define variables
player_one_points = 0
player_two_points = 0
cards = ["1♡", "2♡", "3♡", "4♡", "5♡", "6♡", "7♡", "8♡", "9♡", "10♡", "11♡", "12♡", "1♢", "2♢", "3♢", "4♢", "5♢", "6♢", "7♢", "8♢", "9♢", "10♢", "11♢", "12♢", "1♣",
"2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "11♣", "12♣", "1♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "11♠", "12♠"]
player = ("Player 1", "Player 2")
times_happened = 0

# Print welcome to player/players
print("Welcome to Tricksy Battle!")

# User selects to  start new game or read the rules
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

# Function to deal cards
def deal_cards():
    print("Dealing cards...")
    # Create a deck of cards with the Kings removed (48 cards)
cards = ["1♡", "2♡", "3♡", "4♡", "5♡", "6♡", "7♡", "8♡", "9♡", "10♡", "11♡", "12♡", "1♢", "2♢", "3♢", "4♢", "5♢", "6♢", "7♢", "8♢", "9♢", "10♢", "11♢", "12♢", "1♣",
"2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "11♣", "12♣", "1♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "11♠", "12♠",]

# Shuffle the deck
random.shuffle(cards)

# Deal 8 cards to each player
player_one_hand = cards[:8]
player_two_hand = cards[8:16]


# Remove the dealt cards from the deck
del cards[:16]

# Randomly determine which player goes first
player = ("Player 1", "Player 2")
player_turn = random.choice(player)

times_happened = 0

# Starting round
# Random player chosen to go first
if player_turn == "Player 1":
    print("Player 1 plays first.")
else:
    print("Player 2 plays first.")
    
print(player_turn, ": Are you ready to see your hand?")
# Show player their hand
input("Press enter to see your hand.")
print("Your hand:", player_one_hand if player_turn == "Player 1" else player_two_hand)

player_one_play = ""
player_two_play = ""


# Play a round
def play_round():
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

        # Print the time taken for Player 1 or 2 to play
        def time_taken():
            start_time = time.time()
            # Simulate the time taken for Player 1 or 2 to play
            time.sleep(2)  # Simulate a delay of 2 seconds
            end_time = time.time()
            print("Time taken:", end_time - start_time, "seconds")
        # Call the function to measure time taken
        time_taken()


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

        # Print the time taken for Player 1 or 2 to play
        def time_taken():
            start_time = time.time()
            # Simulate the time taken for Player 1 or 2 to play
            time.sleep(2)  # Simulate a delay of 2 seconds
            end_time = time.time()
            print("Time taken:", end_time - start_time, "seconds")
        # Call the function to measure time taken
        time_taken()    
                
    # Removed card from the deck
    removed_card = cards[0]
    # Remove one card from the deck
    del cards[0]
    # Show the card that was removed
    print("Removed card:", removed_card)

    # Winner of the round leads the next round
    if player_two_play > player_one_play:
        player_turn = "Player 2 leads the next round."
    else:
        player_turn = "Player 1 leads the next round."
    print(player_turn)

# Count players cards
if times_happened < 2:
    if len(player_one_hand) <= 4 and len(player_two_hand) <= 4:
        # Deal 4 cards to each player
        player_one_hand = cards[:4]
        player_two_hand = cards[4:8]
        # Remove the dealt cards from the deck
        del cards[:8]
        times_happened += 1

    # If a player reaches 9 points, they win the game.        
    if player_one_points == 9 and player_two_points >= 1:
        print("Player 1 wins! Ending the game...")
        end = True
    elif player_two_points == 9 and player_one_points >= 1:
        print("Player 2 wins! Ending the game...")
        end = True

    # If the game ends 16 to 0, the player with zero points has “shot the moon”, and immediately scores 17 points
    if player_one_points == 0 and player_two_points == 16:
        print("Player has shot the moon! Player scores 17 points.")
        player_one_points += 17
    elif player_two_points == 0 and player_one_points == 16:
        print("Player has shot the moon! Player scores 17 points.")
        player_two_points += 17


# End game after 16 rounds
end = False
while not end:
    # End after 16 rounds
    if times_happened == 16:
        end = True
        print("Game over! Ending the game...")

# Print final points and establish winner.
print("Final points:")
print("Player 1 points:", player_one_points)
print("Player 2 points:", player_two_points)
if player_one_points > player_two_points:
    print("Player 1 wins the game!")
elif player_two_points > player_one_points:
    print("Player 2 wins the game!")
else:
    print("The game ends in a tie!")
