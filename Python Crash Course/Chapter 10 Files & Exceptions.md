with open('pi_digits.txt.') as file_object:  
    contents = file_object.read()  
    print(contents)

1. The [open()] function requires one argument--the name of the file you want to open. Python looks for this file in the directory where the programs that is being currently executed is stored. 
2. The keyword [with] closes the file once access to it is no longer needed. 
3.  A relative file path tells Python to look for a given location relative to the directory where the currently running program file is stored. 