coins=0
iteration=0
memo={}

def coin_change_memo(x):
    global iteration
    global memo
    global coins
    
    iteration=iteration+1
    
    print("Iteration#:",iteration, "coin change for:", x) 
    
    if x in memo:
        return memo[x]
    if x > 0:
        if x == 1 or x == 2 or x == 5:
            coins = 1
        else:
            coins = 1 + min(coin_change_memo(x-1), coin_change_memo(x-2), coin_change_memo(x-5))
    else:
        coins = 0
    memo[x] = coins
    return coins

amount= 8
number_of_coins=coin_change_memo(amount)

print("We need ", number_of_coins, "coins to make change for $", amount)
