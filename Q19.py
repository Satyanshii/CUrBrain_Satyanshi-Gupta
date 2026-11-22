
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate(nums, k):
    n = len(nums)

    # Handle k greater than array length
    k = k % n

    # Step 1: Reverse the entire array
    reverse(nums, 0, n - 1)

    # Step 2: Reverse the first k elements
    reverse(nums, 0, k - 1)

    # Step 3: Reverse the remaining elements
    reverse(nums, k, n - 1)

nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter rotation steps (k): "))

rotate(nums, k)

print("Rotated array:", nums)
