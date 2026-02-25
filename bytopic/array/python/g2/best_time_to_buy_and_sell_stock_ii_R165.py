"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock
at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Tag: R68/145
Tag: 8/150
Tag: 122/2927, R165/2936 (overall frequency ranking)
"""

def max_profit_using_greedy_ai_gemini(prices: list[int]) -> int:
    """
        :type prices: List[int]
        :rtype: int
        """
    max_profit = 0

    # Iterate through prices starting from the second day
    for i in range(1, len(prices)):
        # If the price increased from yesterday, "capture" that gain
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit


def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_using_greedy_ai_gemini(prices))


if __name__ == "__main__":
    main()


"""
max_profit_using_greedy_ai_gemini:
Approach:
--------
To solve the "Best Time to Buy and Sell Stock II" problem, the most efficient approach is a Greedy Algorithm.

In this version of the problem, since you can perform multiple transactions, the goal is to capture every single 
price increase. If the price tomorrow is higher than the price today, you "buy" today and "sell" tomorrow to lock 
in that specific gain. Summing all these small daily gains is mathematically equivalent to buying at a local 
minimum and selling at a local maximum.

The Algorithm Logic:
-------------------
1. Iterate through the prices array starting from the second element (index 1).
2. Compare the current day's price with the previous day's price.
3. If current_price > previous_price, add the difference to your total_profit.
4. If the price drops or stays the same, do nothing.

Performance Analysis
--------------------
Metric                  Complexity      Explanation
Time Complexity         O(n)            We perform exactly one pass through the list of prices.
Space Complexity        O(1)            We only use one variable (max_profit) regardless of the input size.
Optimality              Maximum         Since there is no transaction fee, capturing every positive delta ensures
                                        the absolute maximum profit possible.

"""