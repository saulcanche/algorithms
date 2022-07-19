def linear_search(list, tarjet):
    """
    Return the index position of the tarjet if found, else returns None """
    for i in range(0, len(list)):
        if list[i] == tarjet:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else: 
        print("target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 2)
verify(result)