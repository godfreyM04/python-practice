def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1) # The recursive part occurs here since the function is recalling itself
num = 4
f = factorial(num) #returns the factorial as the variable value
print(f)
