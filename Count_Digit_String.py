def count_digit_string(n):
    abc = count_digit(n,"1")
    return abc


def count_digit(n,operation):
    if n == 1:
        return operation
    i = 0
    res =""
    while i < len(operation):
        appen = operation[i]
        count = 1
        j = i+1
        while j < len(operation):
            if operation[i] == operation[j]:
#                 print("in if")
                count += 1
                j += 1
                i += 1
            else:
                break
        res += str(count) + appen
        i +=1
    return count_digit(n-1,res)