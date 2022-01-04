from os import close, name, sep
from sys import displayhook
from tkinter import font, ttk
from tkinter import*
from typing import Sized
import os
from PIL import Image
from numpy import number, product
from numpy.core.fromnumeric import prod
import pandas as pd
from pandas.core.frame import DataFrame
import partyname as pyy
import addcustomer as ac
import datetime as dt
import keyboard
import testpdf

program=Tk()
program.geometry("1000x800")
program.maxsize(1000,800)
program.minsize(1000,800)
program.title("tanet")

def addfile():
    add = Toplevel()
    add.focus_set()
    add.title("ADD FILE (tanet)")
    add.geometry("900x500")
    tableframe=Frame(add)
    yscrollbar=Scrollbar(tableframe)
    yscrollbar.place(x=770,height=200)
    managedat=ttk.Treeview(tableframe,height=5 , show='headings' ,yscrollcommand=yscrollbar.set,columns=("Serial no.","product name","party name","UNIT","purchase price","sale price"))
    managedat.column("Serial no.",width=45,anchor='center')
    managedat.column("product name",width=120,anchor='center')
    managedat.column("party name",width=80,anchor='center')
    managedat.column("UNIT",width=45,anchor='center')
    managedat.column("purchase price",width=80,anchor='center')
    managedat.column("sale price",width=80,anchor='center')
    managedat.heading('Serial no.',text="Sr no.")
    managedat.heading('product name',text="Product Name")
    managedat.heading('party name',text="Party Name")
    managedat.heading('UNIT',text='UNIT')
    managedat.heading('purchase price',text="Purchase Price")
    managedat.heading('sale price',text="Sale Price")
    yscrollbar.config(command=managedat.yview)
    managedat.place(width=770,height=200)
    tableframe.place(x=30,y=200,width=800,height=200)
    try:
        
        datastructure=[]
        products=[]
        srno=""
        pn=""
        prn=""
        pp=0
        sp=0
        ut=0
        datastructure=pd.read_csv("Product available.csv")
        datastructure=pd.DataFrame(datastructure)
        datastructure=datastructure.to_numpy()
        for products in datastructure:
            srno=products[0]
            pn=products[1]
            prn=products[2]
            pp=products[4]
            sp=products[5]
            ut=products[3]
            managedat.insert("", 'end',products,values =(srno,pn,prn,ut,pp,sp))
    except:
        pass
    def newparty():
        def again():
            try:
                managedat.delete(*managedat.get_children())
                file=open("party.txt","r")
                z=len(file.readlines())
                file.close()
                file=open("party.txt","r")
                for i in range(0,z):
                    a=file.readline()
                    b,c=a.split(sep="^")
                    managedat.insert("", 'end',i,values =(i,b,c)) 
                file.close()
            except:
                    pass    
        
        party=Toplevel()
        party.focus_set()
        party.title("ADD PARTY")
        party.geometry("500x500")
        managedat=ttk.Treeview(party,height=5 , show='headings' ,columns=("Serial no.","Name","Mobile No."))
        managedat.column("Serial no.",width=45,anchor='center')
        managedat.column("Name",width=120,anchor='center')
        managedat.column("Mobile No.",width=80,anchor='center')
        managedat.heading('Serial no.',text="Sr no.")
        managedat.heading('Name',text="NAME")
        managedat.heading('Mobile No.',text="Mobile No.")
        managedat.pack(side=TOP , fill=BOTH)
        try:
            file=open("party.txt","r")
            z=len(file.readlines())
            file.close()
            file=open("party.txt","r")
            for i in range(0,z):
                a=file.readline()
                b,c=a.split(sep="^")
                managedat.insert("", 'end',i,values =(i,b,c)) 
            file.close()
        except:
            pass    
        label1=Label(party,text="TANET", font="segoescript 18 bold").pack(side=TOP,pady=25)
        partynam=Label(party,text="Enter Party Name=").pack(side=LEFT,anchor='n')
        partyname=StringVar()
        partyname=Entry(party,textvariable=partyname)
        partyname.focus_set()
        partyname.pack(side=LEFT,anchor='n')
        label3=Label(party,text="   Contact=").pack(side=LEFT,anchor='n')
        partynumber=IntVar()
        partynumber.set(value="")
        partynumber=Entry(party,textvariable=partynumber)
        partynumber.pack(side=LEFT,anchor='n')
        def process(event):
            try:
                item=managedat.selection()
                for i in item:
                    a=managedat.item(i,'values')[1]
                    b=managedat.item(i,'values')[2]
                print(a,b)
                partyname.delete(0,END)
                partyname.insert(0,a)
                partynumber.delete(0,END)
                partynumber.insert(0,b)
                
            except:
                pass    
        managedat.bind('<Button-1>',process)
        
        def adding():
            print(partyname.get(),partynumber.get())
            file=open("party.txt","a")
            file.write(partyname.get() + "^" + partynumber.get())
            file.write("\n")
            file.close()
            again()
            partyname.delete(0,END)
            partynumber.delete(0,END)
            partyname.focus_set()

        def dltparty():
            try:
                item=managedat.selection()
                for i in item:
                    a=managedat.item(i,'value')[1]
                    b=managedat.item(i,'value')[2]
                txt=a+"^"+b
                file=open("party.txt","r")
                lines=file.readlines()
                temp=open("temp.txt",'w')
                for line in lines:
                    if line!=txt:
                        temp.write(line)
                        
                file.close()
                os.remove("party.txt")
                temp.close()
                os.rename("temp.txt","party.txt")
                again()
                partyname.delete(0,END)
                partynumber.delete(0,END)
                partyname.focus_set()
            except:
                pass
                
        adbutton=Button(party,text="ADD",command=adding,relief=GROOVE)
        adbutton.place(x=100,y=250,width=150)

        dltbutton=Button(party,text="Delete Party",width=20,relief=GROOVE,command=dltparty)
        dltbutton.place(x=240,y=250)
    partybutton=Button(add,text="ADD PARTY",width=20,height=1,command=newparty ,bg='grey78' ,relief=GROOVE ).place(x=700,y=40,width=100,height=40)
    label2 = Label(add,text="TANET" , font="segoescript 24 bold" , pady=20).place(x=300,y=10,width=150,height=50)
    gstno=Label(add ,text="SERIAL NO.=").place(x=20,y=70)
    entry1=IntVar()
    entry1.set("")
    def focustonameproduct(e):
        entrynam.focus_set()
    entryser=Entry(add ,textvariable=entry1)
    entryser.focus_set()
    entryser.place(x=100,y=70,width=100,height=20)
    entryser.bind("<Return>",focustonameproduct)

    def focustopurchaseprice(e):
        purchaseprice.set("")
        purchasepriceentry.focus_set()
        
    nameproduct=Label(add ,text="Name Product=").place(x=220,y=70)
    entry2=StringVar()
    entry2.set("")
    entrynam=Entry(add,textvariable=entry2)
    entrynam.place(x=310,y=70)
    entrynam.bind("<Return>",focustopurchaseprice)
    
    options=pyy.values()
    party=Label(add,text="Party=").place(x=54,y=109)
    partyvalue=StringVar()
    partyvalue.set("JS pets")
    partyval=ttk.Combobox(add,textvariable=partyvalue,values=options)
    partyval.place(x=95,y=108,width=130,height=25)

    def focustosaleprice(e):
        salepriceentry.focus_set()
        saleprice.set("")
        
    purchase=Label(add,text="Purchase Price=")
    purchase.place(x=270,y=110)
    purchaseprice=DoubleVar()
    purchaseprice.set(100.0)
    purchasepriceentry=Entry(add,textvariable=purchaseprice,font="segoescript 12 ")
    purchasepriceentry.place(x=370,y=110,width=100)
    purchasepriceentry.bind("<Return>",focustosaleprice)
    
    def focustoentry(e):
        Addproduct.focus_set()
        keyboard.press_and_release('Space')
        

    sale=Label(add,text="Sale price=")
    sale.place(x=500,y=110)
    saleprice=DoubleVar()
    saleprice.set(150)
    salepriceentry=Entry(add,textvariable=saleprice,font="segoescript 12 ")
    salepriceentry.place(x=590,y=110)
    salepriceentry.bind("<Return>",focustoentry)
    unitvalues=[]
    unitvalues=['Piece(PCS)','KiloGram(KG)','Centimeter(CM)','Bottles(BTL)','Inches(INCH)','litre(LTR)','Tablets(TBS)','Units(UNT)']
    pieces=Label(add,text="Unit=",font="segoescript 10 ").place(x=300,y=160)
    unitpiece=StringVar()
    unitpiece.set("Piece(PCS)")
    unitpieces=ttk.Combobox(add,textvariable=unitpiece,values=unitvalues)
    unitpieces.place(x=340,y=160)
    def Addpro():
        data=[]
        data.append([entry1.get(),entry2.get(),partyvalue.get(),unitpiece.get(),purchaseprice.get(),saleprice.get()])
        data=pd.DataFrame(data,columns=["serial no.","product name","party name","UNIT","purchase price","sale price"])
        try:
            datas=[]
            datas=pd.read_csv("Product available.csv")
            data=datas.append(data,ignore_index=True)
            print(data)
            data.to_csv("Product available.csv",index=False)
            managedat.delete(*managedat.get_children())
            datastructure=[]
            products=[]
            srno=""
            pn=""
            prn=""
            pp=0
            sp=0
            ut=0
            datastructure=pd.read_csv("Product available.csv")
            datastructure=pd.DataFrame(datastructure)
            datastructure=datastructure.to_numpy()
            for products in datastructure:
                srno=products[0]
                pn=products[1]
                prn=products[2]
                pp=products[4]
                sp=products[5]
                ut=products[3]
                managedat.insert("", 'end',products,values =(srno,pn,prn,ut,pp,sp))
            entry1.set("")
            entry2.set("")
            purchaseprice.set("")
            saleprice.set("")
            partyvalue.set("JS pets")    
            unitpiece.set("Piece(PCS)")
            entryser.focus_set()
        except:
            print(data)
            data.to_csv("Product available.csv",index=False)
            managedat.delete(*managedat.get_children())
            datastructure=[]
            products=[]
            srno=""
            pn=""
            prn=""
            pp=0
            sp=0
            ut=0
            datastructure=pd.read_csv("Product available.csv")
            datastructure=pd.DataFrame(datastructure)
            datastructure=datastructure.to_numpy()
            for products in datastructure:
                srno=products[0]
                pn=products[1]
                prn=products[2]
                pp=products[3]
                sp=products[5]
                ut=products[3]
                managedat.insert("", 'end',products,values =(srno,pn,prn,ut,pp,sp))
            entry1.set("")
            entry2.set("")
            purchaseprice.set("")
            saleprice.set("")
            partyvalue.set("JS pets")    
            unitpiece.set("Piece(PCS)")    
            entryser.focus_set()
            
    Addproduct=Button(add,text="ADD PRODUCT",relief=GROOVE,background='white',command=Addpro)
    Addproduct.place(x=50,y=150,width=140,height=40)
    def delproduct():
        productname=""
        try:
            item=managedat.selection()
            for i in item:
                productname=managedat.item(i,'value')[1]
            datastructure=pd.read_csv("product available.csv")
            datastructure.drop(datastructure.index[(datastructure['product name']==productname)],axis=0,inplace=True)
            print(datastructure)
            datastructure.to_csv("product available.csv",index=False)
            managedat.delete(*managedat.get_children())
            datastructure=[]
            products=[]
            srno=""
            pn=""
            prn=""
            pp=0
            sp=0
            ut=0
            datastructure=pd.read_csv("Product available.csv")
            datastructure=pd.DataFrame(datastructure)
            datastructure=datastructure.to_numpy()
            for products in datastructure:
                srno=products[0]
                pn=products[1]
                prn=products[2]
                ut=products[3]
                pp=products[4]
                sp=products[5]
                managedat.insert("", 'end',products,values =(srno,pn,prn,ut,pp,sp))
            
        except:
            pass
    removeproduct=Button(add,text="Delete Product",relief=GROOVE,background='grey70',command=delproduct)
    removeproduct.place(x=40,y=420,width=750,height=40)

   
