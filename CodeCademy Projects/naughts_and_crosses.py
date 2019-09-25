#Preparing game state
global game_state
game_state = True

#Defining the game as a function to allow multiple playthroughs
def naughts_and_crosses():

    #Game board
    def game_board():
        print(f" {pos_7} | {pos_8} | {pos_9} ")
        print("------------")
        print(f" {pos_4} | {pos_5} | {pos_6} ")
        print("------------")
        print(f" {pos_1} | {pos_2} | {pos_3} ")

    #Win statement
    def win_statement():
        print(f"Congratulations {player_id}, you have won!")
        new_game()

    #New game
    def new_game():
        global game_state
        while game_state is True:
            new_game_input = str(input("Do you want to play again?"))
            if new_game_input.lower() == "yes":
                naughts_and_crosses()
            elif new_game_input.lower() == "no":
                print("OK. Thanks for playing!")
                game_state = "FALSE"
            else:
                invalid_input()
                continue

    #Invalid input
    def invalid_input():
        print("That's not a valid input, try again!")

    #Win checking
    def win_checking():
        if move_d["position_7"]==move_d["position_8"]==move_d["position_9"] or \
        move_d["position_4"]==move_d["position_5"]==move_d["position_6"] or \
        move_d["position_1"]==move_d["position_2"]==move_d["position_3"] or \
        move_d["position_7"]==move_d["position_4"]==move_d["position_1"] or \
        move_d["position_8"]==move_d["position_5"]==move_d["position_2"] or \
        move_d["position_9"]==move_d["position_6"]==move_d["position_3"] or \
        move_d["position_7"]==move_d["position_5"]==move_d["position_3"] or \
        move_d["position_9"]==move_d["position_5"]==move_d["position_1"] or \
        move_d["position_4"]==move_d["position_5"]==move_d["position_6"] or \
        move_d["position_8"]==move_d["position_5"]==move_d["position_2"]:
            win_statement()

        elif set(move_d.values()) == set(comparison_d.values()): #set reduces a list down to its unique values
            print("Game over - no more moves left!")
            new_game()

    #Declaring the values for the board positions
    pos_1=" "
    pos_2=" "
    pos_3=" "
    pos_4=" "
    pos_5=" "
    pos_6=" "
    pos_7=" "
    pos_8=" "
    pos_9=" "

    #Position dictionary
    pos_d = {"1":pos_1,"2":pos_2,"3":pos_3,"4":pos_4,"5":pos_5,"6":pos_6,"7":pos_7,"8":pos_8,"9":pos_9}
    move_d = {"position_1":"1","position_2":"2","position_3":"3","position_4":"4","position_5":"5","position_6":"6","position_7":"7","position_8":"8","position_9":"9"}
    comparison_d = {"k1":"X","k2":"O"}

    #Introduction
    print("Welcome to naughts and crosses! \nWhen asked for your move, type in the number corresponding to the position on the board below.")
    print(" 7 | 8 | 9 ")
    print("------------")
    print(" 4 | 5 | 6 ")
    print("------------")
    print(" 1 | 2 | 3 ")

    #Selecting character
    while game_state is True:
        player1 = str(input("Player 1: Do you want to be X or O?")).upper()
        if player1 not in set(comparison_d.values()):
            invalid_input()
            continue

        if player1 == "X":
            player2 = "O"
        else:
            player1 = "O"
            player2 = "X"

        currentplayer = player1
        player_id = "Player 1"

        game_board()
        break

    #Game logic
    while game_state is True:
        player_moveinput = str(input(f"{player_id} - {currentplayer} - what is your move?"))
        if player_moveinput == "1":
            if pos_1 != " ":
                invalid_input()
                continue
            pos_1 = currentplayer
            move_d["position_1"] = currentplayer
        elif player_moveinput == "2":
            if pos_2 != " ":
                invalid_input()
                continue
            pos_2 = currentplayer
            move_d["position_2"] = currentplayer
        elif player_moveinput == "3":
            if pos_3 != " ":
                invalid_input()
                continue
            pos_3 = currentplayer
            move_d["position_3"] = currentplayer
        elif player_moveinput == "4":
            if pos_4 != " ":
                invalid_input()
                continue
            pos_4 = currentplayer
            move_d["position_4"] = currentplayer
        elif player_moveinput == "5":
            if pos_5 != " ":
                invalid_input()
                continue
            pos_5 = currentplayer
            move_d["position_5"] = currentplayer
        elif player_moveinput == "6":
            if pos_6 != " ":
                invalid_input()
                continue
            pos_6 = currentplayer
            move_d["position_6"] = currentplayer
        elif player_moveinput == "7":
            if pos_7 != " ":
                invalid_input()
                continue
            pos_7 = currentplayer
            move_d["position_7"] = currentplayer
        elif player_moveinput == "8":
            if pos_8 != " ":
                invalid_input()
                continue
            pos_8 = currentplayer
            move_d["position_8"] = currentplayer
        elif player_moveinput == "9":
            if pos_9 != " ":
                invalid_input()
                continue
            pos_9 = currentplayer
            move_d["position_9"] = currentplayer
        else:
            invalid_input()
            continue

        #Game board
        game_board()

        #Win checking
        win_checking()

        #Swapping turns
        if currentplayer == player1:
            currentplayer = player2
        else:
            currentplayer = player1

        if player_id == "Player 1":
            player_id = "Player 2"
        else:
            player_id = "Player 1"

        continue

naughts_and_crosses()
