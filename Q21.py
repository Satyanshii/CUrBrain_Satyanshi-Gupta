
def delete_element(arr, target):
    n = len(arr)

    # Step 1: Find the first occurrence
    index = -1

    for i in range(n):
        if arr[i] == target:
            index = i
            break

    # Step 2: If target is found, shift elements left
    if index != -1:
        for i in range(index, n - 1):
            arr[i] = arr[i + 1]

        # Step 3: Shrink array length by one
        arr.pop()

    return arr

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target element: "))

delete_element(arr, target)

print("Modified array:", arr)
