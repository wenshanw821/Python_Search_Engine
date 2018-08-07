def proc3(n):
   if n <= 3:
      return 1
   return proc3(n - 1) + proc3(n - 2) + proc3(n - 3)

print(proc3(7))
