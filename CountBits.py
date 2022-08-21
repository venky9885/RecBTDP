

# O(logN)
# n: decimal integer
def count_bits(n):
    counter = 0

    while n > 0:
        print(n)
        counter += 1
        # left-shift: doubles the original value
        # right-shift: divides the original value by 2
        n = n >> 1

    return counter


if __name__ == '__main__':
    print(bin(16))
    print(count_bits(16))




