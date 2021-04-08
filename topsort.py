def topog_sort(node, my_list):
  global my_graph
  global my_graph_state
  my_graph_state[node] = 'Y'

  if(len(my_graph[node]) == 0): #No children
    my_list.insert(0, node)

  else:
    for state in my_graph[node]:
      if(my_graph_state[state] == "N"): #Haven't explored
        my_list = topog_sort(state, my_list.copy())

    my_list.insert(0, node)

  return my_list




if __name__ == "__main__":

  my_graph = {'A':['D'], 'B':['D'], 'C':['A','B'], 'D':['H','G'], 'E':['A','F','D'],
              'F':['K','J'], 'G':['I'], 'H':['J','I'], 'I':['L'], 'J':['M','L'], 'K':['J'],
              'L':[], 'M':[]}

  my_graph_state = {'A':'N', 'B':'N', 'C':'N', 'D':'N', 'E':'N', 'F':'N', 'G':'N',
                    'H':'N', 'I':'N', 'J':'N', 'K':'N', 'L':'N', 'M':'N'}


  my_sorted_list = []


  for state in my_graph_state:
    if(my_graph_state[state] == "N"): #Haven't been explored
      my_sorted_list = topog_sort(state, my_sorted_list.copy())


  print(my_sorted_list)
