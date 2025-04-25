def digits_sum(num):
    total = 0 #Variable for storing the sum
    while num > 0: #makes sure that the number is not negative
        total += num % 10 #adds the remainder of the value(which is the last digit) to the total variable
        num = num // 10 # chops of the last digit and the whole loop recycles again
    return total

numbers = 1234
sum_numbers = digits_sum(numbers)
print(sum_numbers) # Output is 10
