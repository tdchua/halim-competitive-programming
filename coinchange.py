
def min_my_coins(UseCoin, remV):
  global coinValue
  global max
  global dp_memo

  if(remV - coinValue[UseCoin] < 0):
    return max

  if(remV - coinValue[UseCoin] == 0):
    return 1

  else:
    i = 0
    remV -= coinValue[UseCoin]

    if(dp_memo[remV] == max): #Have not traversed
      if(remV == 1):
        print("1 has not been traversed")
      while(i < len(coinValue)):
        curr_coin = 1 + min_my_coins(i, remV)
        if(dp_memo[remV] > curr_coin):
          dp_memo[remV] = curr_coin

        i += 1


    return dp_memo[remV]

if __name__ == "__main__":
  V = 7
  n = 3
  coinValue = [1, 2, 5]
  max = V + 1


  dp_memo = [max for i in range(V+1)]

  i = 0
  answer = max
  while(i < len(coinValue)):
    min_coins = min_my_coins(i, V)
    if(answer > min_coins):
      answer = min_coins
      dp_memo[V] = answer

    i += 1

  print(answer)
  print(dp_memo)
