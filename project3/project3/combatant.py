
##########################PART1
class combatant: #defining class combatant
  def __init__(self, name = None, stamina = None, strength = None, speed = None, life = None):##setting instance vars to None
    self.__name = name
    self.__stamina = stamina
    self.__strength = strength##constructor for instance variables, intializes them
    self.__speed = speed 
    self.__life = life
  def get_name(self):##gets name function
    return self.__name
  
  def set_name(self,name):#sets name function
    self.__name=name
  
  def get_stamina(self):#gets stamina function
    return self.__stamina

  def set_stamina(self,stamina):#sets stamina function
    self.__stamina=stamina

  def get_strength(self):#get strength function
    return self.__strength

  def set_strength(self,strength):#sets strength function
    self.__strength=strength

  def get_speed(self):#gets speed function
    return self.__speed

  def set_speed(self,speed):#sets speed function
    self.__speed=speed

  def get_life(self):#gets life function
    return self.__life

  def set_life(self,life):#sets life function
    self.__life=life
  
  def __str__(self):##str method prints info about object as a string 
    re = "Name: "+self.get_name()+", Stamina is "+self.get_stamina()
    turn = ", Strength is "+self.get_strength()+", Speed is "+self.get_speed()+", Life: "+self.get_life()#combining two strings to 
    #whole string (done in two strings so I can see all code on laptop without scrolling to side)
    return re+turn
