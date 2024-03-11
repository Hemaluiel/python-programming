
# i = 1 # initialize i 
# while i < 6: # condition
#     print(i)
#     i += 1 # i is equal ot i + 1, if we didnt increment this then this loop enters into infinite loop



# defining list of strings 
list1 = ["geeksforgeeks", "C++", 
         "Java", "Python", "C", "MachineLearning"] 
  
# initialises a variable 
i = 0
  
print("Printing list items\ 
 using while loop") 
size = len(list1) 
# Implement while loop to print list items 
while(i < size): 
    print(list1[i]) 
    i = i+1
  
i = 0
  
print("Printing list items\ 
 using do while loop") 
  
# Implement do while loop to print list items 
while(True): 
    print(list1[i]) 
    i = i+1
    if(i < size and len(list1[i]) < 10): 
        continue
    else: 
        break