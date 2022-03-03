def binary_search(elements, target):
    left = 0
    right = len(elements) - 1
    while left < right:
        mid = (left+right)//2
        if elements[mid] == target:
            return True
        elif elements[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False
