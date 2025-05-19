# Rules to Tricksy Battle: Card Game
Created by Daniela Burgos Ortega for INST126 Final Project.

How to Run Code for our Game: 

    1. Make sure you have Python 3 installed.
    2. Open a terminal in this folder.
    3. Run the program:
        python <file_name>
    4. Follow the prompts in the terminal.


How to Play Tricksy Battle:

    1. This game uses a standard deck of playing cards, with the Kings removed.
    2. The game starts with the deck face down, and eight cards are dealt to each player.
    3. Every round, each player plays a card.
    4. Whatever suit the player leads with, the other player must follow, if possible.
    5. If the second player cannot play a card in the same suit, they can play any card they wish.
    6. The player with the highest-value card in the “lead” suit wins that round, and that player earns a point.
    7. The player who wins the point gets to lead in the next round.
    8. After every round, one of the cards in the deck is removed and shown to both players. This has no effect on scoring or points, other than giving players information about what cards the other player might have.
    9. There are 16 rounds to the game, so there will be a total of 16 points if all rounds are played.
    10. The player with the most points at the end of the game wins.

    Shot the moon!: If the game ends 16 to 0, the player with zero points has “shot the moon”, and immediately scores 17 points, making them the winner.

    If at any time one player reaches 9 points and the other player has at least 1 point, the game should end, since there is no way the other player can still win.


Dependencies
To run this project with all advanced features, install the following Python packages:
    pip install pandas seaborn


Advanced Topics Included
1. random Module
The program uses random.choice() to randomly select elements or generate numbers to simulate unpredictable scenarios.
2. Data Visualization with pandas and seaborn
The project visualizes data using:
    pandas for structuring data
    seaborn for generating a bar chart or other plot
3. time Module
The program uses:
time.sleep() to simulate loading steps or delays between actions.


This project uses a game license. See LICENSE.txt for full details.