# We are trying to maximize number of 5's in our result. That's why we first check
# whether the inputted number can be exhausted with three 5s, we chose this option, because its the best one and we
# continue recursively. Second option is to continue with five 3s,if the first one doesnt hold
# and the number can still be exhausted with five 3s, we make this choice and continue recursively.
# If neither one of the above mentioned options hold, we just hope for the best in the future,
# and chose the best current option, which is three 5s and continue recursively.
# If the inputted number could not be exhausted we return -1, otherwise the obtained number

def decentNumber(num):
# if the number is exhausted
    if num == 0:
        return ''
# if the number is hopeless
    elif num < 3:
        return '-1'
# if the number at this stage can be exhausted with three 5s, we chose this option, because its the best one
    elif num % 3 == 0:
        recursiveCall = decentNumber(num-3)
        return '555' + recursiveCall if recursiveCall != '-1' else recursiveCall
# second option is to continue with five 3s,if the first one doesnt hold and the number can still be exhausted with five 3s
    elif num % 5 == 0:
        recursiveCall = decentNumber(num-5)
        return '33333' + recursiveCall if recursiveCall != '-1' else recursiveCall
# if neither one of the above hold,we just hope for the best in the future, and chose the best current option, which is three 5s
    else:
        recursiveCall = decentNumber(num - 3)
        return '555' + recursiveCall if recursiveCall != '-1' else recursiveCall

print(decentNumber(13))