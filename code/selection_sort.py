def main(arr: list) -> list:
    """Selection sort
    Time complexity: O(N2)

    Args:
        arr (list): lisit of elements to sort

    Returns:
        list: sorted elements
    """
    for i in range(len(arr)):
        min_val = i        
        for j in range(i+1, len(arr)):    
            if arr[min_val] > arr[j]:
                min_val = j
        arr[i], arr[min_val] = arr[min_val], arr[i]

    return arr
