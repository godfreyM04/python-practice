
def loop_factorial(num):
    i = num #Variable used as the counter
    while i > 1: #checks whether the counter is above 1
        num = num * (i-1) # The num variable stores the product of the 2 values
        i = i - 1
    return num


r = loop_factorial(4) # Output is 24
print(r)