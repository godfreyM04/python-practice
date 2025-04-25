def string_reverse(name):
    for i in range(len(name)-1,-1,-1): #Uses the index of the last letter as starting point as it goes in reverse
        print(name[i])

name = "Hello"
string_reverse(name) #Output: o l l e H
