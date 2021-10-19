### Level 2: Master the Linux Terminal

##### 3.3

1.  Keyboard Shortcuts:  
    ctrl + alt + t --> opens terminal  
    ctrl + d --> closes terminal  
    execute history -c --> clears entire history contents  
    ctrl + L = clears screen  
    

##### 3.5

1.  Commands are just text you type in the terminal.
2.  Commands are interpreted by the shell.
3.  Different shells can interpret the same text in different ways.
4.  The terminal is the window to the shell.
5.  Commands are case-sensitive.

##### 3.7

1.  The program (commandName) you want to use is always the first part of the command.
2.  [Command line structure](app://obsidian.md/Command%20line%20structure) commandName options inputs
3.  echo $PATH --> shows the path taken to call the program
4.  [Operand](app://obsidian.md/Operand) --> the input given to a command line.
5.  Short form is always proceeded by a dash '-'. Long form names are always proceeded by a double dash '--'.
6.  Linux command lines are case sensitive.
7.  Command = CommandName -options(allow you to modify the command's behavior) inputs.
8.  CommandName needs to be on the shell's search path.

##### 3.9 
1. The manual for Linux can be accessed using the [[man]] command. [man -k which].
2. Type in the command 'man' + '-k' + 'which' (or whatever command you are looking for). 
3. Once a list has been generated, the next form is 'man' + (the location number) + the title of the section. It should open the manual page with information about the command.
4. In a main page, if it is in square brackets, it is considered optional. 
5. Anything inside angle brackets <> is considered mandatory.
6. Anything with a pipe | means OR. 

##### 3.10
1. The "ls" command will take you to a directory. "q" will exit the directory. 
2. "h" is a  human readable. 
3. Long form commands commonly have a dash between the words. 

##### 3.12
1. Redirecting allows you to redirect the standard output of a command to something other than the terminal. 
2. Redirecting will also clear a file before adding anything else to it. So if you have a file with information you want to keep, you cannot send something else to it. In order to keep the redirection from truncating the data in the file, you can use '>>' to keep it. 

##### 3.13
1. In order to redirect a data stream without losing the previously documented streams, you need to use >>.
2. In order to get Standard Output from a file, you need to use the "less than" sign (<) instead of the "greater than sign" used to put input into a file. 
3. The [[tty command]] gives you the file name of the terminal connected to standard output. 
4. Standard Input, Standard Output and Standard Error are Data Streams. 
5. Using redirection you can control where those streams "flow".
6. Standard Input = 0, Standard Output = 1, Standard Error = 2 

##### 3.14
1. Command Pipelines
2. [[tee command]] --> The tee command allows for the output of the command to be passed on as the input of another command while simultaneously being passed into a text file. 
3. [[xarg command]]
4. Adding the "|" between commands allows the command to pipe the output of the previous command into another command. 