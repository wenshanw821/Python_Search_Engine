# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.
def bigger(a,b):
    if a>b:
        return a
    else:
        return b

def greatest(list_of_numbers):
    if list_of_numbers == []:
        return 0
    else:
        iter = 0
        max = list_of_numbers[0]
        # print("||||||original_max: ", max)
        for i in list_of_numbers:
            # print(list_of_numbers)
            # print('i is: ', i)
            max = bigger(max,i)
            # print('Therefore, max is: ', max)
            # print('---------------')
        return max



print(greatest([4,23,1]))
#>>> 23
print(greatest([]))
#>>> 0
