from board_map import board_map

print('Hello Checkers!')
print("To make a move you should enter cell's coordinate of a checker to move and destination cell's coordinate.")
print('Start of a game (player - O, bot - X):')
print('Example:')
print("Input (cell's coordinate of a checker to move): A6")
print("Input (destination cell's coordinate): B5")
print()

game = board_map()
board = game._locate_objects
game.print_map(board)

k = 1
while True:
    
    print()
    
    if k % 2:
        print('player move:')
        player = 'player'
        checker = input("Input (cell's coordinate of a checker to move) or Q - for quit:")

        if checker.upper() == 'Q':
            break
            
        if game.exist_checker(board, checker, player) is True:
            destination = input("Input (destination cell's coordinate):")
            if game.restricted_cells(board, destination, checker) is True:
                board = game.move_checker(board, checker, destination, player)
                print()
                print('Updated map:')
                game.print_map(board)
            else:
                print('Incorrect. Try again.')
                continue
        else:
            print('Incorrect. Try again.')
            continue
        
    else:
        print()
        print("Bot's move:")
        player = 'bot'
        #checker = input("Input (cell's coordinate of a checker to move) or Q - for quit:")
        #game.restricted_cells(board, checker)
        #destination = input("Input (destination cell's coordinate):")
        #game.restricted_cells(board, destination)
        #board = game.move_checker(board, checker, destination, player)
        #print()
        #game.print_map(board)
        checker = input("Input (cell's coordinate of a checker to move) or Q - for quit:")

        if checker.upper() == 'Q':
            break
            
        if game.exist_checker(board, checker, player) is True:
            destination = input("Input (destination cell's coordinate):")
            if game.restricted_cells(board, destination, checker) is True:
                board = game.move_checker(board, checker, destination, player)
                print()
                print('Updated map:')
                game.print_map(board)
            else:
                print('Incorrect. Try again.')
                continue
        else:
            print('Incorrect. Try again.')
            continue

    k += 1
