from optparse import Option


option=100
print("menu a la carta")
print("***************")
print("1-->calcular la suma")
print("2-->calcular la resta")
print("3-->calcular la multiplicacion")
print("4-->calcular la divicion")
print("***************")
while(option!=0):
    option=int(input("digita una opcion: "))
    if(option==1):
        numero1=int(input("digita un numero: "))
        numero2=int(input("digita otro numero: "))
        print(f'{numero1}+{numero2}={(numero1+numero2)}')
    elif(option==2):
        numero1=int(input("digita un numero: "))
        numero2=int(input("digita otro numero: "))
        print(f'{numero1}+{numero2}={(numero1-numero2)}')
    elif(option==3):
        numero1=int(input("digita un numero: "))
        numero2=int(input("digita otro numero: "))
        print(f'{numero1}+{numero2}={(numero1*numero2)}')
    elif(option==4):
        numero1=int(input("digita un numero: "))
        numero2=int(input("digita otro numero: "))
        print(f'{numero1}+{numero2}={(numero1/numero2)}')
    else:
        print("")


