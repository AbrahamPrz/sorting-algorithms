def main(arr: list) -> list:
    """
    Bubble sort
    Time complexity: O(N^2)

    Args:
        arr (list): lisit of elements to sort

    Returns:
        list: sorted elements in ascending order
    """
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break

    return arr
