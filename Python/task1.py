#installed games

games = [
  'Soccer', 'Tic Tac Toe', 'Snake',
  'Puzzle', 'Rally']

#taking player's choice as a number input

print("Give a choice from 0-4")
choice = int(input())

#output the corresponding game

print(games[choice])