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
    da=1*int(ik_list[1])+2*int(ik_list[2])+3*int(ik_list[3])+4*int(ik_list[4])+5*int(ik_list[5])+6*int(ik_list[6])+7*int(ik_list[7])+8*int(ik_list[8])+9*int(ik_list[9])+1*int(ik_list[10])
    print(da)
    d=da/11
    print(d)
    f=d*11
    print(f)
    h=s-f
    print(h)
    
    hhh=int(ik_list[8]+ik_list[9]+ik_list[10])
    if 1<=hhh<=10:
        haigla="kuresaare Higla"
    elif 11<=hhh<=19:
        haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21<=hhh<=220:
        haigla="ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221<=hhh<=270:
        haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271<=hhh<=370:
        haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371<=hhh<=420:
        haigla="Narva Haigla"
    elif 471<=hhh<=490:
        haigla="Pärnu Haigla"
    elif 491<=hhh<=520:
        haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 521<=hhh<=570:
        haigla="Järvamaa Haigla (Paide)"
    elif 571<=hhh<=600:
        haigla="Valga Haigla"
    elif 601<=hhh<=650:
        haigla="Viljandi Haigla"
    elif 651<=hhh<=700:
        haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla "
        print(haigla)
        if int(ik_list[0])%2==0:
            sugu="naine"
   else:
        sugu="mees"
        print(sugu)
        print(f"see in {sugu}, sünnipäev {spaev} Ta on sündinud {haigla}")
        isikukoodid.append(ik)
print(isikukoodid)
arvud=list(map(int,arvud))
arvud.sort()
print(arvud)
