def highest_even(li):
  #find evens and sort , take the last one
  even_list=[]
  for i in li:
    
    if(i%2==0):
      even_list.append(i)
      
  even_list.sort()
  
  return even_list[-1]
print(highest_even([11,2,12,3,5,]))

#when we remove the elements from list,it changes the list
#for looping may cause problem