# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(sudoku):
    # Your code here
    # find the row
    column = []
    temp_list = []

    # test whether sudoku is empty
    if sudoku == []:
        return True
    else:
        for ele in sudoku:
            if len(ele) != len(sudoku):
                return False
            else:
                # find the column
                col = 0
                while col <= len(sudoku)-1:
                    row = 0
                    temp_list = []
                    while row <= len(sudoku)-1:
                        if sudoku[row][col] == -sudoku[col][row]:
                            marker = True
                        else:
                            return False
                        row = row + 1
                    col = col + 1

    return marker

# Test Cases:

print(antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
#>>> True

print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]]))
#>>> False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False
