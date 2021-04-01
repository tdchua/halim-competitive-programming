
def fill_my_knapsack(item_no, rem_weight):
  global n
  global V
  global W
  global S
  global dp_state

  max_val = 0

  if(item_no == n):
    return 0
  if(rem_weight == 0):
    return 0

  else:
    if(W[item_no] <= rem_weight):
      max_val     += V[item_no]
      rem_weight  -= W[item_no]
    idx = item_no + 1

    max_val_traversed = 0

    while(idx < n):
      if(dp_state[idx][rem_weight] == -1): #This path hasn't been traversed
        if(W[idx] <= rem_weight):
          dp_state[idx][rem_weight] = fill_my_knapsack(idx, rem_weight)
      if(max_val_traversed < dp_state[idx][rem_weight]):
        max_val_traversed = dp_state[idx][rem_weight]

      idx += 1
    return max_val + max_val_traversed


if __name__ == "__main__":
  n = 4 #no of items
  V = [100, 70, 50, 10] #value of items
  W = [5, 4, 6, 12] #weight of items
  S = 12 #weight capacity of the knapsack

  dp_state = [[-1 for col in range(S)] for row in range(n)]
  max_val = 0
  for idx in range(n):
    val = fill_my_knapsack(idx, S)
    if(max_val < val):
      max_val = val

  print(max_val)
