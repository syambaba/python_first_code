class PlayerCharacter:
  membership=True
  #class Object attribute.It is static
  def __init__(self,name,age):
    #self is for dynamic 
    if(PlayerCharacter.membership):
      self.name=name
      self.age=age #these are regular class attibutes 
  def shout(self): #these are methods
    print(f"my name is {self.name}")
   # print(f"my name is {PlayerCharacter.name}")
    #this won't work cause Class Object has no attribute name
    return "done"
player1=PlayerCharacter("syam",22)
player2=PlayerCharacter("Paban",21)
player2.attack=50
#accessing the blueprint class as an instance
print(player1)
print(player2)
print(player2.attack)
#blue prints instantiated at two diff memory 
#locations
#help(player1)

print(player1.membership)
print(player2.membership)
print(player1.shout())
