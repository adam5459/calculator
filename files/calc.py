import sys
def Calc():
    print("""
        **********************
        add - addition
        sub - subtraction
        div - divistion
        mult = multiplacation
        **********************
    """)

    action_list = ["add", "sub", "div", "mult"]
    contin = False

    while not contin:
        
        try:
            first_inp = float(input("please input your first number. ->  "))
            symbol = str(input("please input your action. ->   "))
            second_inp = int(input("please input your second number. ->  "))
        except ValueError:
            print("------------Please input a valid command/number---------")
            continue

        answer = 0
        symbol = symbol.lower()
        if symbol == "add":
            answer = first_inp + second_inp
            contin = True
        elif symbol == "sub":
            answer = first_inp - second_inp
            contin = True
        elif symbol == "div":
            answer = first_inp/second_inp
            contin = True
        elif symbol == "mult":
            answer = first_inp * second_inp
            contin = True
        else:
            print("--------Please input a valid command/number. ----------")




    print("""

    *********************
        calc = """ + str(answer) + """
    ********************* 
    
      
    """)
    sys.exit()
