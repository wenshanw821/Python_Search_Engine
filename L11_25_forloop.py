# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.

def measure_udacity(list):
    count = 0
    for i in list:
        # print(i)
        pos = i.find('U')
        # print(pos)
        if pos < 0:
            count = count
        else:
            count = count + 1
    return count


print(measure_udacity(['Dave','Sebastian','Katy']))
#>>> 0

print(measure_udacity(['Umika','Umberto']))
#>>> 2
