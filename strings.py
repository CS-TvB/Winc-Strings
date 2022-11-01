# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from re import M

player_0 = "Ruud Gullit" #Assign the name "Ruud Gullit" to variable "player_0"
player_1 = "Marco van Basten" #Assign the name "Marco van Basten" to variable "player_1"
goal_0 = 32 #Assign an interger to variable "goal_0"
goal_1 = 54 #Assign an interger to variable "goal_1"

scorers = f"{player_0 + ' ' + str(goal_0) + ', ' + player_1 + ' ' + str(goal_1)}" #make a string with the + operator to report who scored when.
report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute" #put the variables in the sentences.
print (report) #print report.

player = 'Hans van Breukelen' #define a player name to the variable player.
first_space = player.find(' ') #find the first space in the name.
print (first_space) #print the location of the first space.
first_name = player[:first_space] #take the first character untill the first space.
print (first_name) #print the first name.

last_name = player[first_space +1 :] #take the place of the first space and skip that point, then go untill the end to get the full last name.
last_name_len = len(last_name) #take the last name and get the lenth of it.
print (last_name_len) #print the lenth.
print (last_name) #print the last name.

name_short = (player[0] + ". " + last_name) #take the first letter of player and + ". " last_name_player afther it.
#print (name_short) #print name_short

chantings = (first_name + "! ") #declare the first name + "! " to the variable chantings.
chant_len = (f'{chantings}'*len(first_name)) #make a full lenth chant times the characters in first_name.
chant = chant_len [:-1] #delete the last " " 
#print (chant) #print chant

good_chant = (chant[:-1] != ' ' ) #make sure the last " " has been deleted.
#print (good_chant)#print good_chant to make sure its True.
