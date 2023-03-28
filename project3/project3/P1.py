from combatant import combatant 
from tough import tough ##import files and classes 
from warrior import warrior 
from expert import expert

command=-1#set command to -1 so loop works 
while True:##Never ending while loop
  print("Select which class you want to select\n1. Expert\n2. Tough\n3. Warrior \n4. Combatant Only\n\n0. Exit")##print menu
  command = input("Enter your choice: ")#get user input from input function

  if command == "0": # if choose 0 exit program
    print("Exiting")  # show message that it exits
    break # this statement exits the loop

  if command == "1": #if chose 1 make new object
    newName = input("Enter name: ")#get new name input
    newStamina = input("Enter stamina: ")#get new stamina input
    newStrength = input("Enter strength: ")#get new strength input
    newSpeed = input("Enter speed: ")#get new speed input
    newLife = input("Enter life: ")#get new life input
    newArmour = input("Enter armour: ")#get new armour input
    newExpert = expert()#makes new expert object
    newExpert.set_name(newName)#uses set functions to set newExpert objects vars to input vars 
    newExpert.set_stamina(newStamina)
    newExpert.set_strength(newStrength)
    newExpert.set_speed(newSpeed)
    newExpert.set_life(newLife)
    newExpert.set_armour(newArmour)
    print(newExpert.__str__()+", Subclass is expert")#prints info and subclass using __str__

  elif command == "2": ##else if command is 2
    newName = input("Enter name: ")##Gets new vars values from user
    newStamina = input("Enter stamina: ")
    newStrength = input("Enter strength: ")
    newSpeed = input("Enter speed: ")
    newLife = input("Enter life: ")
    newWillpower = input("Enter Willpower: ")
    newTough = tough()##makes new tough object
    newTough.set_name(newName)##uses set functions to set newExpert objects vars to input vars 
    newTough.set_stamina(newStamina)
    newTough.set_strength(newStrength)
    newTough.set_speed(newSpeed)
    newTough.set_life(newLife)
    newTough.set_willpower(newWillpower)
    print(newTough.__str__()+ ", Subclass is tough")#prints info and subclass using __str__
    

  elif command == "3": #else if command is 3 
    newName = input("Enter name: ")
    newStamina = input("Enter stamina: ")
    newStrength = input("Enter strength: ")
    newSpeed = input("Enter speed: ")##Gets new vars values from user
    newLife = input("Enter life: ")
    newRate = input("Enter rate: ")
    newWarrior = warrior()
    newWarrior.set_name(newName)
    newWarrior.set_stamina(newStamina)
    newWarrior.set_strength(newStrength)
    newWarrior.set_speed(newSpeed)##uses set functions to set newExpert objects vars to input vars 
    newWarrior.set_life(newLife)
    newWarrior.set_rate(newRate)
    print(newWarrior.__str__()+", Subclass is warrior")#prints info and subclass using __str__

  elif command == "4": #else if command is 4 
    newName = input("Enter name: ")##Gets new vars values from user
    newStamina = input("Enter stamina: ")
    newStrength = input("Enter strength: ")
    newSpeed = input("Enter speed: ")
    newLife = input("Enter life: ")
    
    newCombatant = combatant()
    newCombatant.set_name(newName)#uses set functions to set newExpert objects vars to input vars 
    newCombatant.set_stamina(newStamina)
    newCombatant.set_strength(newStrength)
    newCombatant.set_speed(newSpeed)
    newCombatant.set_life(newLife)
    print(newCombatant.__str__()+", Subclass is combatant")#prints info and subclass using __str__