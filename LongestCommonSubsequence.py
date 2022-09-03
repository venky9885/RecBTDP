
def longest_common_subsequence(s1, s2):
    # we need a 2D list to memoize the sub-results
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    # this is why the running time is O(m*n)
    # m=len(s1) and n=len(s2)
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs = ''
    i = len(s1)
    j = len(s2)

    while i > 0 and j > 0:
        # if the current characters of s1 and s2 are matching then the
        # character is part of the LCS
        if s1[i - 1] == s2[j - 1]:
            lcs += s1[i - 1]
            i -= 1
            j -= 1

        # if letters are not matching then find the larger of two and
        # take a step in the direction of larger value
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs[::-1]


if __name__ == '__main__':
    print(longest_common_subsequence('aidfhr', 'abedgh'))
