def sortedSquaredArray(array):
    n = len(array)
    result = [0] * n

    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1):
        left_sq = array[left] ** 2
        right_sq = array[right] ** 2

        if left_sq > right_sq:
            result[i] = left_sq
            left += 1
        else:
            result[i] = right_sq
            right -= 1

    return result
