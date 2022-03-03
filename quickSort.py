def partition(elements, left, right):
    pivot_index = left
    while left < right:
        while elements[left] <= elements[pivot_index] and left < right:
            left = left + 1
        while elements[right] > elements[pivot_index] and right > 0:
            right = right - 1
        if left < right:
            elements[left], elements[right] = elements[right], elements[left]
    elements[pivot_index], elements[right] = elements[right], elements[pivot_index]
    return right


def quick_sort(elements, left, right):
    if left < right:
        pivot_index = partition(elements, left, right)
        quick_sort(elements, pivot_index+1, right)
        quick_sort(elements, left, pivot_index-1)
    return elements
