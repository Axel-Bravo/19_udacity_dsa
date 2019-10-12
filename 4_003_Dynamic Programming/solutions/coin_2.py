# Solution Two

# We initiate F[Amount] to be float('inf') and F[0] = 0
# Let F[Amount] to be the minimum number of coins needed to get change for the Amount.
# F[Amount + coin] = min(F(Amount + coin), F(Amount) + 1) if F[Amount] is reachable.
# F[Amount + coin] = F(Amount + coin) if F[Amount] is not reachable.

def coin_change(coins, amount):
    # initiate the list with length amount + 1 and prefill with float('inf')
    res = [float('inf')]*(amount + 1)
    
    # when amount = 0, 0 number of coins will be needed for the change
    res[0] = 0
    
    i = 0
    while (i < amount):
        if res[i] != float('inf'):
            for coin in coins:
                if i <= amount - coin:
                    res[i+coin] = min(res[i] + 1, res[i+coin])
        i += 1

    if res[amount] == float('inf'):
        return -1
    return res[amount]
        
