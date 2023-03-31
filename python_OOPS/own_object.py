class PlayerCharacter:
  def __init__(self,name,age):
    self.name=name
    self.age=age #these are attibutes of the class
  def run(self):
    print("running")
    return "done"
player1=PlayerCharacter("syam",22)
player2=PlayerCharacter("Paban",21)
#accessing the blueprint class as an instance
print(player1.name)
print(player2.run())