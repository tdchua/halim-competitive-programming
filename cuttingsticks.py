def cutmystick(left, right): #Left and right are indices to the A array
  global dp_memo
  global A

  if(right == left + 1):
    return 0 #Can't cut this

  else:
    cost = A[right] - A[left]
    min = 500000 #A high number

    if(dp_memo[left][right] == 500000):
      for point in range(left+1, right):
        # print(A[point])
        length = cutmystick(left, point) + cutmystick(point, right)
        if(min > length):
          min = length
      dp_memo[left][right] = min + cost
    else:
      print("Memoized!")

    return dp_memo[left][right]

if __name__ == "__main__":
  l = 10
  n = 3
  A = [0, 2, 4, 7, l]
  B = [i for i in range(len(A))] #[0, 1, 2, 3, 4]


  dp_memo = [[500000 for i in range(len(A))] for j in range(len(A))]


  print(cutmystick(0, len(A)-1))
