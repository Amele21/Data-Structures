# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Dynamic Programming


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
   for cents in range(change + 1):
      coinCount = cents
      newCoin = 1

      # get all the coins ex. (1, 5, 10, 25)
      coins = []
      for c in coinValueList:
        if c <= cents: 
            coins.append(c)

      #iterate through each coin
      for j in coins:
        # change the coin count if less than the current
        if minCoins[cents - j] + 1 < coinCount:
            coinCount = minCoins[cents - j] + 1
            newCoin = j

      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin

   return minCoins[change]


# Walks backwards through the table starting at change amount
# to print out the value of each coin used
def printCoins(coinsUsed, change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin


def main():
    amnt = 6
    clist = [1, 5, 10, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)
    print("coinCount:")
    print(coinCount)

main()