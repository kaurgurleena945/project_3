from combatant import combatant##import parent class 
class expert (combatant): ##creating child class 
  def __init__(self, name = None, stamina = None, strength = None, speed = None, life = None, armour = None):##set instance vars to None
    super().__init__(name, stamina, strength, speed, life)##uses super() to initialize parent instance vars 
    self.__armour = armour#initialize armour #constructor 
    

  def set_armour(self,armour):#set armour function
    self.__armour=armour

  def get_armour(self):#get armour function
    return self.__armour

  def __str__(self):##str will print info about the object...uses super() to use parent class str function and and modifies for own vars
    return super().__str__()+", Armour is %s"%self.get_armour()