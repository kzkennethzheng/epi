def profit(prices):
    if not prices:
        return 0

    max_profit = 0
    max_future = prices[-1]
    for x in reversed(prices):
        max_future = max(x, max_future)
        max_profit = max(max_future - x, max_profit)
    return max_profit

prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(profit(prices))