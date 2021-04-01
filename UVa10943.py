def count_ways(n, K):
  global dp_memo

  if(K == 1):
    return 1

  else:
    sum = 0
    for X in range(n+1):
      if(dp_memo[n-X][K-1] == -1): #Haven't traversed
        dp_memo[n-X][K-1] = count_ways(n-X, K-1)
      else:
        print("DP!")

      sum += dp_memo[n-X][K-1]

  return sum


  return something

if __name__ == "__main__":
  n = 3  #target value
  K = 4   #number of addends

  dp_memo = [[-1 for i in range(K+1)] for j in range(n+1)]
  print(count_ways(n, K))
