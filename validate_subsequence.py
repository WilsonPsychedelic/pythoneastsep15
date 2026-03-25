def isValidSubsequence(array, sequence):
    seq_index = 0

    for num in array:
        if seq_index == len(sequence):
            break

        if num == sequence[seq_index]:
            seq_index += 1

    return seq_index == len(sequence)
