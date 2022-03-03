def bubble_sort(elements):
    for i in range(len(elements)-1):
        for j in range(i+1, len(elements)):
            if elements[i] > elements[j]:
                elements[i], elements[j] = elements[j], elements[i]
    return elements
