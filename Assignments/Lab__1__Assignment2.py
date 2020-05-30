# def caseconvert(input):
#     if(input.islower()):
#         c= input.lower()
#     else:
#         c= input.upper()

#     print("\n\n\t\tCase Conversion :- \n\n{}".format(c))

# # -------- Task 0  -------- 
# i = " hello! \n welcome to Python class on STRINGS. \n This is our 2nd L@B."
# print("\n\n\tTask 0 : Sample Text\n\n"+i)


# # -------- Task 1  -------- 
# print("\n\n\tTask 1 : String Functions ")
# a = i.splitlines()
# print("\n\t\tSplit :- \n\n{}".format(a))

# b= i.replace('.','!')
# print("\n\n\t\tReplace :- \n\n{}".format(b))

# caseconvert(i)



# -------- Task 2 -------- 
print("\n\n\tTask 2: Operators ")

#---------------- Index ----------------

s = "Hello World"
m = s[2]
print ("\n\tIndex : \n")
print("Character at index 2 = "+m)
lastchar = s[-1]
print("Last Character = "+lastchar)


#---------------- Concatentating ----------------
x='H'
y='I'
print ("\n\tConcatentation : \n"+x+y)

#---------------- Identity ----------------
x = 1
y = 2
print ("\n\tIdentity : \n")
if(x is y):
    print("Equal")
if(x is not y):
    print("Unequal")

#---------------- Logical ----------------
print ("\n\tLogical : \n")
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

#---------------- Membership ----------------
x = 'Hello world'
y = {1:'a',2:'b'}
print ("\n\tMembership : \n")
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)
print("\n\n\n")




# # -------- Task 4 -------- 
# print("\n\nHello World! Lets Play Madlib game\n")

# print("\n\t\tInput :- \n")
# color = input("\tEnter color: ")
# pluralNoun = input("\tEnter plural noun: ")
# celebrity = input("\tEnter celebrity: ")
 
# print("\n\t\tOutput :- \n")
# print("\tRoses are {}".format(color))
# print("\t{} are blue".format(pluralNoun))
# print("\tI love {}".format(celebrity))