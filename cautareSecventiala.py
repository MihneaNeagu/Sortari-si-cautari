def secvential_search(elements, target):
    for i in range(len(elements)):
        if elements[i] == target:
            return True
    return False
