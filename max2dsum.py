

if __name__ == "__main__":

  A = [ [ 2,  1, -3, -4,  5],
        [ 0,  6,  3,  4,  1],
        [ 2, -2, -1,  4, -5],
        [-3,  3,  1,  0,  3] ]


  maxR = 0
  maxL = 0
  maxUp = 0
  maxDown = 0
  maxSum = 0


  for Lcol in range(len(A[0])):
    max1d = [0 for i in range(4)]

    for Rcol in range(Lcol, len(A[0])):
      for row in range(len(A)):
        max1d[row] += A[row][Rcol]

      leftsub = 0
      rightsub = 0
      max_leftsub = 0
      max_rightsub = 0
      max_sum = 0
      current_sum = 0

      for elem in max1d:
        if(elem + current_sum <= 0):
          current_sum = 0
          leftsub = rightsub + 1
        else:
          current_sum += elem

        if(max_sum < current_sum):
          max_sum = current_sum
          max_leftsub = leftsub
          max_rightsub = rightsub

        rightsub += 1

      if(maxSum < max_sum):
        maxUp   = max_leftsub
        maxDown = max_rightsub
        maxR    = Rcol
        maxL    = Lcol
        maxSum  = max_sum

  print(maxSum)


  for row in range(maxUp, maxDown+1):
    for col in range(maxL, maxR+1):
      print(A[row][col], end = " ")
    print("")
