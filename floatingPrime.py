def floatingPrime():
    threeStr = ''
    check = False
    floatingPrime = 1
    while(floatingPrime != 0):
        floatingPrime = float(input())
        
        if(floatingPrime >= 1 and floatingPrime <= 10):
            floatingPrime = str(floatingPrime).replace(".","")
        
            if(len(floatingPrime) <= 12 and len(floatingPrime) >= 3):
                for i in floatingPrime[0:4]:
                    threeStr += i
                    print(threeStr)
                    if(int(threeStr) > 1):
                        for j in range(2,int(threeStr)):
                            if int(threeStr) % j == 0:
                                check = False
                                break
                        else:
                            check = True
                            break
                    else:
                        check = False
                            
                threeStr = ''
                print(check)
                                
            else:
                print('invalid number')
        
floatingPrime()
            
