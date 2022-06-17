# importing modules
import random
import sys
import pyinputplus as pyip

'''
NOTES:
- By replacing "print("FYI:" with "#print("FYI:" the print statements 
  that only exist for (exploratory) manual testing purposes disappear.
  I used these statements systematically to make sure that the program 
  works the way it should.
'''


'''
LESSONS LEARNED
- If I started this project again, I would have started as early as 
possible with a testing framework (e.g. 'unittest') in order to avoid
manual exploratory testing with the print-statements in the code.


'''


'''
Optional ToDo:
- (((make sure that  player and computer begin the round in turns,
  however I currently don't consider it useful because it adds 
  unnecessary complexity. But if I tried to implement it I would 
  probably do something like the following, although this would not 
  really work out because 1 round can take several loops.
   o add "odd_player_even_computer_starts variable = 0" and 
     "every new round „...+1“.  then)))

-(((Ideally you could play the game again after having won or lost but 
then I'd need another while loop (otherwise the deck does not restart 
again and the cards are not empty like at the beginning) at the 
beginning which would result in having even more intendation.)))

'''

'''TODO:
-Some Comments and print statements might still have to be translated 
into english. (e.g. "Wächter"/"Priester" etc.)
'''

# The welcome text with the rules of the game is displayed.
print('''LOVE LETTERS LIGHT
You play against 1 opponent (the computer). Each of you has up to 2 cards.
The game is played for 3 rounds. Each round can consist of 1 or several moves 
by the players, which makes them act one after the other. Each round begins
with the original deck of cards and can end with a win, a loss or a tie. 
If the deck gets empty within a round, the player with the highest card wins 
the round. The lowest card is a Wächter(1), and the highest is a Prinzessin(8).

Depending on which card is being played the following happens:
- Wächter(1): The card of the other player has to be guessed.
  If the guess is correct, the current round is won.
  As the Wächter exists relatively often in the game it is not possible 
  to guess that the other player has a Wächter.
- Priester(2): You see the card of the other player.
- Baron(3): If your other card is higher than the computer's card you win. 
  If it is lower you lose. If it is the same, the round continues.
- Zofe(4): You are protected from your opponent's card 
  as soon as it the other player's turn.
- Prinz(5): The opponent must replace his card with a new one.
- König(6): Your own card (the non-king card) 
  is swapped with the opponent's card.

These 2 cards have a special role:
- Gräfin(7): If you have this card in your hand, plus a Prinz(5) or König(6), 
  you must play the Gräfin(7).
- Prinzessin(8): If you play this card, you lose, unless it is 
  as a result of a Baron(3) from your opponent or because the cards 
  are compared at the very end.

In the deck there is a different amount of each card:
Wächter(1) -> 5 times
Priester(2), Baron(3), Zofe(4) and Prinz (5) -> twice each
König (6), Gräfin(7) and Prinzessin (8) -> once each

''')

# important variables
#wins, losses, ties
wins = 0
losses = 0
ties = 0

# player- and computerMove
player_card_chosen = []
computer_card_chosen = []

# Round number
round_number = 0


# The 2 variables below are used to make sure that the deck-renewal of a
# new round is only done once per round.
deck_round_2_is_recreated = False
deck_round_3_is_recreated = False

'''
OPTIONAL-TODO: it might make sense to already have lists with 1 element 
within the deck-list (e.g. "[5]" instead of "5") but probably it is not 
useful and/or worth the time adjusting it, well maybe as soon as I make 
the computer act intelligently by not making random decisions. Then it 
might be easier if the deck and the "lostDeck" already consists of
 "[5]"s etc.
'''


# The deck of cards is created.

# deck = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]  # 8s for
# testing purposes this is sometimes adjusted.

# deck = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]  # 7s for
# testing purposes'''

# deck = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6] # 3s for
# testing purposes

# deck = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ] # 3s for
# testing purposes

# deck = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4] # 4s for
# testing purposes

# deck = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ] # 3s for
# testing purposes

