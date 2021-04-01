def solve_DP(M, g_no): #M - money remaining
  if(M < 0):
    return -100000
  if(g_no == C):
    global reached
    reached = True
 
    return M
  else:
    M_least = 250
    for i in g[g_no]:
      # print(i, g_no)
      if(M >= i):
        M_copy = M - i

        if(memo[M_copy][g_no+1] == -1):
          memo[M_copy][g_no+1] = solve_DP(M_copy, g_no+1)

        if(M_least > memo[M_copy][g_no+1]):
          M_least = memo[M_copy][g_no+1]

    return M_least


if __name__ == "__main__":

  reached = False
  M = 9
  C = 3
  g = [[6, 4, 8], [5, 10], [1, 5, 3, 5]]

  #There are 200 * 20 possible states
  memo = [[-1 for i in range(25)] for j in range(210)]

  answer = solve_DP(M, 0)
  if(reached == True):
    print(M - answer)
  else:
    print("No solution")
