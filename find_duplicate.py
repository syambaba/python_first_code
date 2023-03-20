l=["a","b","c","b","d","n","n"]
is_dup=[]
for i in range(len(l)): #iterate all items
  for j in range(len(l)):#every item is checked for duplicacy
    if(l[i]==l[j]):
      is_dup.append(l[i]) #if duplicate break the loop go for next element check
      break
print(is_dup)
  
