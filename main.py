class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1=Cat("kitty",4)
cat2=Cat("cindy",5)
cat3=Cat("puppy",3)



# 2 Create a function that finds the oldest cat
def OldestCat(a,b,c):
  l=[a.age,b.age,c.age]
  l.sort()
  
  



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2