# Busca binária

# Nova função
def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <= end:
        m = (begin + end)//2
        if array [m] == item:
            return m
        if item < array[m]:
            return binary_search(array, item, begin, m-1)
        else:
            return binary_search(array, item, m+1, m-1)
        return None

