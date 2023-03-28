from combatant import combatant##importing combatant so child class can be made
class tough (combatant): ##creating child class 
  def __init__(self, name = None, stamina = None, strength = None, speed = None, life = None, willpower = None):##set instane vars to None
    super().__init__(name, stamina, strength, speed, life)###using super keyword to initialize parent class vars with __init__ (constructor)
    self.__willpower = willpower##initilize willpower
    

  def get_willpower(self):##get willpower function
    return self.__willpower

  def __str__(self):##str will print info about the object...uses super() to use parent class str function and and modifies for own vars
    return super().__str__()+", Willpower is %s"%self.get_willpower()

  def set_willpower(self,willpower):#set willpower function
    self.__willpower=willpower