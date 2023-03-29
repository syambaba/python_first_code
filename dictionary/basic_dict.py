dict={"a":"hello","b":"syam",1:"one"}
print(dict.items())
print(dict.keys())
l=dict.values()
print(l)
for i in l:
  print(i)
print(l[0:2]) #error dict_Values not subscriptable
