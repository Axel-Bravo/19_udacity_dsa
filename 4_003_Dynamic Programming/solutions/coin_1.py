# Solution One

# Let's assume F(Amount) is the minimum number of coins needed to make a change from coins [C0, C1, C2...Cn-1]
# Then, we know that F(Amount) = min(F(Amount-C0), F(Amount-C1), F(Amount-C2)...F(Amount-Cn-1)) + 1

# Base Cases: 
    # when Amount == 0: F(Amount) = 0
    # when Amount < 0: F(Amount) =  float('inf')

def coin_change(coins, amount):
    # Create a memo that will storing the fewest coins with given amount
    # that we have already calculated so that we do not have to do the
    # calculation again.
    memo = {}
    
    def return_change(remaining):
        # Base cases
        if remaining < 0:  return float('inf')
        if remaining == 0: return 0 
        
        # Check if we have already calculated
        if remaining not in memo:
            # If not previously calculated, calculate it by calling return_change with the remaining amount
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)
        return memo[remaining]
    
    res = return_change(amount)
    
    # return -1 when no change found
    return -1 if res == float('inf') else res
