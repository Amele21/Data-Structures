# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Recursions

# Recursive Coin Optimization Using Table Lookup
# Used memoization/caching with [0]*64
def recDC(coinValueList, change, knownResults):
    minCoins = change
    # base case, change value is of a coin
    if change in coinValueList:
       knownResults[change] = 1
       return 1

    # memozation, we have already solved
    elif knownResults[change] > 0:
       return knownResults[change]

    else:
        #for i in [c for c in coinValueList if c <= change]: # changed to below
        coins = []
        for c in coinValueList:
            if c <= change: 
                coins.append(c)

        #iterate through each coin
        for i in coins:
            numCoins = 1 + recDC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins #save min # of coins for value


    return minCoins

print(recDC([1,5,10,25], 27, [0]*28))
print(recDC([1,5,10,25], 6, [0]*7))