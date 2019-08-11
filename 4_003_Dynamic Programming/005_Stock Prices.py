#%% Imports and functions declarations


def max_returns(prices: list) -> int:
    """
    Given a list of prices, return the maximum margin possible
    :param prices: prices
    :return: maximum margin
    """
    margins = dict()

    for i_buy in range(0, len(prices)-1):
        for i_sell in range(i_buy+1, len(prices)):
            buy_val = prices[i_buy]
            sell_vall = prices[i_sell]

            if (buy_val, sell_vall) not in margins:
                margins[(buy_val, sell_vall)] = sell_vall - buy_val

    margins = sorted(margins.items(), key=lambda x: x[1], reverse=True)

    return margins[0][1]


#%% Testing zone
prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
assert solution == max_returns(prices), 'Error, implementation is not correct'

prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
assert solution == max_returns(prices), 'Error, implementation is not correct'

prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
assert solution == max_returns(prices), 'Error, implementation is not correct'
