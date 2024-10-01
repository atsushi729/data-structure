def maxProfit(prices: list[int]) -> int:
    # Store profit as list
    profit = []

    for i in range(len(prices)):
        current_day_price = prices[i]
        max_price_day_after_current_day = max(prices[i:])

        current_profit = max_price_day_after_current_day - current_day_price
        profit.append(current_profit)

    max_profit = max(profit)

    if max_profit <= 0:
        return 0
    return max_profit
