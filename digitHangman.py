def digitHangman():
    
    listForHang = [int(x) for x in input("Enter twelves value 0-9: ").split()]
    indexList = [ '_' for i in range(12)]
    wrongNumberList = []
    score = 0
    if not (len(listForHang) == 12):  
        return
    for i in listForHang:
        if not (1 <= i <= 9):
            return
    print(listForHang)
    print(indexList)
    guess = 0
    while guess < 5:
        number = int(input())
        for j in range(len(listForHang)):
            
            if(listForHang[j] == number):
                indexList[j] = number
        if number not in listForHang:        
          wrongNumberList.append(number)
        print(indexList, wrongNumberList)
        guess += 1
    for g in range(len(indexList)):
        if(indexList[g] != '_'):
            score += 1
    print(score)
digitHangman()