"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
element always exists in the array.

Example:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Tag: 5/150
Tag: 169/2927, R89/2936 (overall frequency ranking)
Tag: g1
"""
from collections import defaultdict


def majority_element_using_sorting(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[n//2]


def majority_element_using_hashmap(nums: list[int]) -> int:
    n = len(nums)
    m = defaultdict(int)
    for num in nums:
        m[num] += 1
    n = n // 2
    for key, value in m.items():
        if value > n:
            return key
    return 0


def majority_element_using_moore_voting_algo(nums: list[int]) -> int:
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


def majority_element_using_boyer_moore_voting_algorithm_ai(nums: list[int]) -> int:
    candidate = None
    count = 0

    for num in nums:
        # If count is 0, we establish a new candidate
        if count == 0:
            candidate = num
            count = 1
        # If the current number matches the candidate, increment
        elif num == candidate:
            count += 1
        # If it's different, the votes cancel out
        else:
            count -= 1

    return candidate


def main():
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element_using_boyer_moore_voting_algorithm_ai(nums))


if __name__ == "__main__":
    main()

"""
Approach:
While we could solve this using a hash map to count occurrences, that requires O(n) extra space. Since the 
problem guarantees that a majority element exists (appearing more than half the time), the Boyer-Moore 
Voting Algorithm is the gold standard.It is the most performant because it processes the array in a single
 pass with zero extra memory beyond two variables.
 
 The Strategy: Boyer-Moore Voting:
 ---------------------------------
 Think of this like a political election where every "non-majority" element
  tries to "vote out" the majority candidate. Because the majority element appears more than n/2 times, it 
  will always have at least one vote left over after all other elements have paired up to cancel each other
   out.
 
 -Candidate: We pick a candidate (the first element).
 -Count: We maintain a count.
 --If the next element is the same as the candidate, count += 1.
 --If it's different, count -= 1.
 -Reset: If the count hits zero, it means the current candidate has been "canceled out." we pick the current
  element as the new candidate and reset count to 1.
  
Why this is the "Best Performing"
--------------------------------
-Time Complexity: $O(n)$
--We iterate through the array exactly once.
-Space Complexity: O(1) 
--We only store two variables (candidate and count), regardless of how large the
 input array is. Compare this to a Hash Map approach which would take O(n) space.

"""