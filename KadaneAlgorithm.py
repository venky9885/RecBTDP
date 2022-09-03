

# O(N)

def kadane(nums):
    local_max = nums[0]
    global_max = nums[0]

    # this is why it has linear running time complexity
    for i in range(1, len(nums)):
        local_max = max(nums[i], local_max + nums[i])

        if local_max > global_max:
            global_max = local_max

    return global_max


if __name__ == '__main__':
    print(kadane([1, -2, 1, 2, 3, -4]))
