def replace_with_right_sum(nums):
    right_sum = 0

    # Traverse from right to left
    for i in range(len(nums) - 1, -1, -1):
        current = nums[i]

        # Replace current element with right_sum
        nums[i] = right_sum

        # Add original value to right_sum
        right_sum += current

nums = list(map(int, input("Enter array elements: ").split()))

replace_with_right_sum(nums)

print("Modified array:", nums)
