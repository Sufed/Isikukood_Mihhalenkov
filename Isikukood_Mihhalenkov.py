isikukood=[] #50608167079
arvud=[]
while True:
    isikukood=input("Введите isikukood: ")
    print("!Isikukood kontroll!")
    if len(isikukood)==11 and isikukood.isdigit():
        isikukood_list=list(isikukood) #Выводим первую цифру.
        первая_цифра=isikukood_list[0] 
        print("Первая цифра:", первая_цифра)
        if первая_цифра in ["1","2","3","4","5","6"]: #Квадратные скобки нужны чтобы проверить содержутся ли эти цифры в первой букве.
            print("Isikukood is correct")
            break
        else:
            print("Isikukood on viga. Первая цифра неправильная.")
    else:
        print("Неверно написан isikukood.") #Выдаст если написать буквами или если цифр меньше чем 11 и наоборот.
#Проверка пола.
print("!Контроль пола!")
if первая_цифра in ["1","3","5"]:
    print("Пол: Мужчина.")
    if первая_цифра in ["2","4","6"]:
        print("Вы посудомойка.")
else:
    print("Вы не человек.")
#Проверка дня рождения.
print("!Контроль дня рождения!")
год=isikukood_list[1]+isikukood_list[2]
месяц=int(isikukood_list[3]+isikukood_list[4])
день=int(isikukood_list[5]+isikukood_list[6])
if (int(месяц)<1) or int(месяц)>13 or (int(день)<1 or int(день)>31):
    print(год,("."),месяц("."),день )
else:
    if первая_цифра==1 or первая_цифра==2:
        yy="18"
    elif первая_цифра==3 or первая_цифра==4:
        yy="19"
    else:
        yy="20"
    spaev=str(день)+"."+str(месяц)+"."+yy+год #ei ole 18.. 19..,20..
    print(f"Sünnipäev on:", spaev)
    print(f"Viimane number: {isikukood_list[-1]}")
da=isikukood_list[1]*1+isikukood_list[2]*2+isikukood_list[3]*3+isikukood_list[4]*4+isikukood_list[5]*5+isikukood_list[6]*6+isikukood_list[7]*7+isikukood_list[8]*8+isikukood_list[9]*9+isikukood_list[1]*1

