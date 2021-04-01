max1d = [ -50,  2, -6,  20]

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

print(max_leftsub, max_rightsub, max_sum)
