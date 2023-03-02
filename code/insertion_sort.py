def main(arr: list) -> list:
    """
    Insertion sort
    Time complexity: O(N^2)

    Args:
        arr (list): lisit of elements to sort

    Returns:
        list: sorted elements in ascending order
    """
    for i in range(1, len(arr)):
        aux = arr[i]
        j = i - 1
        while j >= 0 and aux < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = aux

    return arr
