length = int(input("Podaj długość ciągu: "))  
allNmbrs=[]
even=[]
odd=[]
sumEven=0
sumOdd=0

for element in range(length):
    print("Podaj liczbę nr ", element+1)
    allNmbrs.append(int(input()))
#print(allNmbrs)
for element in allNmbrs:
    if element % 2 == 0:
        even.append(element)
    else:
        odd.append(element)
#print("parzyste ", even )
#print("nieparzyste ", odd )
for element in even:
    sumEven+=int(element)
for element in odd:
    sumOdd+=int(element)
#print("suma even",sumEven)
#print("suma odd", sumOdd)
if sumEven > sumOdd:
    print("Suma liczb parzystych jest większa.")
elif sumEven < sumOdd:
    print("Suma liczb nieparzystych jest większa.")
else:
    print("Suma licz parzystych i nieparzystych jest taka sama.")
