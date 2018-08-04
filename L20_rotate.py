# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string, n):
    # Your code here

    new_string = []

    string = string.split()

    for entry in string:
        list = []
        for i in entry:
            value = ord('a') + (ord(i) + n - ord('a')) % 26
            list.append(chr(value))
        new_string.append(''.join(list))

    return ' '.join(new_string)

print(rotate ('sarah', 13))
# #>>> 'fnenu'
print(rotate('fnenu',13))
# #>>> 'sarah'
print(rotate('dave',5))
# #>>>'ifaj'
print(rotate('ifaj',-5))
#>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???
