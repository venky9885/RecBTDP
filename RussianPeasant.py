

def multiply(a, b):
    result = 0

    while b > 0:
        # whether 'b' is even or not (XOR operator)
        # if 'b' becomes odd (XOR operator decrements the value by 1 for odd numbers)
        # we want to skip when 'b' is even
        if b ^ 1 == b - 1:
            result = result + a

        # double the first number
        a <<= 1
        # halve the second number
        b >>= 1

    return result


if __name__ == '__main__':
    print(multiply(2355, 780))
    print(2355*780)






