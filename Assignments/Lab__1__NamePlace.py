print("\n\n\t\tLet's Play \n\tName_Place_Animal_Thing \n\n\t\tRules : \n\t\n\tEach   player   gets   one   chance\n\tScore = +1   For   Correct   Guess\n\n\t\tHint: \n\n\tKeep your 1st letter similar to the given ")
n = int(input("\n\tEnter the no. of users : "))

# Variable Declaration 
names = []
score = {}

# Variable Initialization 
s = 0 
win_score = 0

# Storing List Of Users as inputs 
# ------- FOR LOOP ------- 
for i in range(0,n):
    a = input("\n\tEnter your name Player {} : ".format(i+1))
    names.append(a) 

print("\n----------- Game Starts ----------- ")


for i in range(0,n):
    x = input("\n\tPlayer {} enter the character to play :".format(names[i]))
    for i in range(0,n):
        print("\n\t\tPlayer {} is playing.... \n".format(names[i]))
        
        # Initializing key for score dictionary 
        score.setdefault(names[i],[])

        a = input("\tName : ")
        # ------- IF LOOP ------- 
        if(a.startswith(x)):
            s+=1    

        a = input("\tPlace : ")
        if(a.startswith(x)):
            s+=1    
        
        a = input("\tAnimal : ")
        if(a.startswith(x)):
            s+=1    

        a = input("\tThing : ")
        if(a.startswith(x)):
            s+=1    

        score[names[i]].append(s)
        s=0
max=0
win_score = 0
win_name = 0
print("\n\n----------- ScoreBoard ----------- ")
for i in range(0,n):
    print("\t{} : {}".format(names[i],score[names[i]]))
    for j in score[names[i]]:
        max = max + j
        max_name = names[i]

    # ------- IF LOOP ------- 
    if(max > win_score):
        win_score = max
        win_name = max_name
    
    max=0
print("\n----------- Winner ----------- \n\n\t{}".format(win_name))
print("\n------------------------------\n\n")