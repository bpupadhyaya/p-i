"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Tag: R5/145
Tag: 7/150
Tag: 121/2927, R6/2936
Cat: g1
"""


def max_profit(prices: list[int]) -> int:
    min_price = prices[0]
    max_profit_ = 0
    for price in prices[1:]:
        max_profit_ = max(max_profit_, price - min_price)
        min_price = min(min_price, price)
    return max_profit_


def max_profit_ai_gemini(prices: list[int]) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """
    # If the list is empty or has one price, no profit possible
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the lowest price found so far
        if price < min_price:
            min_price = price
        # Calculate profit if sold at current price and update max_profit
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_ai_gemini(prices))


if __name__ == "__main__":
    main()

"""
max_profit_ai_gemini:
Approach:
--------
To solve the "Best Time to Buy and Sell Stock" problem efficiently, we use a one-pass greedy algorithm.
Since we only care about the maximum difference between a historical low and a future high, we don't need 
to compare every single pair of days (which would be O(n^2)). Instead, we track the lowest price seen so 
far and calculate the potential profit at every step.

The Algorithm Logic:
--------------------
1. Initialize min_price to infinity (or the first element).
2. Initialize max_profit to 0.
3. Iterate through the prices:
    3-i: If the current price is lower than our min_price, update min_price.
    3-ii: Otherwise, calculate the profit if we sold today (current_price - min_price). If this profit is 
    greater than our current max_profit, update it.

Why this is the best solution:
------------------------------
Metric                  Complexity              Explanation
------                  ----------              -----------
Time Complexity         O(n)                  We only iterate through the prices list exactly once.
Space Complexity        O(1)                  We only store two variables (min_price and max_profit), 
                                                regardless of input size.
Optimality              Maximum               This is the "One Pass" approach, which is the most efficient 
                                                way to solve this specific constraint (single transaction).
"""