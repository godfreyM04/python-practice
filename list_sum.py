def list_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

marks = [10,20,30]
sum = list_sum(marks)
print(sum)