def pl():
    prlo = Toplevel()
    prlo.title("Profit / Loss (tanet)")
    prlo.geometry("500x500")
def howerbutton1(e):
    button1["bg"]="red"
def leavebutton1(e):
    button1["bg"]="white"    
def howerbutton2(e):
    button2["bg"]="red"
def leavebutton2(e):
    button2["bg"]="white"    
def howerbutton3(e):
    button3["bg"]="red"
def leavebutton3(e):
    button3["bg"]="grey"    

frame1= Frame(program , width=300 , height=800 , bg='Royalblue2',pady=60)
photo1=PhotoImage(file="addproduct.png")
button1=Button(frame1 , image=photo1 ,bg='white' , border=2 , command=addfile , relief=FLAT)
button1.pack(side=TOP)
photo2=PhotoImage(file="bill.png")
button2=Button(frame1 , image=photo2 ,bg='white', border=2 , command=ac.addcustomer)
button2.pack(side=BOTTOM , anchor='ne')
photo3=PhotoImage(file="pl.png")
button3=Button(frame1 , image=photo3 , border=2 , command=pl)
button3.pack(side=RIGHT)
button1.bind("<Enter>",howerbutton1)
button1.bind("<Leave>",leavebutton1)
button2.bind("<Enter>",howerbutton2)
button2.bind("<Leave>",leavebutton2)
button3.bind("<Enter>",howerbutton3)
button3.bind("<Leave>",leavebutton3)
frame1.pack(side=LEFT , anchor='e', fill=Y)

