"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
unique element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they
were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4
respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Tag: 3/150
Tag: 26/2927, R59/2936 (overall frequency ranking)
Tag: g1
"""


def remove_duplicates(nums: list[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j


def remove_duplicates_2_ai(nums: list[int]) -> int:
    # If the array is empty, return 0
    if not nums:
        return 0

    # k is the write-pointer.
    # The first element (index 0) is always unique, so we start writing at index 1.
    k = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous unique element
        if nums[i] != nums[k - 1]:
            # Move the unique element to the position k
            nums[k] = nums[i]
            # Increment k to the next available slot
            k += 1

    return k


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print('Before:', nums)
    print(remove_duplicates_2_ai(nums))
    print('After:', nums)


if __name__ == "__main__":
    main()
