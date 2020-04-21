
class board_map:
    
    def __init__(self):

        self._map = self._generate_map()
        self._locate_objects = self._locate_objects(self._map)
        #self._print_map = self._print_map(self._locate_objects)

        return

        
    def _generate_map(self):

        col_names = sorted(frozenset('ABCDEFGH'))
        row_names = sorted(frozenset('12345678'))
        dict_row = {}
                
        for i in row_names:
            row_dict = {}
            for j in col_names:
                row_dict[j + i] = '_'
            
            dict_row[i] = row_dict

        return dict_row


    def _locate_objects(self, board):

        for i in range(len(board)):

            if i < 3:
                k = 1
                for j in board[str(i + 1)]:
                    if k % 2 and not i % 2:
                        board[str(i + 1)][j] = '#'
                    elif not k % 2 and i % 2:
                        board[str(i + 1)][j] = '#'
                    else:
                        board[str(i + 1)][j] = 'X'
                    k += 1

                k = 1
                for j in board[str(len(board) - i)]:
                    if k % 2 and i % 2:
                        board[str(len(board) - i)][j] = '#'
                    elif not k % 2 and not i % 2:
                        board[str(len(board) - i)][j] = '#'
                    else:
                        board[str(len(board) - i)][j] = 'O'
                    k += 1
            else:
                k = 1
                for j in board[str(i + 1)]:
                    if k % 2 and not i % 2:
                        board[str(i + 1)][j] = '#'
                    elif not k % 2 and i % 2:
                        board[str(i + 1)][j] = '#'
                    else:
                        pass
                    k += 1
                        
        return board


    def check_near_cell(self, board, destination, checker):
        
        #print(checker)
        #print(destination)
        keys_list = []
        for i in board['1'].keys():
            keys_list.append(i[0])
        
        if 0 < int(checker[1]) <= len(board) and 0 < int(destination[1]) <= len(board):
            diff = int(checker[1]) - int(destination[1])
            if -1 <= diff <= 1 and diff != 0:
                for i in range(0, len(keys_list)):
                    if keys_list[i] == str(checker[0]).upper():
                        if 0 < (i + 1) < len(keys_list):
                            if keys_list[int(i + 1)] == str(destination[0]).upper():
                                return True
                            elif 0 <= (i - 1):
                                if keys_list[int(i - 1)] == str(destination[0]).upper():
                                    return True
                return False
            elif -2 <= diff <= 2 and diff != 0:
                #fight
                for i in range(0, len(keys_list)):
                    if keys_list[i] == str(checker[0]).upper():
                        if 0 < (i + 2) < len(keys_list):
                            if keys_list[int(i + 2)] == str(destination[0]).upper():
                                print('fight')
                                return True
                            elif 0 <= (i - 2):
                                if keys_list[int(i - 2)] == str(destination[0]).upper():
                                    print('fight')
                                    return True
                return False
            else:                
                return False
        else:
            return False



    def restricted_cells(self, board, destination, checker):

        if len(destination) == 2:
            for i in board['1'].keys():
                if str(i[0]) == str(destination[0]).upper() and int(destination[1]) < len(board):
                    if board[str(destination[1])][destination.upper()] == '_':
                        result = self.check_near_cell(board, destination, checker)
                        return result
            return False
        else:
            return False


    

    def exist_checker(self, board, cell, player):

        if player == 'player':
            player = 'O'
        else:
            player = 'X'

        if len(cell) == 2:
            for i in board['1'].keys():
                if str(i[0]) == str(cell[0]).upper() and int(cell[1]) < len(board):
                    if board[str(cell[1])][cell.upper()] == player:
                        return True
            return False
        else:
            return False


    def move_checker(self, board, checker, destination, player):

        if player == 'player':
            player = 'O'
        else:
            player = 'X'

        board[str(checker[1])][str(checker).upper()] = '_'
        board[destination[1]][str(destination).upper()] = player
        
        return board

    def print_map(self, board):

        columns_keys = []

        for i in board['1'].keys():
            columns_keys.append(i[0])

        print('    ', ' '.join(columns_keys), sep='')
        print()
        
        for i in board:
            print(i,'  |', '|'.join(list(board[i].values())), '|  ', i, sep='')

        print()
        print('    ', ' '.join(columns_keys), sep='')

        return


if __name__ == '__main__':

    print('Hello world!')
    #board_map()