# deck = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ]  # 2s for
# testing purposes

# deck = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 1s for
# testing purposes

# deck = [1, 1, 1, 1] # small deck for testing purposes

deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
print("The deck has the following cards:", deck)

# OPTIONAL TODO: This variable was supposed to be used later for 
# recreating the deck for the second and third round. Unfortuantely 
# neither the version below 
# ("startingDeck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8] 
# " nor "startingDeck = deck" later did  work out later._8.5.22
#startingDeck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]

'''
(((OPTIONAL TODO: It might make sense to create a dictionary 
(e.g. 1 -> Wächter) to make the user see that actual name of the cards 
instead of the number)))
'''

# player and computer have each no card 1 and no card 2
player_card_1 = []
player_card_2 = []
computer_card_1 = []
computer_card_2 = []
print(
    '''FYI: The players have the following cards: 
    (playercards 1+2 and computercard 1+2)''',
    player_card_1,
    player_card_2,
    computer_card_1,
    computer_card_2)


# The player loses or wins or the round continues depending on how the 2
# compared cards relate to each other. This function is used in 2
# situations: when the Baron(3) is played and when the deck is empty.
def compare_cards():
    global wins
    global losses
    global ties
    if player_card_for_comparison < computer_card_for_comparison:
        print(
            "As your card (",
            player_card_for_comparison,
            ") is lower than the computer's card (",
            computer_card_for_comparison,
            ") you lose this round.")
        losses = losses + 1
    elif player_card_for_comparison > computer_card_for_comparison:
        print(
            "As your card (",
            player_card_for_comparison,
            ") is higher than the computer's card (",
            computer_card_for_comparison,
            ") you win this round.")
        wins = wins + 1
    elif player_card_for_comparison == computer_card_for_comparison:
        if deck == []:
            print(
                "As your card (",
                player_card_for_comparison,
                ") is as high as the computer's card (",
                computer_card_for_comparison,
                ") this round ends with a tie.")
            ties = ties + 1
        else:
            print(
                "As your card (",
                player_card_for_comparison,
                ") is as high as the computer's card (",
                computer_card_for_comparison,
                ") this round continues.")


# This function is used when the deck is empty, therefore every time the
# player or the computer gets a new card it its is checked whether the
# deck is empty and if so the function is used. The function forces the
# players to compare each other's highest card. The player with the
# highest card wins the round.
def card_comparison_after_empty_deck():
    global computer_card_for_comparison
    global player_card_for_comparison
    print(
        "As the deck is empty now", 
        "the player with the highest card wins the round.")
    player_card_for_comparison = max(player_card_1, player_card_2)
    computer_card_for_comparison = max(computer_card_1, computer_card_2)
    compare_cards()


# function which makes player a) get 1st card or b)get 2nd card as 
# card 1 or card 2 depending on which one is empty

def get_new_card_player():
    list_player_cards = [player_card_1, player_card_2]
    # Only playerCard2 should be filled
    if list_player_cards[0] != [] and list_player_cards[1] == []:
        print("FYI: listPlayerCards is:", list_player_cards)
        print(
            "playerCard2 is empty (but not playerCard1)," 
            "therefore playerCard2 will be filled")
        # decide on random card which the player will get as card 2
        picked_card_2_player = random.choice(deck)
        print(
            "Player picked the following card as card2:",
            picked_card_2_player)
        print("Card 2 of Player is now:", picked_card_2_player)
        # the card the player got as card No 2 is the card wich will disappear
        # from deck
        card_lost_from_deck = picked_card_2_player
        print(
            "The card which disappeared from the deck is:",
            card_lost_from_deck)
        # the card the player got as card No 2 disappears from deck
        deck.remove(card_lost_from_deck)
        print(deck)
        # print(type(playerCard2))
        return [player_card_2.append(picked_card_2_player)]

    # Only playerCard1 should be filled
    else:
        print("FYI: listPlayerCards is:", list_player_cards)
        print("playerCard1 is empty, therefore playerCard1 will be filled")
        # decide on random card which the player will get as card 1
        picked_card_1_player = random.choice(deck)
        print(
            "Player picked the following card as card1:",
            picked_card_1_player)
        print("Card 1 of Player is now:", picked_card_1_player)
        # the card the player got as card No 1 is the card wich will disappear
        # from deck
        card_lost_from_deck = picked_card_1_player
        print(
            "The card which disappeared from the deck is:",
            card_lost_from_deck)
        # the card the player got as card No 1 disappears from deck
        deck.remove(card_lost_from_deck)
        print(deck)
        # print(type(playerCard1))
        return [player_card_1.append(picked_card_1_player)]

