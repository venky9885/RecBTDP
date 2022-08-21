

# binary operations
# O(1) running time
# XOR operator by 1 increments the value of an even number by 1
# and decrements the value for odd numbers by 1
def is_even(n):
    if n ^ 1 == n + 1:
        return True

    return False


print(is_even(544365))







