# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# def find_element(list, value):
#
#     pos = 0
#     for i in list:
#         if i != value:
#             mark = False
#         else:
#             return pos
#         pos = pos + 1
#
#     return -1

def find_element(list, value):

    try:
        return list.index(value)
    except:
        return -1

print(find_element([1,2,3],3))
#>>> 2

print(find_element(['alpha','beta'],'gamma'))
#>>> -1

print(find_element(['flower', 'petal', 'tree', 'grass'], 'flower'))
