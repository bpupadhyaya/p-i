"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the
following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.

Example:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Tag: 2/150
Tag: 27/2927, R174/2936 (overall frequency ranking)
Tag: g1
"""


def remove_element(nums: list[int], val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


def remove_element_2_ai(nums: list[int], val: int) -> int:
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            # Swap current element with the last valid element
            nums[i] = nums[n - 1]
            # Reduce array size, but don't increment i
            # because the new nums[i] needs to be checked
            n -= 1
        else:
            i += 1

    return n


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print("Before: ", nums)
    print(remove_element_2_ai(nums, val))
    print("After: ", nums)


if __name__ == "__main__":
    main()

"""
For remove_element_2_ai:
The Strategy: Two Pointers (Head and Tail)
------------------------------------------
Instead of shifting every non-target element forward, we can swap elements we want to remove with elements
 from the end of the array. This reduces the number of assignments if val appears infrequently.

Place one pointer (i) at the start and one pointer (n) at the end.

If nums[i] is equal to val, swap it with the last element nums[n-1] and reduce the size of the array we are
 considering (decrement n).

If nums[i] is not equal to val, simply move the start pointer i forward.
"""