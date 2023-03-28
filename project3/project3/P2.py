from combatant import combatant
from tough import tough#import files and classes 
from warrior import warrior
from expert import expert

command=-1##negative 1 so loop works 

names,stamina,strength,speed,life,extra=[],[],[],[],[],[] # initialize a list of names & ages = []
while True:##always true loop
  print("1. Read database of Combatants")
  print("0. Exit")##print menu and statement that gets info from the user 
  command = input("Enter your choice: ")

  if command == "0": # if 0 exit program
    print("Exiting")  # show message that it exits
    break # this statement exits the loop

  if command == "1":  

    names,classes,stamina,strength,speed,life,extra=[],[],[],[],[],[],[] # initialize a list of names & ages = []

    f1 = open("combatant.txt","r") # read mode
    content1=f1.readlines() # reads each line and returns list
        
    for line in content1:
      temp=line.split() # split the string
      names.append(temp[0]) #appends each index of list to proper new list
      classes.append(temp[1])
      stamina.append(temp[2])
      strength.append(temp[3])
      speed.append(temp[4])
      life.append(temp[5])
      if str(classes[-1]) != "combatant":##if isn't a combatant add an extra attribute 
        extra.append(temp[6])  
      
                           
      f1.close()##close file 
      counter = 0#set counter to 0 
      for i in range(len(names)): ##for loop to go thru list
        if str(classes[i]) == "combatant":#if combatant
          counter = counter+1##add to counter
          object1 = combatant()##make new method
          object1.set_name(names[i])##set vars from each lists index of i
          object1.set_stamina(stamina[i])
          object1.set_strength(strength[i])
          object1.set_speed(speed[i])
          object1.set_life(life[i])
          print(object1.__str__()+", Subclass is combatant")##prints info with __str__ and subclass 
                        

        if str(classes[i]) == "expert":##same as combatant above
          object1 = expert()
          object1.set_name(names[i])
          object1.set_stamina(stamina[i])
          object1.set_strength(strength[i])
          object1.set_speed(speed[i])
          object1.set_life(life[i])
          object1.set_armour(extra[i-counter])##here subtracts the number of combatants that have appeared so far to get correct index
          print(object1.__str__()+", Subclass is expert")

        if str(classes[i]) == "warrior":##same as if statement above
          object1 = warrior()
          object1.set_name(names[i])
          object1.set_stamina(stamina[i])
          object1.set_strength(strength[i])
          object1.set_speed(speed[i])
          object1.set_life(life[i])
          object1.set_rate(extra[i-counter])
          print(object1.__str__()+", Subclass is warrior")

        if str(classes[i]) == "tough":#same as if statement above
          object1 = tough()
          object1.set_name(names[i])
          object1.set_stamina(stamina[i])
          object1.set_strength(strength[i])
          object1.set_speed(speed[i])
          object1.set_life(life[i])
          object1.set_willpower(extra[i-counter])
          print(object1.__str__()+", Subclass is tough")
        
    
  break#break out of loop

  