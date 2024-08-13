def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False
    
    total_sum = 0
    
    for index in range(9):
        if not isbn[index].isdigit():
            return False
        total_sum += int(isbn[index]) * (10 - index)

    if isbn[9] == 'X':
        total_sum += 10
    elif isbn[9].isdigit():
        total_sum += int(isbn[9])
    else:
        return False
    
    return total_sum % 11 == 0
