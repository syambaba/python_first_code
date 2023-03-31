class PlayerCharacter:
  membership=True
  def __init__(self,name="unknown",age=0):
    #default attribute values if not given
    if(age>18):
      self.name=name
      self.age=age
  def shout(self):
    print(f"hell {self.name}")
player1=PlayerCharacter()
player2=PlayerCharacter("syam",22)

#print(player1.shout())
#this will give error cause for age=0 attibute 
#wil not be instantiated
print(player2.shout())
