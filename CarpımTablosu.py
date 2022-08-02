from random import randint
print("0<cıkış \n 1<kolay \n 2<orta /n 3<zor \n 5<tekrar")

        

def carp(say1,say2):
    skor=-1
    for i in range (say1,say2):
        skor+=1
        sa1=randint(say1,say2)
        sa2=randint(say1,say2)
        sonuc=sa1*sa2
        a=input("%d * %d = sonucu kaçtır="%(sa1,sa2))
        if int(sonuc)==int(a):
            print("Dogru cevap tebrikler")
            
        else:
            print("Yanlış cevap %d olacaktı skorunuz = %d.\n Tekrar deneyiniz."%(sonuc,skor))
            secıım()
            

def secıım():
    secım=input("Seçiminizi yapın=")

    if secım=="1":
        carp(1,10)
    elif secım=="2":
        carp(10,50)
    elif secım=="3":
        carp(50,250)
    elif secım=="0":
        exit
    elif secım=="5":
        secıım()
    else:
        print("Yanlış giriş yaptınız tekrar deneyiniz")
        return secıım()
secıım()