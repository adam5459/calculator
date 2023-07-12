import sys
def Avg():
    cont = False
    while not cont:
        try:
            numOfAvgs = int(input('\n Please input the number of values \n in your average.\n -> '))
            cont = True
        except ValueError :
            print("please input a float/integer")
            continue

    numbers = []
    for x in range(numOfAvgs):
        cont = False
        while not cont:
            try:
                num = float(input(str(x+1) + ' number. ->  '))
                numbers.append(num)
                cont = True
            except ValueError:
                print("please use an integer/float")
                continue
        
    total = 0
    for i in numbers:
        total += i
    answer = total/numOfAvgs
    print("""

    *********************
        avg = """ + str(answer) + """
    ********************* 
    
      
    """)
    sys.exit()
