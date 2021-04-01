def measure_water(row, col):

  global land_matrix
  global explored_matrix
  global row_len
  global col_len

  #Let's check if checking the top row doesn't exceed our bounds
  no_more_adjacent = True
  explored_matrix[row][col] = 'Y'
  answer = 1

  if(row - 1 >= 0): #N
    if(land_matrix[row-1][col] == 'W' and explored_matrix[row-1][col] == 'N'):
      no_more_adjacent = False
      answer += measure_water(row-1, col)
  if(row - 1 >= 0 and col - 1 >= 0): #NW
    if(land_matrix[row-1][col-1] == 'W' and explored_matrix[row-1][col-1] == 'N'):
      no_more_adjacent = False
      answer += measure_water(row-1, col-1)
  if(row - 1 >= 0 and col + 1 <= col_len): #NE
    if(land_matrix[row-1][col-1] == 'W' and explored_matrix[row-1][col-1] == 'N'):
      no_more_adjacent = False
      answer += measure_water(row-1, col-1)
  if(col - 1 >= 0): #W
    if(land_matrix[row][col-1] == 'W' and explored_matrix[row][col-1] == 'N'):
      no_more_adjacent = False
      answer += measure_water(row, col-1)
  if(col - 1 >= 0): #W
    if(land_matrix[row][col-1] == 'W' and explored_matrix[row][col-1] == 'N'):
      no_more_adjacent = False
      answer += measure_water(row, col-1)









  return area



if __name__ == "__main__":

  land_matrix = [ "LLLLLLLLL",
                  "LLWWLLWLL",
                  "LWWLLLLLL",
                  "LWWWLWWLL",
                  "LLLLLLLLL",
                  "LLLWWLLWL",
                  "LLWLWLLLL",
                  "LLLLLLLLL" ]

  row_len = len(land_matrix[0])
  col_len = len(land_matrix)

  explored_matrix = [['N' for i in range(len(land_matrix[0]))] for j in range(len(land_matrix))]


  print(explored)
