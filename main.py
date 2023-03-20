l=["a","b","c","b","d","n","n"]
is_dup=[]
for i in range(len(l)): #iterate all items
  for j in range(i+1,len(l)):#every item is checked for duplicacy
    if(l[i]==l[j]):
      is_dup.append(l[i]) #if duplicate break the loop go for next element check
      break
print(is_dup)
#another method
some_list=["a","b","c","b","d","n","n"]
is_dup=[]
for item in some_list:
  if some_list.count(item)>1:
    if item not in is_dup:
      is_dup.append(item)
print(is_dup)
