while 1:
    strInputTime = input().split(" ")
    intInputTime = [int(i) for i in strInputTime]
    
    
    day31 = [1,3,5,7,8,10,12]
    day30 = [4,6,9,11]
    
    if intInputTime[1] in day31:
        print(31)
    
    elif intInputTime[1] in day30:
        print(30)
    
    else:
        if intInputTime[0] % 4 == 0:
            print(29)
        else:
            print(28)
