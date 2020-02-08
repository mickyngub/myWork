acronym = ''
def sorting():
  global acronym
  listOfAcronym = []
  
  numOfSort = (int)(input())
  for i in range(numOfSort):
    #namesOfUni += input()+"\n"
    namesOfUni = input()
    namesOfUni.replace(" ", "")
    for e in namesOfUni:
      if(e.isupper()):
        acronym += e

    listOfAcronym.append(acronym)
    acronym = ''
  
  listOfAcronym.sort(key = len, reverse = True)
    
  for k in listOfAcronym:
    print(k)


sorting()
