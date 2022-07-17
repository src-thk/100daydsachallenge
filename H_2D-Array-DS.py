'''
space complexity o(n^2)
time complexity o(n^2)
'''


def hourglassSum(arr):
    rows = len(arr)
    coloumns = len(arr[0])

    max_sum = -63  # acc to constraints

    for i in range(rows - 2):
        for j in range(coloumns - 2):
            current_sum = (
                (arr[i][j] + arr[i][j+1] + arr[i][j+2]) +
                (arr[i+1][j+1]) +
                (arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            )
            max_sum = max(current_sum, max_sum)
    return max_sum
