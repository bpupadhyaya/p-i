"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Tag: 6/150
Tag: 189/2927, R54/2936 (overall frequency ranking)
Tag: g2
"""


def rotate(nums: list[int], k: int) -> None:
    length = len(nums)
    if length == k:
        return
    k = k % length  # the case when k > length
    nums.reverse()
    for i in range(k//2):
        nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
    for i in range(k, (length+k)//2):
        nums[i], nums[length-1-i+k] = nums[length-1-i+k], nums[i]


def rotate_2_ai_gemini(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n  # Handle cases where k > n

    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the whole array
    reverse(0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the rest
    reverse(k, n - 1)


def rotate_3_ai_grok(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # O(n) time · O(1) space – using three reverses

    n = len(nums)
    k = k % n  # handle k >= n
    if k == 0:
        return

    # Step 1: reverse whole array
    nums.reverse()  # [7,6,5,4,3,2,1]

    # Step 2: reverse first k elements
    nums[:k] = nums[:k][::-1]  # [5,6,7,4,3,2,1]

    # Step 3: reverse the rest
    nums[k:] = nums[k:][::-1]  # [5,6,7,1,2,3,4]


def rotate_4_ai_grok(nums: list[int], k: int) -> None:
    # One-liner version (very clean, still O(n) time, O(1) extra space)
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Before: ", nums)
    rotate_4_ai_grok(nums, k)
    print("After: ", nums)


if __name__ == "__main__":
    main()

"""
rotate_2_ai(...):

Approach:
---------
To rotate an array efficiently, the "best" implementation depends on whether you prioritize time
 complexity (speed) or space complexity (memory usage).

For technical interviews and large datasets, the Reversal Algorithm is considered the gold 
standard because it operates in-place with no extra memory.

The Reversal Algorithm:
-----------------------
The logic is elegant: by reversing specific segments of the array, the elements "rotate" into
 their correct positions without needing a temporary copy.
Steps:
    1. Normalize k: Since rotating an array of length n by n steps results in the original array, 
        we use k = k (mod n).
    2. Reverse the entire array.
    3. Reverse the first k elements.
    4. Reverse the remaining n-k elements.
  
Why use k %= n?
If our array length is 7 and k is 10, rotating 10 times is the same as rotating 3 times
 (10 mod 7 = 3). Skipping this step could lead to out-of-bounds errors or unnecessary work.  
 
 Performance Breakdown
 Metric             Complexity          Why?
 ------             ----------          ----
 Time Complexity    O(n)              We touch each element a constant number of times (two passes).
 Space Complexity   O(1)              No additional arrays or data structures are created.

"""