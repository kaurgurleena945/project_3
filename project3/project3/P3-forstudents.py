from combatant import combatant
from tough import tough
from warrior import warrior#import files and classes and random
from expert import expert
import random

# Create blank list

combatants = []

names,classes,stamina,strength,speed,life,extra=[],[],[],[],[],[],[] # initialize a list of names & ages = []
def read_combatants():

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
                        print(object1.__str__()+", Subclass is combatant\n")##prints info with __str__ and subclass 
                        

                if str(classes[i]) == "expert":##same as combatant above
                        object1 = expert()
                        object1.set_name(names[i])
                        object1.set_stamina(stamina[i])
                        object1.set_strength(strength[i])
                        object1.set_speed(speed[i])
                        object1.set_life(life[i])
                        object1.set_armour(extra[i-counter])##here subtracts the number of combatants that have appeared so far to get correct index
                        print(object1.__str__()+", Subclass is expert\n")

                if str(classes[i]) == "warrior":##same as if statement above
                        object1 = warrior()
                        object1.set_name(names[i])
                        object1.set_stamina(stamina[i])
                        object1.set_strength(strength[i])
                        object1.set_speed(speed[i])
                        object1.set_life(life[i])
                        object1.set_rate(extra[i-counter])
                        print(object1.__str__()+", Subclass is warrior\n")

                if str(classes[i]) == "tough":#same as if statement above
                        object1 = tough()
                        object1.set_name(names[i])
                        object1.set_stamina(stamina[i])
                        object1.set_strength(strength[i])
                        object1.set_speed(speed[i])
                        object1.set_life(life[i])
                        object1.set_willpower(extra[i-counter])
                        print(object1.__str__()+", Subclass is tough\n")

                combatants.append(object1)##add the object made to the list of objects 

read_combatants()#call combatants method


def engage(combatant1, combatant2):##engage function
        num1 = random.random()#find 2 random numbers 
        num2 = random.random()
        returnval = False#set return value to false
        if num1 > num2 and int(combatant1.get_life()) > int(combatant2.get_life()): #if this statement is true 
                returnval = True #set the return value to true 
        return returnval#return the value 
        
# Main program
f2 = open("engage.txt", "w")##open engage.txt file to write in


# Loop over 50 times
for i in range(50): 
# Pick two random combatants
        num1 = random.randrange(0, len(combatants))
        num2 = random.randrange(0, len(combatants))
        # Have them fight
        i = str(i)#set i to a string so it can be printed 
        returnval = engage(combatants[num1], combatants[num2])
        # Print result on screen and print to output file
        f2.write("Engagement {0}: Combatant {1} defeated {2}\n".format(i, combatants[num1].get_name(), combatants[num2].get_name()))
        print("Engagement %s: Combatant %s defeated %s"%(i, combatants[num1].get_name(), combatants[num2].get_name()))
        i = int(i)#set i back to int so it can be iterated over
        

f2.close()#close f2 file 
