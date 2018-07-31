# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]


incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

incorrect6 = [[0,1,2],
              [2,0,1],
              [1,2,0]]

def check(list):
    list = ''.join(str(e) for e in list) # convert the list of numbers to string
    # print(len(list))

    for i in list:
        pos = list.find(i)
        pos_next = list.find(i, pos+1)
        # print('pos_next: ', pos_next)
        if pos_next < 0 and int(i) <= len(list) and int(i) >= 1:
            marker = True
        else:
            return False
    return marker

def check_sudoku(sudoku):

    column = []

    col = 0
    while col <= len(sudoku)-1:
        row = 0
        list = []
        while row <= len(sudoku)-1:
            if type(sudoku[row][col]) is not int:
                # print('hello')
                return False
            else:
                list.append(sudoku[row][col])
                row = row + 1
        column.append(list)
        col = col + 1

    # check whether the element is increasing by 1
    iter = 0
    while iter <= len(sudoku)-1:
        if check(sudoku[iter]) and check(column[iter]):
            marker = True
        else:
            marker = False
        iter = iter + 1

    return marker

# print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

# print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

# print(check_sudoku(incorrect4))
#>>> False

# print(check_sudoku(incorrect5))
#>>> False

print(check_sudoku(incorrect6))
