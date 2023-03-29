l=[{"a":[1,2,3,4],"b":"hi",1:True},
   {"c":[1,2,3,4],"d":"hii","de":"baa",1:True}
  ]
print(l[0]["a"][2])
print(l[1].get("d"))
print(l[1].get("de","hello"))#optional value to be return if not present
print(l[1].update({"syam":"babu"}))
print(l[1])