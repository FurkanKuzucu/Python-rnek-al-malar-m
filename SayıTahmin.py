import random as rd
def rast(sa1,sa2,sa3):
    try:
        if sa3<=10:
            a=rd.randrange(sa1,sa2)
            print("*"*20,"\n\tTuttuğunuz sayı =%d\n"%(a),"*"*20)
            b=input("\n\tDoğrumu (E/H)=")
            if b=="E"or b=="e":
                print("*"*20,"\n\tOyun bitti kazandım tahmin=%d"%(sa3))
            elif b=="H"or b=="h":
                ta=sa3+1
                ya=input("\n\tTuttuğun sayı aşağıda mı yukarıda mı Y/A=")
                if ya=="Y"or ya=="y":
                    ysa=a+1
                    secim(ysa,sa2,ta)
                elif ya=="A"or ya=="a":
                    ysa2=a
                    secim(sa1,ysa2,ta)
            else:
                print("*"*20,"\n\tYanlış karakter tekrar deneyin")
                secim(sa1,sa2)
        else:
            print("*"*20,"\n\tBulamadım :( Tebrikler kazandın\n","*"*20)
    except ValueError:
        print("*"*20,"\n\tLütfen doğru değerler girmeye dikkat edin.")
        tutulansayı()
def secim(sayı,sayı1,tahmin):
        rast(sayı,sayı1,tahmin)
def tutulansayı():
        print("*"*20,"\n\t10 tahmin hakkım var\n","*"*20)
        tut=input("\n\t0-50 Arası bir sayı tutun=")
        try:
            int(tut)
        except ValueError:
            print("*"*20,"\tLütfen sayısal bir değer giriniz.")
            return tutulansayı()
        if int(tut)>=0 and int(tut)<=50:
            print("*"*20,"\n\tOyun başlıyorr...")
            secim(0,51,1)
        else:
            print("*"*20,"\n\tLütfen 0-50 arası tahmin yapın...")
            return tutulansayı()
tutulansayı()
