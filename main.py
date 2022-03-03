from bubbleSort import bubble_sort
from cautareBinara import binary_search
from cautareSecventiala import secvential_search
from quickSort import quick_sort


def test_secvential_search():
    elements = [1, 2, 4, 5]
    target = 2
    result = secvential_search(elements, target)
    print(result)
    target = 3
    result = secvential_search(elements, target)
    print(result)


test_secvential_search()


def test_binary_search():
    elements = [1, 2, 4, 5]
    target = 2
    result = binary_search(elements, target)
    print(result)
    target = 3
    result = binary_search(elements, target)
    print(result)


test_binary_search()


def test_bubble_sort():
    elements = [4, 8, 1, 3, 3]
    print(bubble_sort(elements))
    elements = [8, 9, 7, 3, 2, 125]
    print(bubble_sort(elements))


test_bubble_sort()


def test_quick_sort():
    elements = [4, 8, 1, 3, 3]
    print(quick_sort(elements, 0, len(elements)-1))
    elements = [8, 9, 7, 3, 2, 125]
    print(quick_sort(elements, 0, len(elements)-1))


test_quick_sort()
