# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(sudoku):
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
                        # print(sudoku[row][col])
                        temp_list.append(sudoku[row][col])
                        row = row + 1
                    column.append(temp_list)
                    col = col + 1

                # test whether the row and the column match
                iter = 0
                while iter <= len(sudoku)-1:
                    if sudoku[iter] != column[iter]:
                        return False
                    else:
                        marker = True
                    iter = iter + 1

    return marker


print(symmetric([]))

print(symmetric([['cricket', 'football', 'tennis'], ['golf']]))


print(symmetric([[1, 2, 3],
               [2, 3, 4],
               [3, 4, 1]]))
#>>> True

# print(symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "dog"],
               ["fish","fish","cat"]]))
#>>> False

# print(symmetric([[1, 2],
#                [2, 1]]))
#>>> True

# print(symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]]))
#>>> False

# print(symmetric([[1,2,3],
#                 [2,3,1]]))
#>>> False
