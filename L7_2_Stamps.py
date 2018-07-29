# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required
# to make up that value. The return value should be a tuple of three numbers
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def int_p(x, pence):
    float_val = float(x/pence)
    string_val = str(float_val)
    pos = string_val.find('.')
    int_val = string_val[:pos]
    return int(int_val)

def stamps(x):
# Your code here

    # find the integer of 5p
    pence_5 = int_p(x,5)
    pence_2 = int_p(x-5*pence_5,2)
    pence_1 = int_p(x-5*pence_5-2*pence_2,1)

    return pence_5, pence_2, pence_1


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
