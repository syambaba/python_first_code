picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
for row in picture:
  for elem in row:
    if(elem==0):
      print(" ",end="")
    else:
      print("*",end="")
  print("\n")
  