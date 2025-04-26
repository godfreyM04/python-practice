def list_sum(numbers):
    sum = 0 #Included a variable to which all numbers would be added to there
    for number in numbers:
        sum += number #Implementation of line 2
    return sum #Sum is returned to the variable storing the function call

marks = [10,20,30]
sum = list_sum(marks) #Returns 60
print(sum)#