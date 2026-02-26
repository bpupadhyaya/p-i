"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element
in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it
impossible to reach the last index.

Tag: 9/150
Tag: 55/2927, R130/2936 (overall frequency ranking)
"""


def can_jump_ai_gemini(nums: list[int]) -> bool:
    # This variable tracks the furthest index we can currently reach
    farthest_reachable = 0
    last_index = len(nums) - 1

    for i, jump_distance in enumerate(nums):
        # If the current index is greater than our max reach, we're stuck
        if i > farthest_reachable:
            return False

        # Update the max reach if the current jump takes us further
        farthest_reachable = max(farthest_reachable, i + jump_distance)

        # Early exit: if we can already reach the end, no need to keep checking
        if farthest_reachable >= last_index:
            return True

    return farthest_reachable >= last_index


def main():
    nums = [2, 3, 1, 1, 4]
    print(can_jump_ai_gemini(nums))


if __name__ == "__main__":
    main()


"""
Approach: 
This is a classic Greedy algorithm problem often referred to as Jump Game. While you could solve 
this using Dynamic Programming, the Greedy approach is significantly more efficient in both time 
and space.

The Logic: "The Horizon"
The most efficient way to solve this is to keep track of the farthest index you can possibly 
reach as you iterate through the array. If at any point your current index exceeds the farthest 
point you could have reached, it means you're stuck and can't progress.

Why this is the "Best" Performing Solution
Feature            Efficiency          Why it matters   
-------            ----------          --------------
Time Complexity     O(n)              We only traverse the array once.
Space Complexity    O(1)              We only store one integer (farthest_reachable), regardless of input size.
Early Exit          Yes               The if farthest_reachable >= last_index check ensures we 
                                            stop as soon as success is guaranteed, saving time on large arrays.

"""