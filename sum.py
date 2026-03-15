def add(*vargs):
    print(vargs)
    sum = 0
    for x in vargs:
        sum += x
    return sum

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))