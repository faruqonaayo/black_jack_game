import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_card():
    return random.choice(cards)

def give_two_cards(players_dict):
    for _ in range(0,2):
        for key in players_dict:
            players_dict[key].append(get_card())
    return

def more_than_21(list):
    if sum(list) > 21:
        return True
    else:
        return False

def decide_player_wins(players_dict, player):
    # creating variable to keep track of the players card total
    player_total = sum(players_dict[player])
    other_player_total = 0

    # deciding the other players total
    for key in players_dict:
        if key != player:
            other_player_total = sum(players_dict[key])

    if player_total > 21:
        return "lose"
    elif player_total == 21:
        return "win"
    elif player_total < 21 and player != "Computer":
        return "nothing"
    elif player_total > other_player_total:
        return "win"
    elif player_total == other_player_total:
        return "draw"
    else:
        return "lose"


def display_final_result(players_dict):
    for key in players_dict:
        print(f"\t{key} Cards: {players_dict[key]}; Total: {sum(players_dict[key])}")
    return


def black_jack():
    play_game = True

    while play_game:
        print("\n" * 20)
        print(logo)
        continue_game = input("Do you want to play a game of Black Jack? 'y' or 'n'").lower()

        if continue_game == 'y':
            run_game()
        else:
            # if continue game is 'n' then run game
            return


def run_game():
    # dictionary to hold players cards
    players = {
        "Player": [],
        "Computer": [],
    }

    # give the two players 2 cards each
    give_two_cards(players)

    get_another_card = 'y'

    while get_another_card == "y":
        print(f"Your Cards: {players["Player"]}; Total: {sum(players["Player"])}")
        print(f"Computer's first card: {players["Computer"][0]}")

        # Ask if the player wants to get another card
        get_another_card = input("Type 'y' to get another card and 'n' to pass").lower()

        if get_another_card == "y":
            new_card = get_card()

            # checking if adding new card increases the player card total to exceed 21
            if new_card == 11 and sum(players["Player"]) + new_card > 21:
                new_card = 1

            players["Player"].append(new_card)

            # checking if players total cards is more than 21
            player_wins = decide_player_wins(players, "Player")

            if player_wins == "win":
                get_another_card = "n"
                display_final_result(players)
                print("You Win 😊")
            elif player_wins == "lose":
                get_another_card = "n"
                display_final_result(players)
                print("You Lose 😢")
        elif get_another_card == "n":
            while sum(players["Computer"]) < 17:
                new_card = get_card()

                # checking if adding new card increases the computer card total to exceed 21
                if new_card == 11 and sum(players["Computer"]) + new_card > 21:
                    new_card = 1

                players["Computer"].append(new_card)

            # checking if computers total cards is more than 21
            computer_wins = decide_player_wins(players, "Computer")

            if computer_wins == "win":
                display_final_result(players)
                print("You Loose 😢")
            elif computer_wins == "lose":
                display_final_result(players)
                print("You Win 😊")
            elif computer_wins == "draw":
                display_final_result(players)
                print("It is a draw 🪢")

    input()

black_jack()