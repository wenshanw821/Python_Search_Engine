# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def smaller(x,y):
    if x < y:
        min = x
    else:
        min = y
    return min

def bigger(x,y):
    if x > y:
        max = x
    else:
        max = y
    return max

def smallest(x,y,z):
    return smaller(smaller(x, y), z)

def biggest(x,y,z):
    return bigger(bigger(x, y), z)

def set_range(x,y,z):
    # Your code here
    min = smallest(x,y,z)
    max = biggest(x,y,z)
    range = round(max-min,1)
    return range


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6
