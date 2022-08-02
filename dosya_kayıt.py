def dosya(c,x):
    dosya=open("C:/Users/kuzuc/Desktop/dosya işlem/dosya.txt","a")
    dosya.write("İsim=%s Soyisim=%s\n"%(c,x))
    dosya.close()
    print("Kayıt yapılmıştır...")
    devam=input("Devam etmek istermisiniz= E/H")
    if devam=="E" and devam=="e":
        giris()
    else:
        exit
def kayıt(isim,soyisim):
    dosya(isim,soyisim)

def kayıt():
    a=input("İsminizi girin=")
    b=input("Soyisminizi girin=")
    dosya(a,b)

def kayıt_gorme():
    dos=open("C:/Users/kuzuc/Desktop/dosya işlem/dosya.txt","r")
    f=dos.read()
    print(f)
    devam=input("Devam etmek istermisiniz= E/H")
    if devam=="E" and devam=="e":
        giris()
    else:
        exit

        
            
def giris():        
    print("1>Yeni Kayıt \n2>Kayıt görme")
    giris=input("Secenegi seciniz=")
    if giris=="1":
        kayıt()
    elif giris=="2":
        kayıt_gorme()
giris()