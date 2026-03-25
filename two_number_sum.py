def twoNumberSum(array, targetSum):
    seen = set()

    for num in array:
        needed = targetSum - num

        if needed in seen:
            return [num, needed]
        
        seen.add(num)

    return []
