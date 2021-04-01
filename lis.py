if __name__ == "__main__":

  A = [-7, 10, 9, 2, 3, 8, 8, 1]
  A_LIS = [1 for i in A]

  i = 0
  j = 0
  max = 1
  max_idx = 0
  for i in range(len(A)):
    for j in range(i):
      print(A[i], A[j])
      if(A[i] > A[j] and A_LIS[i] <= A_LIS[j]):
        A_LIS[i] = A_LIS[j] + 1
        if(max < A_LIS[i]):
          max = A_LIS[i]
          max_idx = i

  print(A_LIS, max, max_idx)

  idx = max_idx
  LIS = []

  while(idx >= 0):
    if(max == A_LIS[idx]):
      LIS.append(A[idx])
      max -= 1

    idx -= 1

  print(LIS)
