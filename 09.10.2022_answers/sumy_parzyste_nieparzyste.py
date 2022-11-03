#pobiera od usera liczby do listy allNmbrs
def addNmbrs(nmbrs):     
    allNmbrs=[]
    for element in range(nmbrs):
        print("Podaj liczbę nr ", element+1)
        allNmbrs.append(int(input()))
    print(allNmbrs)
    return allNmbrs
#sprawdza liste allNmbrs pod kątem parzystych i nieparzystych i dodaje je do list even i odd
def parityCheck(nmbrs): 
    even=[]
    odd=[]
    nmbrs = addNmbrs(nmbrs)
    for element in nmbrs:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    print("parzyste ", even )
    print("nieparzyste ", odd )  
    return even, odd
#sumuje liczby w listach even i odd oraz porownuje te sumy
def sum(nmbrs):
    even, odd=parityCheck(nmbrs)
    sumEven=0
    sumOdd=0
    for element in even:
        sumEven+=int(element)
    for element in odd:
        sumOdd+=int(element)
    print("suma even",sumEven)
    print("suma odd", sumOdd)
    if sumEven > sumOdd:
        print("Suma liczb parzystych jest większa.")
    elif sumEven < sumOdd:
        print("Suma liczb nieparzystych jest większa.")
    else:
        print("Suma licz parzystych i nieparzystych jest taka sama.")

lenght = int(input("Podaj długość ciągu: "))  
sum(lenght)

