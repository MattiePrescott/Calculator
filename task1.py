# this compiles my code into a function to help repetition of the code
def calculation():

    # this creates a file for the user input equations to be stored
    equations = open("equations.txt","a+")

    # user input for first number. 
    no_1 = ""
    while no_1 is not int:
        try:
            no_1 = int(input("Please enter a number : \n"))
            break
        except ValueError:
            print("invalid entry : \n ")

    # user input for second number and protects against invalid characters
    no_2 = ""
    while no_2 is not int:
        try:
            no_2 = int(input("Please enter a number : \n"))
            break
        except ValueError:
            print("invalid entry : \n ")

    '''
      takes user input operator to compleat the equation and output the result.
      it also writes and stores the equation and answer into a text file.
      makes use of try and except to stop input errors coming from the user and zero division errors.

      '''
    while True:
        try:
            operator = input("Please enter a operator, either + - / * : \n")
            if operator == "+":
                print(no_1 + no_2)
                equations.write("\n"+str(no_1)+"+"+str(no_2)+"="+str(no_1+no_2))
                equations.close()
                break
            if operator == "-":
                print(no_1 - no_2)
                equations.write("\n"+str(no_1)+"-"+str(no_2)+"="+str(no_1-no_2))
                equations.close()
                break
            if operator == "*":
                print(no_1 * no_2)
                equations.write("\n"+str(no_1)+"*"+str(no_2)+"="+str(no_1*no_2))
                equations.close()
                break
            if operator == "/":
                print(no_1 / no_2)
                equations.write("\n"+str(no_1)+"/"+str(no_2)+"="+str(no_1/no_2))
                equations.close()
                break
            if operator != "+" and operator != "-" and operator != "*" and operator != "/":
                print("Invalid Entry")
        except ZeroDivisionError:
             print("Can not divide a number by 0! \n")
    
    # this block of code asks user if they want to repeat the code again for more equations or access and read the text file containing all previous equations
    while True:
        restart = input("to continue with the calculator enter 'continue' or to read equations enter 'read' or to quit enter 'exit': \n").lower()
        if restart != "continue" and restart != "read" and restart != "exit":
            print("Invalid entry! \n")
        elif restart == "continue":
              calculation()
        elif restart == "exit":
            exit()
        else:
            if restart == "read":
                 enter_file = input("Please enter file name equations.txt : \n").lower()
            if enter_file == "equations.txt":
                file = (open(enter_file, "r"))
                data = (file.read())
                print(data)
                exit()
            elif enter_file != "equations.txt":
                 print("Invalid file name try equations.txt \n")
   
# this starts the code calling the definition the code runs in.              
calculation()