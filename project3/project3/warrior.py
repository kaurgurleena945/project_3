from combatant import combatant ##import parent class 
class warrior (combatant): ##creating child class 
  def __init__(self, name = None, stamina = None, strength = None, speed = None, life = None, rate = None):##set instance vars to None
    self.__rate = rate#initialize rate 
    super().__init__(name, stamina, strength, speed, life)#use super to initialize parent instance vars #constructor 
    
    

  def get_rate(self):#get rate function
    return self.__rate

  def __str__(self):###str will print info about the object...uses super() to use parent class str function and and modifies for own vars
    return str(super().__str__())+", Rate is %s"%self.get_rate()

  def set_rate(self,rate):#set rate function
    self.__rate=rate