# function which makes computer a) get 1st card or b)get 2nd card as card
# 1 or card 2 depending on which one is empty


def get_new_card_computer():
    list_computer_cards = [computer_card_1, computer_card_2]
    # Only computerCard2 should be filled
    if list_computer_cards[0] != [] and list_computer_cards[1] == []:
        print("FYI: listComputerCards is:", list_computer_cards)
        print(
            "computerCard2 is empty (but not computerCard1),",
            "therefore computerCard2 will be filled")
        # decide on random card which the computer will get as card 2
        picked_card_2_computer = random.choice(deck)
        print(
            "Computer picked the following card as card2:",
            picked_card_2_computer)
        print("Card 2 of Computer is now:", picked_card_2_computer)
        # the card the computer got as card No 2 is the card wich will
        # disappear from deck
        deckLostCard = picked_card_2_computer
        print("The card which disappeared from the deck is:", deckLostCard)
        # the card the computer got as card No 2 disappears from deck
        deck.remove(deckLostCard)
        print(deck)
        # print(type(pick2Computer))
        return [computer_card_2.append(picked_card_2_computer)]

    # Only computerCard1 should be filled
    else:
        print("FYI: listComputerCards is:", list_computer_cards)
        print("computerCard1 is empty therefore computerCard1 will be filled")
        # decide on random card which the computer will get as card 1
        picked_card_1_computer = random.choice(deck)
        print(
            "Computer picked the following card as card1:",
            picked_card_1_computer)
        print("Card 1 of Computer is now:", picked_card_1_computer)
        # the card the computer got as card No 1 is the card wich will
        # disappear from deck
        deckLostCard = picked_card_1_computer
        print("The card which disappeared from the deck is:", deckLostCard)
        # the card the computer got as card No 1 disappears from deck
        deck.remove(deckLostCard)
        print(deck)
        # print(type(pick1Computer))
        return [computer_card_1.append(picked_card_1_computer)]

# Optional ToDo: it might make sense to make sure that the function 
# accepts „[x]“ format instead of „integer“ format and adjust code where 
# the 2 lose-functions are applied but it is not really necessary
# function which makes PLAYER lose the card it just used


def lose_card_player(integer):
    global player_card_1
    global player_card_2
    if player_card_1 == [integer] and player_card_2 == [integer]:
        player_card_1 = []
    elif player_card_1 == [integer]:
        player_card_1 = []
    elif player_card_2 == [integer]:
        player_card_2 = []

# function which makes COMPUTER lose the card it just used


def lose_card_computer(integer):
    global computer_card_1
    global computer_card_2
    if computer_card_1 == [integer] and computer_card_2 == [integer]:
        computer_card_1 = []
    elif computer_card_1 == [integer]:
        computer_card_1 = []
    elif computer_card_2 == [integer]:
        computer_card_2 = []

# function which makes the player have no cards anymore


def no_cards_player():
    global player_card_1
    global player_card_2
    player_card_1 = []
    player_card_2 = []

# function which makes the computer have no cards anymore


def no_cards_computer():
    global computer_card_1
    global computer_card_2
    computer_card_1 = []
    computer_card_2 = []

# function which makes the computer and the player have no cards anymore


def no_cards_player_computer():
    no_cards_player()
    no_cards_computer()


