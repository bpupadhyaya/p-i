"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are
at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach
nums[n - 1].

Example:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1,
then 3 steps to the last index.

Tag: 10/150
Tag: 45/2927, R258/2936 (overall frequency ranking)
"""


def jump(nums: list[int]) -> int:
    ans = 0
    end = 0
    farthest = 0
    # Implicit BFS
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            ans += 1
            break
        if i == end:    # Visited all the items on the current level
            ans += 1    # Increment the level
            end = farthest  # Make the queue size for the next level

    return ans


def jump_ai_gemini(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    # We don't need to jump from the last element
    for i in range(n - 1):
        # Update the farthest point reachable from current index
        farthest = max(farthest, i + nums[i])

        # If we've reached the end of our current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest

            # Optimization: if we can already reach the end, break early
            if current_end >= n - 1:
                break

    return jumps


def main():
    nums = [2,3,1,1,4]
    print(jump_ai_gemini(nums))


if __name__ == "__main__":
    main()

"""
jump_ai_gemini(...):
Approach:
--------
To solve this problem (commonly known as Jump Game II), the most efficient approach is a Greedy Algorithm. Instead of 
exploring every possible path, we track the farthest point we can reach within our current "jump range" and only 
increment our jump count when we exhaust that range.

The Greedy Strategy:
--------------------
We maintain three variables:
1. jumps: The total number of jumps made.
2. current_end: The farthest index we can reach with the current number of jumps.
3. farthest: The farthest index we can reach overall by jumping from any index we've passed so far.

Why this is the "Best" Solution?
--------------------------------
Feature             Complexity      Why it matters
-------             ---------       --------------
Time Complexity     O(n)            We traverse the array exactly once.
Space Complexity    O(1)            We only use a few integer variables regardless of input size.
Optimality          Greedy          Unlike Dynamic Programming (O(n^2)), this avoids unnecessary calculations by 
                                    always picking the "best" next window.

"""