import pypyodbc
from tkinter import *

def sql():
    #sql üzerinden kayıtlı verileri çekmek için alttaki kodları kullanıyoruz.
    db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=FURKAN;'
    'Database=Northwind;'
    'Trusted_Connection=True;'
    )
    #Aşağıdaki imlec içerisine yazılan sql kodu ile veri tabanında bulunan plaka tablosundan bulunan plakalar sütununu yazdırmaktadır. 
    imlec=db.cursor()
    imlec.execute("SELECT plaka FROM plaka")
    
    plaka=imlec.fetchall()
    #İlk for sql üzerinden çekilen verileri liste şeklinde sıralıyor('06T06',) şeklinde sıralıyor ikinci for ise listeyi açarak tek tek 06T06 şeklinde sıralamamıza yarıyor.
    for i in plaka:
        for j in i:
            #Entry içine kullanıcı tarafından girilen plaka ile veri tabanından çekilen plaka eşleşir ise name isimli def fonksiyonuna kullanıcının girdiği plaka gönderilir.
            if j==entry.get():
                name(j)
            

            
            
def name(plk):
    #sql üzerinden kayıtlı verileri çekmek için alttaki kodları kullanıyoruz.
    db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=FURKAN;'
    'Database=Northwind;'
    'Trusted_Connection=True;'
    )
    #Aşağıdaki name içerisine yazılan sql kodu ile veri tabanında bulunan kullanıcının girmiş olduğu plakanın isim ve ceza sütunları yazdırmaktadır.
    name=db.cursor()
    name.execute("SELECT isim,ceza FROM plaka WHERE plaka='"+plk+"';")
    names=name.fetchall()
    #for içerisinde sql den gelen kullanıcının girdiği plaka verilerini label üzerinden kullanıcılara aktarılması sağlanmıştır. 
    for i in names:
        lbl["text"]=plk,"/R. sahibi ve cezası(TL)=",i
tk = Tk()
tk.title("Plaka Sorgu")
tk.geometry("800x800")

lbl = Label(tk,text="Plaka=",)
lbl.pack()

entry = Entry(tk, width=40)
entry.pack()


btn = Button(tk,
            text="Sorgu",
            padx="30",pady="30",
            #Butona basıldığında sql fonksiyonu çalıştırılmaktadır.
            command=sql)
btn.pack()

lbl = Label(tk)
lbl.pack()


tk.mainloop()
            