frame2= Frame(program , width=800 , height=1000 , bg='white' )
label1=Label(frame2,text='TANET' , font=("comicsans 30 bold"),bg='orange' , padx=1000).pack(side=TOP)
customernumber=Label(frame2,text="ENTER CUSTOMER NO.=",font="segoescript 12 ",background='white').place(x=20,y=110)
time=Label(frame2,text=f"Date={dt.date.today()}",font="segoescript 14 ", background='white').place(x=435,y=60)
numvar=StringVar()
numvar.set("")
numberentry=Entry(frame2,textvariable=numvar,font="segoescript 12 ", border=2)
numberentry.focus_set()
numberentry.place(x=220,y=110,height=25,width=200)
def focustoclick(e):
    nobutton.focus_set()
    keyboard.press_and_release('Space') 
numberentry.bind("<Return>",focustoclick)
def checkbutton():
    try:
        data=numvar.get()
        filename="customers/"+data+".csv"
        data=pd.read_csv(filename)
        def billing():
            numberentry["state"]=DISABLED
            nobutton["state"]=DISABLED
            customername=[]
            customername=pd.read_csv("customers.csv")
            datasss=numvar.get()
            datas=customername.loc[customername['Number']==int(datasss)]
            print(datas.values)
            textname=Label(frame2,text="Name=",font=" 10 ",background='white')
            textname.place(x=20,y=180)
            customernamevaribale=StringVar()
            customernamevaribale.set(datas.values[0][1])
            customernames=Entry(frame2,font=" 10 ",textvariable=customernamevaribale)
            customernames.place(x=100,y=180)
            customernames['state']=DISABLED
            totalamount=Label(frame2,text="Grand Total:",font=" 10 ",background='white')
            totalamount.place(x=300,y=180)
            totalamountvaribale=DoubleVar()
            totalamountvaribale.set("")
            totalamountdisplay=Entry(frame2,font=" 10 ",textvariable=totalamountvaribale)
            totalamountdisplay.place(x=420,y=180,width=120)
            totalamountdisplay['state']=DISABLED
            purchaseprice=DoubleVar()
            purchaseprice.set("")
            def customerproductsearch():
                add = Toplevel()
                add.focus_set()
                add.title("customer add (tanet)")
                add.geometry("900x550")
                tanetlabel=Label(add,text="TANET",bg='orange',font="segoescript 24 bold")
                tanetlabel.place(x=0,y=0,width=900)
                tableframe=Frame(add)
                yscrollbar=Scrollbar(tableframe)
                yscrollbar.place(x=840,height=430)
                managedata=ttk.Treeview(tableframe,height=5 , show='headings',yscrollcommand=yscrollbar.set,columns=("Serial no.","product name","party name","UNIT","sale price","purchase price"))
                managedata.column("Serial no.",width=105,anchor='center')
                managedata.column("product name",width=380,anchor='center')
                managedata.column("party name",width=130,anchor='center')
                managedata.column("UNIT",width=75,anchor='center')
                managedata.column("sale price",width=200,anchor='center')
                managedata.heading('Serial no.',text="Sr no.")
                managedata.heading('product name',text="Product Name")
                managedata.heading('party name',text="Party Name")
                managedata.heading('UNIT',text='UNIT')
                managedata.heading('sale price',text="Sale Price")
                yscrollbar.config(command=managedat.yview)
                managedata.place(width=840,height=430)
                tableframe.place(x=30,y=100,width=860,height=430)
                def tableformation(): 
                    try:
                        datastructure=[]
                        products=[]
                        srno=""
                        pn=""
                        prn=""
                        pp=0
                        sp=0
                        ut=0
                        datastructure=pd.read_csv("Product available.csv")
                        datastructure=pd.DataFrame(datastructure)
                        datastructure=datastructure.to_numpy()
                        for products in datastructure:
                            srno=products[0]
                            pn=products[1]
                            prn=products[2]
                            pp=products[4]
                            sp=products[5]
                            ut=products[3]
                            managedata.insert("", 'end',products,values =(srno,pn,prn,ut,sp,pp))
                    except:
                        pass
                def parties(e):
                    if partyvalue.get()==' ':
                        tableformation()
                        
                    else:
                        try:
                            managedata.delete(*managedata.get_children())
                            datastructure=[]
                            products=[]
                            srno=""
                            pn=""
                            prn=""
                            pp=0
                            sp=0
                            ut=0
                            partyvalues=str(partyvalue.get())
                            print(partyvalues)
                            datastructure=pd.read_csv("Product available.csv")
                            datastructure=pd.DataFrame(datastructure)
                            datastructure=datastructure.to_numpy()
                            for products in datastructure:
                                srno=products[0]
                                pn=products[1]
                                prn=products[2]
                                pp=products[4]
                                sp=products[5]
                                ut=products[3]
                                if partyvalues in prn:
                                    managedata.insert("", 'end',products,values =(srno,pn,prn,ut,sp,pp))
                        except:
                            pass    
                options=pyy.values()
                party=Label(add,text="Party:",font=" 1 ").place(x=400,y=55)
                partyvalue=StringVar()
                partyvalue.set("")
                partyval=ttk.Combobox(add,textvariable=partyvalue,font=" 1 ",values=options)
                partyval.place(x=465,y=57,width=130,height=25)
                partyval.bind("<<ComboboxSelected>>",parties)
                tableformation()
                def namedd(e):
                    if nameserialvar.get()==' ':
                        tableformation()
                    else:    
                        try:
                            managedata.delete(*managedata.get_children())
                            datastructure=[]
                            products=[]
                            srno=""
                            pn=""
                            prn=""
                            pp=0
                            sp=0
                            ut=0
                            name=str(nameserialvar.get())
                            datastructure=pd.read_csv("Product available.csv")
                            datastructure=pd.DataFrame(datastructure)
                            datastructure=datastructure.to_numpy()
                            for products in datastructure:
                                srno=products[0]
                                pn=products[1]
                                prn=products[2]
                                pp=products[4]
                                sp=products[5]
                                ut=products[3]
                                if name.lower() in str(products[1]).lower():
                                    managedata.insert("", 'end',products,values =(srno,pn,prn,ut,sp,pp))
                        except:
                            pass
                nameserial=Label(add,text="Name:",font=" 1 ")
                nameserial.place(x=40,y=55)
                nameserialvar=StringVar()
                nameserialvar.set("")
                nameserialentry=Entry(add,textvariable=nameserialvar,font=" 1 ")
                nameserialentry.place(x=105,y=55)
                nameserialentry.bind('<KeyRelease>',namedd)
                def clicked(e):
                    try:
                        item=managedata.selection()
                        for i in item:
                            prdnm=managedata.item(i,'values')[1]
                            unt=managedata.item(i,'values')[3]
                            sales=managedata.item(i,'values')[4]
                            purchase=managedata.item(i,'values')[5]
                        print(prdnm,"\t",unt,'\t',sales)
                        
                        productnamevar.set(prdnm)
                        unitvar.set(unt)
                        productmrpvar.set(sales)
                        totalpricevar.set(sales)
                        purchaseprice.set(purchase)
                        add.destroy()
                        

                    except:
                        pass
                    
                managedata.bind("<ButtonRelease-1>",clicked)        
            def hover(e):
                Customerproduct['bg']='grey71'
            def leave(e):
                Customerproduct['bg']='white'
                        
            Customerproduct=Button(frame2,text="ADD PRODUCT FOR CUSTOMER",font="segoescript 12 ",relief=GROOVE,bg='white',command=customerproductsearch)
            Customerproduct.place(x=20,y=240,width=550,height=40)
            Customerproduct.bind("<Enter>",hover)
            Customerproduct.bind("<Leave>",leave)
            Customerproduct.focus_set()
            frame3=Frame(frame2)
            scollingtable=Scrollbar(frame3)
            scollingtable.place(x=550,height=200)
            managedat=ttk.Treeview(frame3,height=5 ,yscrollcommand=scollingtable.set, show='headings',columns=("product name","UNIT","MRP","Discount","AMOUNT","PP"))
            managedat.column("product name",width=174,anchor='center')
            managedat.column("UNIT",width=95,anchor='center')
            managedat.column("MRP",width=90,anchor='center')
            managedat.column("Discount",width=90,anchor='center')
            managedat.column("AMOUNT",width=100,anchor='center')
            managedat.heading('product name',text="Product Name")
            managedat.heading('UNIT',text='UNIT')
            managedat.heading('MRP',text="MRP")
            managedat.heading('Discount',text="Discount")
            managedat.heading('AMOUNT',text="AMOUNT")
            managedat.place(width=550,height=200)
            scollingtable.config(command=managedat.yview)
            frame3.place(x=20,y=300,width=570,height=200)
            Productname=Label(frame2,text="Product name=",font=" 12 ",background='white')
            Productname.place(x=20,y=510)
            productnamevar=StringVar()
            productnamevar.set("")
            productnamedisplay=Entry(frame2,textvariable=productnamevar,font=" 10 ",state=DISABLED)
            productnamedisplay.place(x=160,y=514)
            productmrp=Label(frame2,text="MRP=",font=" 8 ",bg='white')
            productmrp.place(x=400,y=510)
            productmrpvar=DoubleVar()
            productmrpvar.set(0.0)
            productmrpdisplay=Entry(frame2,textvariable=productmrpvar,state=DISABLED,font=" 8 ",bg='white')
            productmrpdisplay.place(x=465,y=510,width=80)
            discountcalculation=Label(frame2,text="Discount%=",font=" 1 ",bg="white")
            discountcalculation.place(x=20,y=551)
            discountpervar=DoubleVar()
            def calqty():
                discountpercentage=float(discountpricevar.get())
                mrp=float(productmrpvar.get())
                qtyy=qtyvar.get()
                total=float((mrp-discountpercentage)*qtyy)
                totalpricedisplay.delete(0,END)
                totalpricedisplay.insert(0,float(int(total*100)/100))
            def changess(e):
                discountpercentage=float(discountpervar.get())
                mrp=float(productmrpvar.get())
                discountedprice=((discountpercentage)*mrp)/100
                discountpriceentry.delete(0,END)
                discountpriceentry.insert(0,float(int(discountedprice*100))/100)
                try:
                    calqty()
                except:
                    pass
            def changes():
                discountpercentage=float(discountpervar.get())
                mrp=float(productmrpvar.get())
                discountedprice=((discountpercentage)*mrp)/100
                discountpriceentry.delete(0,END)
                discountpriceentry.insert(0,float(int(discountedprice*100))/100)
                try:
                    calqty()
                except:
                    pass
            discountper=Spinbox(frame2,border=1,font=" 1 ",increment=0.5,command=changes,textvariable=discountpervar,from_=0 , to=100)            
            discountper.place(x=130,y=553,width=80,height=26)
            discountper.bind('<Return>',changess)
            discountprice=Label(frame2,text="Discount(Rs.)=",font=" 1 ",bg="white")
            discountprice.place(x=220,y=550)
            discountpricevar=DoubleVar()
            discountpricevar.set(0)
            def changesss(e):
                discountpercentage=float(discountpricevar.get())
                mrp=float(productmrpvar.get())
                discountedprice=((discountpercentage)*100)/mrp
                discountper.delete(0,END)
                discountper.insert(0,float(int(discountedprice*100))/100)
                try:
                    calqty()
                except:
                    pass
            def change():
                discountpercentage=float(discountpricevar.get())
                mrp=float(productmrpvar.get())
                discountedprice=((discountpercentage)*100)/mrp
                discountper.delete(0,END)
                discountper.insert(0,float(int(discountedprice*100))/100)
                try:
                    calqty()
                except:
                    pass
            discountpriceentry=Spinbox(frame2,border=1,from_=0,to=999999,command=change,textvariable=discountpricevar,font=" 8 ",bg='white')
            discountpriceentry.place(x=360,y=550,width=80)
            discountpriceentry.bind('<Return>',changesss)
            qty=Label(frame2,text="QTY=",font=" 1 ",bg='white')
            qty.place(x=440,y=550)
            qtyvar=IntVar()
            qtyinput=Spinbox(frame2,textvariable=qtyvar,command=calqty,from_=1,to=999,border=1,font=" 1 ",bg='white')
            qtyinput.place(x=500,y=550,width=50)
            totalprice=Label(frame2,text="TOTAL=",font=" 1 ",bg="white")
            totalprice.place(x=20,y=600)
            totalpricevar=DoubleVar()
            totalpricevar.set(0)
            totalpricedisplay=Entry(frame2,border=1,textvariable=totalpricevar,font=" 1 ",bg='white')
            totalpricedisplay.place(x=110,y=600,width=100)
            def totalpricecalculation(e):
                discounts=float(productmrpvar.get())-float(totalpricevar.get())
                discountpercentage=discounts
                discountpriceentry.delete(0,END)
                discountpriceentry.insert(0,discountpercentage)
                mrp=float(productmrpvar.get())
                discountedprice=((discountpercentage)*100)/mrp
                discountper.delete(0,END)
                discountper.insert(0,(float(int(discountedprice*100))/100))
                

            totalpricedisplay.bind("<KeyRelease>",totalpricecalculation)
            
            text=open("Name.txt",'w')
            text.write(str(customernamevaribale.get()))
            def addtable():
                try:
                    products=[]
                    name=productnamevar.get()
                    unt=unitvar.get()+"/"+str(qtyvar.get())
                    mrp=productmrpvar.get()
                    dscnt=discountpervar.get()
                    grandtotal=totalpricevar.get()
                    print(f"value of pp={purchaseprice.get()}")
                    products.append([name,unt,dscnt,grandtotal,purchaseprice.get()])
                    print(products)
                    managedat.insert("", 'end',products,values=(name,unt,mrp,dscnt,grandtotal,purchaseprice.get()))
                    alldaata=[]
                    tot=0
                    tota=0
                    for i in managedat.get_children():
                        tot=managedat.item(i)['values'][4]
                        tota=tota+float(tot)
                    print(tota)
                    totalamountvaribale.set(tota) 
                except:
                    pass    

            def addbuttonentry(e):
                addbutton['background']='white'
            def addbuttonout(e):
                addbutton['bg']='grey90'
            unit=Label(frame2,text="Unit=",bg='white',font=" 2 ")
            unit.place(x=215,y=597)
            unitvar=StringVar()
            unitvar.set("")
            unitentry=Entry(frame2,textvariable=unitvar,font=" 1 ",bg='white',state=DISABLED)
            unitentry.place(x=270,y=599,width=80)
            addbutton=Button(frame2,text="ADD PRODUCT",bg='grey90',relief=GROOVE,command=addtable)
            addbutton.place(x=370,y=593,width=200,height=40)
            addbutton.bind('<Enter>',addbuttonentry)
            addbutton.bind('<Leave>',addbuttonout)
            def deltable():
                item=managedat.selection()[0]
                managedat.delete(item)
                tot=0
                tota=0
                for i in managedat.get_children():
                    tot=managedat.item(i)['values'][4]
                    tota=tota+float(tot)
                print(tota)
                totalamountvaribale.set(tota) 
                
            def delbuttonentry(e):
                deletebutton['background']='white'
            def delbuttonout(e):
                deletebutton['bg']='red'
            deletebutton=Button(frame2,text="REMOVE PRODUCT",bg='red',relief=GROOVE,command=deltable)
            deletebutton.place(x=30,y=740,width=500,height=40)
            deletebutton.bind('<Enter>',delbuttonentry)
            deletebutton.bind('<Leave>',delbuttonout)
            def prttable():
                try:
                    i=[]
                    alldata=[]
                    for i in managedat.get_children():
                        pn,unt,slp,dsp,tt,pp=managedat.item(i)['values']
                        alldata.append([pn,unt,slp,dsp,tt,pp,str(dt.date.today())])            
                    all=pd.DataFrame(alldata,columns=["Product Name","Unit","Sale Price","Discount","Amount","Purchase Price","Date"])
                    all.to_csv("forprinting.csv",index=False)
                    try:
                        data=[]
                        data=pd.read_csv(f"customers/{numvar.get()}.csv")
                        all=data.append(all)
                        all.to_csv(f"customers/{numvar.get()}.csv",index=False)
                    except:
                        all.to_csv(f"customers/{numvar.get()}.csv",index=False)
                    try:
                        data=[]
                        data=pd.read_csv("alldataforcalulation.csv")
                        all=data.append(all)
                        all.to_csv("alldataforcalculation.csv",index=False)
                    except:
                        all.to_csv("alldataforcalculation.csv",index=False)
                    testpdf.printpdf()
                    textname.destroy()
                    customernames.destroy()
                    Customerproduct.destroy()
                    frame3.destroy()
                    Productname.destroy()
                    productnamedisplay.destroy()
                    productmrp.destroy()
                    productmrpdisplay.destroy()
                    discountcalculation.destroy()
                    discountper.destroy()
                    discountprice.destroy()
                    discountpriceentry.destroy()
                    qty.destroy()
                    qtyinput.destroy()
                    totalprice.destroy()
                    totalpricedisplay.destroy()
                    unit.destroy()
                    unitentry.destroy()
                    addbutton.destroy()
                    deletebutton.destroy()
                    printbutton.destroy()
                    numvar.set("")
                    totalamount.destroy()
                    totalamountdisplay.destroy()
                    numberentry["state"]=NORMAL
                    nobutton["state"]=NORMAL
                    os.system("doc.pdf")                 
                    numberentry.focus_set()       
                except:
                    print("exception working bro...")
                
            def prbuttonentry(e):
                printbutton['background']='white'
            def prbuttonout(e):
                printbutton['bg']='lawngreen'
            printbutton=Button(frame2,text="PRINT INVOICE",bg='lawngreen',relief=GROOVE,command=prttable)
            printbutton.place(x=30,y=640,width=500,height=90)
            printbutton.bind('<Enter>',prbuttonentry)
            printbutton.bind('<Leave>',prbuttonout)
                
        billing()

    except:
        print("exception working...")
        ac.addcustomer()
    
nobutton=Button(frame2,text="Check",command=checkbutton,relief=GROOVE)
nobutton.place(x=450,y=108,width=120,height=30)
frame2.pack(side=RIGHT , fill=Y)
program.mainloop()