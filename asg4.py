
import os
def file_importer()->list:
    """
    This function reads the building.txt file and reads it and then it splits and turns is into a list of list
    """
    # this reading file format was taken from lecture slides and file i\o lab
    absolute_path = os.path.dirname(__file__)
    relative_path = "building.txt"
    full_path = os.path.join(absolute_path, relative_path)

    list = []
    file = open(full_path, "r")             
    list = file.readlines()
    file.close()                            #im closing the file

    building = []                       # my txt moves into this building
    
    for i in range(len(list)):       #this returns the length of the given list                   

        line = list[i].split("|")         # this split the list             
        list_split = str.split(list[i],"|")  # this split the "|" from my list 
        building.append(list_split)        
    return(building)         

    # Im moving the split list into a list of list using append which helps me move my split into my building variable
    #Video's that helped me with file input and output were: https://www.youtube.com/watch?v=7sFXkJvQ7Qs&t=263s
    # Video's that helped me with list of list were: https://www.youtube.com/watch?v=jE0nVl8iTFI&t=79s
    # Before starting the assignment, i shared idea's about the formatting of my functions with proff PJ perri

def clear_dice_score(building:str)-> int:
    """
    This function finds "G" and turns the number next to the "G" into a new list and scores them by adding them up
    """

    sum_of_clear_dice = 0       
    new_list = []           # created a new list so i can move the variable beside "G" into it
    
    for floor in building:   #im going into the floor of the building 
        for dice in floor:   # im going into the first index of list of list which is  [0]
         if dice[0] == "G":  # in the index[0] im looking for "G"
              new_list.append(int(dice[1])) # moving number beside "G" into a new list as a int
        sum_of_clear_dice = (sum(new_list))  # adding all the number in a new_list
    return (sum_of_clear_dice)

    #beside "G" im taking a number beside it using indexing which is [1] to identify it and moving it into a new_list variable
    # For glass scoring we need to add all the number beside it so i moved them into a new list and sum all them up.
    # for glass shared idea's with prince and akrum

def recycled_dice_score(building:str)-> int:
    """
   Finding the "R" string in the list of list and scoring them based on the how many "R" strings are there
    """
    
    sum_of_recycled_dice = 0
    
    for floor in building:   #going into the floor of the building 
        for dice in floor:   # going into a certain index of the building 
            if dice[0] == "R": # using index to find "R"
                sum_of_recycled_dice += 1  

    # counting up how many "R" are in my building.txt list of list by using loops

    if sum_of_recycled_dice == 0:
        return (0)

    if sum_of_recycled_dice == 1:
        return (2)

    elif sum_of_recycled_dice == 2:
        return(5)
    
    elif sum_of_recycled_dice == 3:
        return(10)

    elif sum_of_recycled_dice == 4:
        return(15)


    elif sum_of_recycled_dice == 5:
        return(20)

    elif sum_of_recycled_dice == 6:
        return(30)


    # depending on how many "R" my code picks up it would return the certain score based on the scoring format of "R"

    # For glass and recycled shared idea's with akrum, hassen, jordan and prince which helped me to calculate the accurate scoring for each of the dices
    # for glass and recycled shared idea's with proff steve, jordan, approve and PJ pierre 
    

def score_stone_dice(building: list) -> int:
    """
    This function finds "S" label dice in the list of list and then it scores it based on the what floor of the building in the file it is in .
    """
    score = 0
    height = len(building)
    i = 0
    while i < height:
        floor = building[i]
        if 'S' in floor:
            if i == 0:
                score = 0
            elif i == 1:
                score = 2
            elif i == 2:
                score = 3
            elif i == 3:
                score = 5
            else:
                score = 8

            # don't break here, keep iterating over the rest of the floors
        i += 1

    return score

    # for the stone function/code i worked and shared idea's with sharan and professor apoorve chokshi
    # professor apoorve helped us to explain and taught us how to solve and write the code for stone
    #Idea's also shared with steve and professor jordan for the stone function, to make sure my stone code works
    # Also got help from augusto


