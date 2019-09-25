from random import randint  # imports randint
print("The below is your board. There is only 1 ship. The ship is hidden behind one of the Os. Guess a row and column to hit the ship")
board = []  # creates the empty list

for x in range(0, 5):
  board.append(["O"] * 5)  # this creates a list between [1,2,3,4,5] * 5


def print_board(board):
  for row in board:  # puts them in seprate lines
    print(" ".join(row))  # gets rid of the comas, and makes it look clean with the .join function


print_board(board)  # prints the board to show you how it looks


def random_row(board):
  return randint(0, len(board) - 1)


def random_col(board):
  return randint(0, len(board[0]) - 1)  # these two give you a random column and row using the random function. the reason we use 0, len is so that it counts from 0 to len so if you make changes in the future it will grab that number


ship_row = random_row(board)
ship_col = random_col(board)  # these two take on the function and asign it to the board with the variables


# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):  # this is a for loop that does it 4 times, gives you 4 guesses
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))  # this asks you to input a guess for rows and cols

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break  # tells you that you have guessed correctly and breaks the for loop so you dont have to continue guessing
  else:
    if guess_row not in range(5) or \
            guess_col not in range(5):
      print("Oops, that's not even in the ocean.")  # tells you if you guess outside of the range
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
      # tells you if you guess the same number as X is already marked as existing in the previos
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"  # marks the area as x if you miss it
      if turn == 3:
        print("Game Over")  # feeds back to the turn for loop, if its 3 then game is over
    print_board(board)  # prints the board after turns
    print(turn + 1)  # tells you how many turns you have, you cant have 0 turns becasue python starts with 0 so you add 1
