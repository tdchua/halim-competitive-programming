def travel_salesman(explored_state, last_pos):
  global city_matrix
  global starting_node
  global num_cities
  global dp_memo

  if(explored_state == "1" * num_cities): #Traveled everywhere
    dp_memo[int(explored_state, 2)][last_pos] = city_matrix[last_pos][starting_node]
    return(city_matrix[last_pos][starting_node])

  else:
    i = 0
    # print(explored_state)
    min_cost = 10000

    while(i < num_cities):
      if(explored_state[i] == '0'): #Haven't traversed
        explored_state_copy = list(explored_state).copy()
        explored_state_copy[i] = '1'
        explored_state_copy = "".join(explored_state_copy)
        num_version = int(explored_state_copy, 2)

        print(explored_state_copy, last_pos, i)

        if(dp_memo[num_version][i] == -1): #Haven't traversed this state
          dp_memo[num_version][i] = travel_salesman(explored_state_copy, i)


        if(min_cost > city_matrix[last_pos][i] + dp_memo[num_version][i]):
          min_cost = city_matrix[last_pos][i] + dp_memo[num_version][i]

      i += 1


    return min_cost


if __name__ == "__main__":
  city_matrix = [ [ 0, 20, 42, 35],
                  [20,  0, 30, 34],
                  [42, 30,  0, 12],
                  [35, 34, 12,  0] ]

  explored_state = "0" * len(city_matrix[0])
  num_cities = len(city_matrix[0])
  dp_memo = [[-1 for i in range(len(city_matrix[0]))] for j in range(2**len(city_matrix[0]))]

  starting_node = 0

  i = 0
  min = 1000

  dp_memo[int("1000", 2)][0] = travel_salesman("1000", 0)
  print(dp_memo[int("1000", 2)][0])
  print(dp_memo)
