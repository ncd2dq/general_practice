# Recieve array of stock prices, each index is a day
# Determine the max profit you could have made of the given time range


def max_profit(prices, start=0, end=None):
    if end == None:
        end = len(prices)

    prices = prices[start:end]

    buy_price = prices[0]
    max_profit = prices[1] - buy_price

    for index, price in enumerate(prices):
        if index != 0:
            current_profit = price - buy_price
            if current_profit > max_profit:
                max_profit = current_profit
            elif price < buy_price:
                buy_price = price

    return max_profit

if __name__ == '__main__':
    test_range_1 =  [1, 2, 3, 4, 5, 6, 7, 8]
    test_range_2 = [8, 7, 6, 5, 4, 3, 2, 1]
    test_range_3 = [4, 4, 5, 8, 2, 3, 10, 15]
    test_range_4 = [0, 4, 5, 8, 2, 3, 10, 0]
    assert max_profit(test_range_1) == 7
    assert max_profit(test_range_2) == -1
    assert max_profit(test_range_3) == 13
    assert max_profit(test_range_4) == 10