def wood_dice(building:list)->int:
    """
    This function scores for orange dice by looking at the dice up/down left and right
    """
    for floor in building:   #going into the floor of the building 
        for dice in floor:   # going into a certain index of the building 
            if dice[0] == "W":




                return 0


    # For the orange/wood dice i couldn't solve for it and i was more focused on taking step by step up the ladder and 
    # making sure my code can solve for glass and green and then work with stone and orange. 
    # At the moment of my coding skills i can't solve for orange but i tried my best...... 

def scoringresults(glass,recycled, stone, wood) -> None:
    """
    #scoring all the dices in a given format and it they print into the terminal
    """
    print(f"+-----------+-----+")
    print(f"|  glass    |   "+ str(glass)   +     " |")
    print(f"|  recycled |   "+ str(recycled) +    " |") 
    print(f"|  stone    |   "+ str(stone)   +     " |")  
    print(f"|  wood     |   "+ str(wood)    +     " |") 
    print(f"+===========+=====+")
    print(f"|   total   |  "+ str(glass + recycled + stone + wood)  +     " |") 
    print(f"+-----------+-----+")


    # im scoring all the dices in a format, it's asking for
    # i used if statement for the total because my (|)"pipe" would move left or right depending on how many digit my total has.
    # and to fix the problem i used if statement to fix the (|) "pipe" problem. 
    # for the formatting of the scoring result i took Idea's from: https://www.practicepython.org/solution/2016/03/17/27-tic-tac-toe-draw-solutions.html
    
    # this function only works in the terminal not in my scoring result, i had to check if my answers are right before i write to my scoring-result file





def output_exporter(building:list,clearscore:int,recycled_score:int,stone_score:int,wood_score:int )-> None:
    """
    This function writes a  function and building.txt and outputs into the scoring-result.txt all together
    """
    #join function idea taken from: https://www.w3schools.com/python/ref_string_join.asp
    scoring_output = open("scoring-results.txt", "w")
     
    new_building = []
    for floor in building:
        new_building.append("|".join(floor))   # join takes a list and turns it into a string
   

    for floor in new_building:

        scoring_output.write((f""+ str(floor)+ ""))  

    scoring_output.write(("\n"))
    scoring_output.write(("\n"))
    scoring_output.write(f"+-----------+----+\n")
    scoring_output.write(f"|  glass    | {clearscore:>2} |\n")       # newline charactors adds spaces to my scoring results
    scoring_output.write(f"|  recycled | {recycled_score:>2} |\n")   
    scoring_output.write(f"|  stone    | {stone_score:>2} |\n")
    scoring_output.write(f"|  wood     | {wood_score:>2} |\n")
    scoring_output.write(f"+===========+====+\n")
    scoring_output.write(f"|  total    | {clearscore + recycled_score + stone_score + wood_score:>2} |\n")
    scoring_output.write(f"+-----------+----+\n")
    


    scoring_output.close()
    
    #return scoring_output

    #you can only call read the file onces so i just turn the list of list into a string using join build in function

   #outputting file was learned from lecture slides and youtube videos: https://www.practicepython.org/solution/2016/03/17/27-tic-tac-toe-draw-solutions.html



def main()-> None:
    """
    This function is the def main which means all my returned values from different functions are posted over here.
    """
    building = file_importer()    # returns file_importer function

    clear_score = clear_dice_score(building)  # return the glass function
    #print("Glass:", clear_score)

    recycled_score = recycled_dice_score(building) # return the green dice
    #print("Green:", recycled_score)

    stone_score = score_stone_dice(building)  # return the stone building

    wood_score = wood_dice(building) #returns the wood building

    #scoring = scoringresults(clear_score, recycled_score, stone_score,wood_score) # returning all the scoring format function
    

    file_output = output_exporter(building,clear_score, recycled_score, stone_score,wood_score)
    
    
    
       
    
    



main()
 




