import numpy as np
import copy


class SAHistory:

    def __init__(self, checker_board, comment):
        self.queen_checkerboard = checker_board
        self.comment = comment

    def __repr__(self):
        return str(self.queen_checkerboard) + '\n' + 'Strategy -> ' + self.comment + '\n'


class N_Queen:

    def __init__(self, queen_no, queen=None):

        self.own_fitness = None
        self.checker_board_min_fitness = None

        if not queen:
            self.queen_no = queen_no
            self.checker_board = np.zeros((queen_no, queen_no), dtype=int)
            self.checker_board_fitness = np.zeros((queen_no, queen_no), dtype=int)
            self.initialize_checkerboard()
        else:
            self.queen_no = queen.queen_no
            self.checker_board_fitness = np.zeros((queen.queen_no, queen.queen_no), dtype=int)
            self.make_queen_from_queen(queen)
        self.calculate_checker_board_fitness()

    def make_queen_from_queen(self, queen):
        self.checker_board = queen.checker_board
        for column in range(queen.queen_no):
            present_column = list(queen.checker_board_fitness[:, column])
            minimum_value = queen.checker_board_min_fitness
            min_index = present_column.index(minimum_value) if minimum_value in present_column else -1
            if min_index != -1:
                current_column = self.checker_board[:, column]
                current_row_index = list(current_column).index(1)
                self.checker_board[current_row_index][column] = 0
                self.checker_board[min_index][column] = 1

    def initialize_checkerboard(self):
        # self.checker_board[4][0] = 8
        # self.checker_board[5][1] = 8
        # self.checker_board[6][2] = 8
        # self.checker_board[3][3] = 8
        # self.checker_board[4][4] = 8
        # self.checker_board[5][5] = 8
        # self.checker_board[6][6] = 8
        # self.checker_board[5][7] = 8
        random_index = [np.random.randint(self.queen_no) for i in range(self.queen_no)]
        for i in range(self.queen_no):
            self.checker_board[random_index[i]][i] = 1

    def calculate_checker_board_fitness(self):
        for row in range(self.queen_no):
            for column in range(self.queen_no):
                temp_checker_board = copy.deepcopy(self.checker_board)
                pre_present_column = temp_checker_board[:, column]
                pre_row_index = list(pre_present_column).index(1)
                temp_checker_board[pre_row_index][column] = 0
                temp_checker_board[row][column] = 1
                # print(temp_checker_board)
                total_attack = 0
                for column_index in range(self.queen_no):
                    present_column = temp_checker_board[:, column_index]
                    row_index = list(present_column).index(1)
                    # print(row_index, column_index)
                    attack = 0

                    """ same row attack"""
                    for i in range(column_index + 1, self.queen_no):
                        if temp_checker_board[row_index][i] == 1:
                            attack += 1

                    """ upper diagonal attack"""
                    temp_row = row_index - 1
                    temp_column = column_index + 1
                    while True:
                        if temp_row == -1 or temp_column == self.queen_no:
                            break
                        if temp_checker_board[temp_row][temp_column] == 1:
                            attack += 1
                        temp_row -= 1
                        temp_column += 1

                    """ lower diagonal attack"""
                    temp_row = row_index + 1
                    temp_column = column_index + 1
                    while True:
                        if temp_row == self.queen_no or temp_column == self.queen_no:
                            break
                        if temp_checker_board[temp_row][temp_column] == 1:
                            attack += 1
                        temp_row += 1
                        temp_column += 1

                    # print(attack)
                    total_attack += attack
                    pass
                self.checker_board_fitness[row][column] = total_attack
                pass
            pass
        pass
        self.checker_board_min_fitness = self.checker_board_fitness.min()
        self.own_fitness = self.checker_board_fitness[list(self.checker_board[:, 0]).index(1)][0]

    def __repr__(self):
        return str(self.checker_board)


def simulated_anneling(queen):
    global simulation_history
    current_queen = queen
    chance = 3
    while True:

        if current_queen.own_fitness == 0:
            simulation_history.append(SAHistory(current_queen.checker_board, 'Goal CheckerBoard Found'))
            return current_queen

        neighbour_queen = N_Queen(None, current_queen)

        if current_queen.own_fitness < neighbour_queen.own_fitness:
            queen = N_Queen(8)
            simulation_history.append(SAHistory(neighbour_queen.checker_board, 'Local Minimum Found, so CheckerBoard is Heated and New CheckerBoard Produced'))
            return simulated_anneling(queen)
        if current_queen.own_fitness == neighbour_queen.own_fitness:
            simulation_history.append(SAHistory(current_queen.checker_board, 'Shoulder or Flat Local Minimum Found. Neighbour  It will get 3 chances. Neighbourhood is Chosen'))
            chance -= 1
        if chance == 0:
            break
        current_queen = neighbour_queen
        if chance == 3:
            simulation_history.append(SAHistory(current_queen.checker_board, 'Neighbourhood CheckerBoard is Chosen'))
        # print(current_queen.own_fitness, current_queen.checker_board_min_fitness)
    if chance == 0:
        queen = N_Queen(8)
        simulation_history.append(SAHistory(queen.checker_board, 'After The Given 3 Chances, CheckerBoard is Heated and New CheckerBoard Produced'))
        return simulated_anneling(queen)


simulation_history = list()
my_queen = N_Queen(8)
simulation_history.append(SAHistory(my_queen.checker_board, 'Starting CheckerBoard'))
simulated_anneling(my_queen)
for i in range(len(simulation_history)):
    print(simulation_history[i])
print('iteration -> '+str(len(simulation_history)))