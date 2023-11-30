import random

def get_birthdays():                                                                        # make a function get_birthdays
    myList = []                                                                             # define a black list
    for i in range(23):                                                                     # call out the range from parameters
        myList.append(random.randint(1,365))                                          # add the numbers to the list ,loops through all the number. And generate a list of 23 random numbers representing birthdays
    return myList                                                                           # returns the completed list
def is_duplicates(numbers):                                                                 # make a function is_duplicates
    for x in range(len(numbers)):                                                           # to list  all the numbers, and to make  a loop correct
        for v in range (x+1,len(numbers)):                                                  # to make a loop twice, and to continuous make a next loop numbers
            if numbers[x] == numbers[v]:                                                    # to check numbers whether same
                return True                                                                 # Found a duplicates, and if numbers have same return True
    return False                                                                            # If doesn't have duolicates numbers , return False

def main():
    class_birthday = 0                                                                      # to check the same birthdays times
    ask_user = int(input("how many times they would like to run the birthday simulation"))  # use 'int' and 'input' to ask user how many times they would like to run the birthday simulation
    for j in range(ask_user):                                                               # does a loop based
        birthdays = get_birthdays()                                                         # try to call get_birthdays function
        duplicate_found = is_duplicates(birthdays)                                          # to call is_duplicates function and return to a duplicates _found
        if duplicate_found == True:                                                         # to check  duplicate_found function whether True
            class_birthday = class_birthday +1                                              # add 1 to the variable keeping track of duplicates
    print(class_birthday,"times there were two of the same birthday")                       # to get the same birthdays times
    calculate = (class_birthday/ ask_user)*(100)                                            # to caluculte the present

    print("This is about", calculate,"percent of the time")                                 # get the percent answer



main()















