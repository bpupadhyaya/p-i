"""
You are given an integer array nums. Two players are playing a game with this array:
player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start
the game with a score of 0. At each turn, the player takes one of the numbers from
either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the
size of the array by 1. The player adds the chosen number to their score. The game
ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal,
then player 1 is still the winner, and you should also return true. You may assume
that both players are playing optimally.

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 10^7

Sample Input/Output:
Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7.
 No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True
representing player1 can win.

Tag: R10/2935
Cat: g2
"""


class PredictTheWinner:
    def predict_the_winner(self, nums: list[int]) -> bool:
        n = len(nums)
        # If the length is even, Player 1 can always win by
        # picking all even-indexed or all odd-indexed numbers.
        if n % 2 == 0:
            return True

        # dp[i] will store the max relative score for a subarray ending at i
        dp = nums[:]

        # Iterate through subarray lengths from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # The current player chooses either the left (nums[i])
                # or the right (nums[j]) element.
                # dp[i] (from previous length) represents the optimal
                # relative score for the other player.
                dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])

        # If the relative score is 0 or more, Player 1 wins
        return dp[0] >= 0


def main():
    winner = PredictTheWinner()
    nums = [1, 5, 233, 7]
    print(f"Input: {nums}")
    print(f"Output: {winner.predict_the_winner(nums)}")


if __name__ == "__main__":
    main()

