def type_of_number(num):
    if num % 2 == 0: #Checks for whether the remainder is 0 to determine if it is even
        print('The Number is Even')
    else:
        print('The Number is Odd') #If the remainder is not 0, it is automatically odd

num = 3 #odd
type_of_number(num) # The print statement in the else block is executed