while True:
    # The Game ends after 3 rounds
    if losses + wins + ties == 3:
        if losses > wins:
            print(
                "---Unfortunately YOU HAVE LOST the game with", wins, "wins,",
                losses, "losses and", ties, "ties.---")                    
            sys.exit()
        elif wins > losses:
            print(
                "---CONGRATULATIONS! You have won the game with", wins, 
                "wins,", losses, "losses and", ties, "ties.---")              
            sys.exit()
        else:
            print(
                "---THE GAME FINISHED without a winner: It\'s a tie with",
                wins, "wins,", losses, "losses and", ties, "ties.---") 
            sys.exit()

    # The round number is shown.
    round_number = wins + losses + ties + 1
    print("----- ROUND:", round_number, "-----")

    print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))

    # The deck is recreated when a new round begins

    # (((OPTIONAL TODO: It might make sense to make the game playable 
    # for more than 3 rounds, but I am not sure yet
    # how to implement it withough manually making each new round 
    # possible like in the 2 blocks below. The difficulty of 
    # implementing it is that there are "big" rounds and the rounds 
    # within each round.

    # ToDo:ideally "deck = startingDeck" should work but it didn't which is
    # why I wrote the deck's numbers manually again_8.5.22
    if round_number == 2 and deck_round_2_is_recreated == False:
        deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        deck_round_2_is_recreated = True
        print("FYI: The deck is recreated for the 2nd round:", deck)
        no_cards_player_computer()
        print(
            '''FYI: The players have the following cards: 
            (playercards 1+2 and computercard 1+2)''',
            player_card_1,
            player_card_2,
            computer_card_1,
            computer_card_2)

    if round_number == 3 and deck_round_3_is_recreated == False:
        deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        deck_round_3_is_recreated = True
        print("FYI: The deck is recreated for the 3rd round:", deck)
        no_cards_player_computer()
        print(
            '''FYI: The players have the following cards: 
            (player cards 1+2 and computer cards 1+2)''',
            player_card_1,
            player_card_2,
            computer_card_1,
            computer_card_2)

    # player can pick 2nd card
    print(
        'Please press "X" and Enter to pick a card',
        ' or press "Q" and Enter to quit the program.')

    # Player can pick a card or quit the game.
    player_pick_card_or_quit = pyip.inputMenu(
        ['X', 'Q'], lettered=False, numbered=False)

    while True:
        if player_pick_card_or_quit == 'Q':
            print('Thanks for playing!')
            sys.exit()
        if player_pick_card_or_quit == "X":
            break

    # computer gets first card (in the beginning of each round)
    
    # NOTE to myself: when I put "getNewCardPlayer()" before 
    # "getNewCardComputer()" , then only the 
    # "getNewCardPlayer()"-function works.
    # I don't know why, but this is the reason why I made it in this 
    # order._13.8.21 _TODO: maybe check if this problem still exists
    # but it does not really make difference, so it is not necessary. 
    # _23.5.22

    listComputerCards = [computer_card_1, computer_card_2]
    if computer_card_1 == [] and computer_card_2 == []:
        get_new_card_computer()
        print(
            "FYI: Because a new round began, the computer got the 1st card",
            "and now has the follwoing computerCard1:", computer_card_1)
        if deck == []:
            card_comparison_after_empty_deck()
            break

    # player gets first card (in the beginning of each round)
    listPlayerCards = [player_card_1, player_card_2]
    if player_card_1 == [] and player_card_2 == []:
        get_new_card_player()
        print(
            "Because a new round began, the player got the 1st card and now",
            " has the follwoing playerCard1:", player_card_1)
        if deck == []:
            card_comparison_after_empty_deck()
            break

    # player gets 2nd card
    get_new_card_player()
    if deck == []:
        card_comparison_after_empty_deck()
        break

    while True:
        # This is a special case: If the player has "Gräfin(7) and 
        # König(6)" or "Gräfin(7) and Prinz(5)"" the player cannot 
        # choose which card to play.
        # This variable is used for the if-statements below
        listPlayerCards = [player_card_1, player_card_2]

        if [7] in listPlayerCards and any(
                [[5] in listPlayerCards, [6] in listPlayerCards]):
            player_card_chosen = [7]
            print(
                "As you have the",
                player_card_1,
                "and the",
                player_card_2,
                ", now you automatically play the Gräfin.")
            print("FYI: playermove:", player_card_chosen)
            break

        print("You have the following 2 cards:", player_card_1, player_card_2)

        print(
            "You can now decide which of the following two cards you want to",
            " play:", player_card_1, "or", player_card_2)

        # The player chooses which of the 2 cards to play (unless it was 
        # the special case before).
        while True:
            player_card_chosen = [
                pyip.inputInt(
                    prompt='>>>>>>>',
                    min=1,
                    max=8)]  # input as integer in list
            # player move is only accepted if input is card 1 or card 2
            if player_card_chosen == player_card_1 or \
            player_card_chosen == player_card_2:
                break
            else:
                print(
                    "Please enter one of the following numbers depending on",
                    "which card you want to play:", player_card_1,
                    "or", player_card_2)

        print("FYI: playermove:", player_card_chosen)
        break

    # What happens depending on which card the player has chosen
    while True:
        # Gräfin(7)
        if player_card_chosen == [7]:  # player loses the card it just used
            print(
                "FYI: Before you played the Gräfin(7), those were the cards:",
                "(playercard 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            lose_card_player(7)

            print(
                "FYI: After you played the Gräfin(7), those are the cards:",
                "(playercard 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)
            break

        # Prinzessin(8)
        if player_card_chosen == [8]:
            print(
                "FYI: Before the Princess was played, those were the player's",
                "cards: playerCard1, playerCard2,  =>",
                player_card_1,
                player_card_2)

            no_cards_player()

            print("You lose!")

            losses = losses + 1

            print(
                "FYI: After the Princess was played, those were the player's",
                "cards: playerCard1, playerCard2,  =>",
                player_card_1,
                player_card_2)

            break

        '''
        If the computer has played the Zofe right before, the card the 
        player plays is without negative consequences for the computer.
        '''
        if computer_card_chosen == [4]:
            print(
                "FYI: Before you reacted to the Zofe of the computer:",
                "(playercard 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            # Even if the player played a Zofe here it would also have 
            # no consequence.
            print(
                "You played a", player_card_chosen, "but it has no",
                "consequence because of the Zofe played by the computer.")

            # the function needs the integer
            lose_card_player(player_card_chosen[0])

            print(
                "FYI: After you reacted to the Zofe of the computer:",
                "(playercard 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            # This makes sure that a Zofe(4) of the player or computer 
            # does not have unintended consequences afterwards. 
            # (((TODO: Check if this is really necessary but I am 
            # relatively sure that it is. Because otherwise it might 
            # become a problem in the next block of code or when it's 
            # the computer's turn. The same applies for the appropriate 
            # lines in the computer-blocks of code. _23.5.22)))
            player_card_chosen = []
            computer_card_chosen = []

            break

        # Zofe(4)
        if player_card_chosen == [4]:
            print(
                "FYI: Before you played the Zofe(4), those were the cards:",
                "(playercard 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            lose_card_player(4)

            print(
                "FYI: After you played the Zofe(4), those are the cards:",
                "(playercard 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            break

        # Baron(3) is played by the user.
        if player_card_chosen == [3]:
            print(
                "FYI: Before you played the Baron, those were the cards:",
                "(playercard 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            # The cards which have to be compared to each other are 
            # calculated. The computer has only 1 card, so as the other 
            # one is an empty list, the non-empty-list is automatically 
            # the card that has to be compared with"
            computer_card_for_comparison = max(
                computer_card_1, computer_card_2)
            print("FYI: comparisonComputerCard:", computer_card_for_comparison)

            if player_card_1 == [3] and player_card_2 == [3]:
                player_card_for_comparison = [3]

            else:
                listPlayerCards = [player_card_1, player_card_2]
                # list in list  
                player_card_for_comparison = [
                    non_3 for non_3 in listPlayerCards if non_3 != [3]]  
                # integer in list
                player_card_for_comparison = player_card_for_comparison[0]

            print("FYI: comparisonPlayerCard:", player_card_for_comparison)

            # The player loses or wins or the round continues depending 
            # on how the 2 compared cards relate to each other.
            compare_cards()

            no_cards_player_computer()

            print(
                "FYI: After you played the Baron, those are the cards:",
                "(playercard 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            break

        # Wächter(1)
        if player_card_chosen == [1]:
            lose_card_player(1)  # player loses the card it just uses

            print(
                "Which card do you expect the computer to have?",
                "(2/3/4/5/6/7/8)")
            print(
                "FYI: The Computer has the follwing 2 cards",
                computer_card_1,
                computer_card_2)

            # as integer (for testing purpose I sometimes use "min = 1" instead
            # of "min = 0")
            playerGuess = pyip.inputInt(prompt='>>>>>>>>', min=2, max=8)
            playerGuess = [playerGuess]  # as integer in list

            print("FYI: the playerGuess is:", playerGuess)

            if playerGuess == max(computer_card_1, computer_card_2):
                print("Your assumption was correct! You won this round!")
                wins = wins + 1
                no_cards_player()

            else:
                print(
                    "Unfortunately your assumption was incorrect.",
                    "The round continues")

            break

        '''
        ((TODO: at the beginning and end it should be 
        "Before/After...playercard1+2 u computercard 1+2." 
        This should be for every special card. I might have forgotten
        it for some although I am relatively sure that I have it for
        all of them_27.5.22))
        '''

        # Prinz(5)
        if player_card_chosen == [5]:
            print(
                "FYI: Before you played the Prinz(5), those were the cards",
                "(playercard 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            no_cards_computer()
            print(
                "FYI: After the computer's cards are '[]',",
                "the computer's cards are:",
                computer_card_1,
                computer_card_2)

            get_new_card_computer()
            print(
                "FYI: After the computer got a new card,",
                "the computer's cards are:",
                computer_card_1,
                computer_card_2)
            if deck == []:
                card_comparison_after_empty_deck()
                break

            lose_card_player(5)  # player loses the card it just uses

            print(
                "FYI: After you played the Prinz(5), those are the cards",
                "(playercards 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            break

        # Priester(2)
        if player_card_chosen == [2]:
            print("The computer has the following card: ",
                  max(computer_card_1, computer_card_2))

            print(
                "FYI: Before the Priester(2) was played, those were the cards",
                "(playercards 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            lose_card_player(2)

            print(
                "FYI: After the Priester(2) was played, those are the cards",
                "(playercards 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            break

        # König(6)
        if player_card_chosen == [6]:
            print(
                "Before the King was played, those were the cards",
                "(playercards 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            if player_card_1 == [6] and computer_card_1 != []:
                player_card_2, computer_card_1 = computer_card_1, player_card_2
            if player_card_1 == [6] and computer_card_2 != []:
                player_card_2, computer_card_2 = computer_card_2, player_card_2
            if player_card_2 == [6] and computer_card_1 != []:
                player_card_1, computer_card_1 = computer_card_1, player_card_1
            if player_card_2 == [6] and computer_card_2 != []:
                player_card_1, computer_card_2 = computer_card_2, player_card_1

            lose_card_player(6)

            print(
                "After the King was played, those are the cards",
                "(playercards 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)
            break

    while True:  # Main loop of Computer's turn
        if round_number == wins + ties + losses:  # If the player lost or won 
            # already before, the "while-True-Level-1"-script is started
            # all over again.
            break
        else:  # If the player has not lost or won yet, the script continues.
            # computer gets first card (only in the beginning of each round or
            # if computer has lost all 2 cards before)
            print(
                "FYI:Before the computer got new card(s)",
                "(playercards 1+2 and computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            listComputerCards = [computer_card_1, computer_card_2]
            if computer_card_1 == [] and computer_card_2 == []:
                get_new_card_computer()
                print(
                    "FYI: Because a new round began (or because both 2 cards",
                    "were lost before), the computer got the 1st card and now",
                    "has the follwoing computerCard1:",
                    computer_card_1)
                if deck == []:
                    card_comparison_after_empty_deck()
                    break

            # computer gets 2nd card
            get_new_card_computer()
            print(
                "The computer has the following 2 cards now:",
                computer_card_1,
                computer_card_2)
            if deck == []:
                card_comparison_after_empty_deck()
                break

            print(
                "FYI: After the computer got new card(s) (playercards 1+2 and",
                "computercard 1+2):",
                player_card_1,
                player_card_2,
                computer_card_1,
                computer_card_2)

            # This is a special case: If the computer has "Gräfin(7) and
            # König(6)" or "Gräfin(7) and Prinz(5)"" the computer cannot 
            # choose randomly which card to play.
            # This variable is used for the if-statements below
            listComputerCards = [computer_card_1, computer_card_2]

            if [7] in listComputerCards and any(
                    [[5] in listComputerCards, [6] in listComputerCards]):
                computer_card_chosen = [7]
                print(
                    "FYI: The computer has a ",
                    computer_card_1,
                    "and a ",
                    computer_card_2,
                    "and now automatically plays the Gräfin.")

                print("FYI: computerMove:", computer_card_chosen)

            # Other Cases
            else:
                # random integer 1 vs 2 is generated; POTENTIAL TODO: ideally
                # the computer would choose based on certain useful rules which
                # card to play
                x = random.randint(1, 2)
                print("FYI: the generated random 1 vs. 2 is:", x)
                if x == 1:
                    computer_card_chosen = computer_card_1
                    print("Computer Move is:", computer_card_chosen)
                if x == 2:
                    computer_card_chosen = computer_card_2
                    print("Computer Move is:", computer_card_chosen)

            # Gräfin (7)
            if computer_card_chosen == [
                    7]:  # computer loses the card it just used
                print(
                    "FYI: Before the computer played the Gräfin(7), those",
                    "were the cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                lose_card_computer(7)

                print(
                    "FYI: After the computer played the Gräfin(7), those are",
                    "the cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)
                break

            # Prinzessin(8)
            if computer_card_chosen == [8]:
                print(
                    "FYI: Before the computer played the princess(8), those",
                    "were the cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                no_cards_computer()

                print("You win!")

                wins = wins + 1

                print(
                    "FYI: After the computer played the princess(8), those",
                    "are the cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                break

            # The card which the computer reacts with to the Zofe played by the
            # player has not the usual consequence.
            if player_card_chosen == [4]:
                print(
                    "FYI: Before the computer reacted to the Zofe of the",
                    "player (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                # Even if the computer played a Zofe here it would also have no
                # consequence.
                print(
                    "The computer played a",
                    computer_card_chosen,
                    "but it has no consequence because of the Zofe played by",
                    "the player.")

                # the function needs the integer
                lose_card_computer(computer_card_chosen[0])

                print(
                    "FYI: After the computer reacted to the Zofe of the",
                    "player (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                # This makes sure that a Zofe(4) of the player or computer does
                # not have unintended consequences afterwards. (((TODO: Check
                # if this is really necessary but I am relatively sure that it
                # is. Because otherwise it might become a problem in the next
                # block of code or when it's the player's turn. The same
                # applies for the    appropriate lines in the computer-blocks
                # of code. _23.5.22)))
                player_card_chosen = []
                computer_card_chosen = []

                break

            # Zofe(4)
            if computer_card_chosen == [4]:
                lose_card_computer(4)
                break

            # Priester(2) (TODO: ideally the computer would get the information
            # about the 1 card of the player and make use of this information
            # in its further decision making, however ths is not yet the case)
            if computer_card_chosen == [2]:
                print(
                    "FYI: Before the Priester(2) was played, those were the",
                    "cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                lose_card_computer(2)

                print(
                    "FYI: After the Priester(2) was played, those are the",
                    "cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                break

            # Prinz(5)
            if computer_card_chosen == [5]:
                print(
                    "FYI: Before the computer played the Prinz(5), those",
                    "were the cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)
                lose_card_computer(5)  # computer loses the card it just uses

                no_cards_player()
                print(
                    "FYI: After you lost your card, your cards are:",
                    player_card_1,
                    player_card_2)

                get_new_card_player()
                print(
                    "FYI: After you got a new card, your cards are:",
                    player_card_1,
                    player_card_2)
                if deck == []:
                    card_comparison_after_empty_deck()
                    break

                print(
                    "FYI: After the computer played the Prinz(5), those are",
                    "the cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                break

            # König(6)
            if computer_card_chosen == [6]:
                print(
                    "Before the King was played by the computer, those were",
                    "the cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                if computer_card_1 == [6] and player_card_1 != []:
                    computer_card_2, player_card_1 = \
                    player_card_1, computer_card_2
                if computer_card_1 == [6] and player_card_2 != []:
                    computer_card_2, player_card_2 = \
                    player_card_2, computer_card_2
                if computer_card_2 == [6] and player_card_1 != []:
                    computer_card_1, player_card_1 = \
                    player_card_1, computer_card_1
                if computer_card_2 == [6] and player_card_2 != []:
                    computer_card_1, player_card_2 = \
                    player_card_2, computer_card_1

                lose_card_computer(6)

                print(
                    "After the King was played by the computer, those are",
                    "the cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                break

            '''
            TODO: BELOW: ideally the computer knows which cards are already
             played this round in order to adjust which computerGuess has
             a higher chance of being correct
            '''

            # Wächter(1) is played by the computer.
            if computer_card_chosen == [1]:
                lose_card_computer(1)  # computer loses the card it just uses

                print(
                    "The computer will guess which card you have",
                    "(2/3/4/5/6/7/8).")
                print(
                    "FYI: You have the follwing card:", max(
                        player_card_1, player_card_2))

                computerGuess = random.choice(
                    [[2], [3], [4], [5], [6], [7], [8]])
                print(
                    "The computer guesses that you have the following card:",
                    computerGuess)

                if computerGuess == max(player_card_1, player_card_2):
                    print(
                        "The computer's assumption was correct!",
                        "You lost this round!")
                    losses = losses + 1
                    no_cards_computer()
                else:
                    print(
                        "The computer's assumption was incorrect.",
                        "The round continues.")
                break

            # Baron(3) is played by the computer.
            if computer_card_chosen == [3]:
                print(
                    "FYI: Before the Baron was played by the computer,",
                    "those were the cards (playercards 1+2 and",
                    "computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                # The player has only 1 card, so as the other one is an empty
                # list, the non-empty-list is automatically the card that has
                # to be compared with"
                player_card_for_comparison = max(player_card_1, player_card_2)
                print("FYI: comparisonPlayerCard:", player_card_for_comparison)

                # The cards which have to be compared to each other are
                # calculated.
                if computer_card_1 == [3] and computer_card_2 == [3]:
                    computer_card_for_comparison = [3]

                else:
                    listComputerCards = [computer_card_1, computer_card_2]
                    # list in list
                    computer_card_for_comparison = [
                        non_3 for non_3 in listComputerCards if non_3 != [3]]  
                    # integer in list
                    computer_card_for_comparison = \
                    computer_card_for_comparison[0]

                print(
                    "FYI: comparisonComputerCard:",
                    computer_card_for_comparison)

                # The computer loses or wins or the round continues depending
                # on how the 2 compared cards relate to each other.
                compare_cards()

                no_cards_player_computer()

                print(
                    "FYI: After the Baron was played by the computer, those",
                    "are the cards (playercards 1+2 and computercard 1+2):",
                    player_card_1,
                    player_card_2,
                    computer_card_1,
                    computer_card_2)

                break
