#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    current = 0
    next = 1
    for i in range(0,n):
        current, next = next, current + next
    return current


print(fibonacci(60))

print(fibonacci(36))
#>>> 14930352
