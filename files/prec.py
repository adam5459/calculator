import sys
def Prec():
    def one():
        www = False
        while not www:
            try:
                x = float(input("x = ->   "))
                y = float(input("y = ->   "))
                www = True
            except ValueError:
                print("\nplease enter an integer or float\n")
                continue
        xx = x/100
        ans = xx * y
        return """
        *********************
        answer = """ + str(ans) + """
        ********************* 
        """

    def two():
        www = False
        while not www:
            try:
                x = float(input("x = ->   "))
                y = float(input("y = ->   "))
                www = True
            except ValueError:
                print("\nplease enter an integer or float\n")
                continue
        ans = 100 * float(x)/float(y)
        return """
        *********************
        answer = """ + str(ans) + """
        ********************* 
        """


    print(""" 
    ******************

    1 - what is _x_% of _y_
    
    2 - _x_ is what precent of _y_

    ******************""")

    cont = False
    while not cont:
        try:
            num = int(input("\nPlease pick a number 1-2 from the chart above.\n ->  "))
        except ValueError:
            print("-----invanid input------")
            continue
            
        if num == 1:
            print("""
            ***********************
            1 - what is _x_% of _y_
            ***********************
            """)
            print(one())
            sys.exit()
        elif num == 2:
            print("""
            ***********************
            1 - _x_ is what % of _y_
            ***********************
            """)
            print(two())
            sys.exit()
        else :
            continue
        


