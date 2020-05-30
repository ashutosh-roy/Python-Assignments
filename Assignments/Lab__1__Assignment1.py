# def validate_length(x,a):
#     if(len(x) == a):
#         return True
#     else:
#         return False

def validate_name(x):
    if(x.isspace()):
        return False
    
    else:
        i = x.split(' ')
        a = i[0]
        b = i[1]

        if( a[0].isupper() and b[0].isupper()):
            return True
        else:
            return False

def validate_cell(a,b):
    
    if((x.isDigit() == True) and (len(x) == 10)):
        return True
    else :
        return False
        
# x = False
# a = 4

# while x == False:
#     year = input("\n\tEnter the year : ")
#     x = validate_length(year,a) 
#     if((x == False) and (year[0] != '0')):
#         print("Invalid Input ! Input shouldn't begin with 0 & should be of length 4")
      

# x = False
# a = 3

# while x == False:
#     prog = input("\n\tEnter the programme : ")
#     x = validate_length(prog,a) 
    
#     if(x == False):
#         print("Input should be of length 3 !")

# x = False
# a = 4
# while x == False:
#     enum = input("\n\tEnter the enum : ")
#     x = validate_length(enum,a)
    
#     if(x == False):
#         print("Enum should be of 4 digits !")

# print("Format = {}".format(year[2:]+prog+enum))

n = int(input("Enter the no. of employees :- "))

# List Declaration
emp_id = []
emp_name = []
emp_cell = []
x = False
# Initialization For EMP_ID 
for i in range(0,n):
    while x == False:
        a = input("\n\tEnter your employee ID {} : ".format(i+1))
        x = a.isdigit() 
    
        if(x == False):
            print("Input should be a digit !")
    emp_id.append(a) 

# Initialization For EMP_NAME
for i in range(0,n):
    
    while x == False:
        a = input("\n\tEnter the name for emp {} : ".format(i+1))
        x = validate_name(a)
    
        if(x == False):
            print("First letter of 1st & Last Name should be in caps! ")
        
    emp_id.append(a) 




# # Initialization For EMP_CELL
# for i in range(0,n):
#     a = input("\n\tEnter your name employee {} : ".format(i+1))
#     emp_cell.append(a) 


