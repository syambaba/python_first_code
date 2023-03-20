def hello(name="syam",age=22): #default param
  '''
  INfo: It simply print the args dude!!!!
  '''
  print(f'hello {name} you are {age} yr old')
hello()
hello("gnani",19)
hello("heman")
print(hello.__doc__) #for accessing doc string written in function

#clean code
def even_or_not(num):
  return num%2==0  #evaluate relational logic and returns 
                    #true or false
print(even_or_not(51))
