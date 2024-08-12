def get_lcs_length(S1, S2):
    # Get the lengths of the two strings
    m = len(S1)
    n = len(S2)

    # Initialize a 2D list (matrix) of size (m+1) x (n+1) with all values set to 0
    # dp[i][j] will hold the length of LCS of S1[0..i-1] and S2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp matrix in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the characters in both strings match at position (i-1) and (j-1)
            if S1[i - 1] == S2[j - 1]:
                # Take the value from the diagonal left-up cell and add 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If they don't match, take the maximum value from either the left cell or the upper cell
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the longest common subsequence will be in dp[m][n]
    return dp[m][n]


# Driver code
if __name__ == "__main__":
    # Example strings
    S1 = "AGGTAB"
    S2 = "GS1TS1AS2B"

    # Function call to find the length of the LCS and print the result
    print("Length of LCS is", get_lcs_length(S1, S2))
