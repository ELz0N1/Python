def bits_count(number: int):
    count = 0

    if number >= 0:
        while number:
            count += number % 2
            number >>= 1
    else:
        number = abs(number)
        good_one = True
        while number:
            if number % 2:
                good_one = False
            elif not good_one:
                count += 1
            number >>= 1
        count += 2

    return count


n = int(input())
print(bits_count(n))
