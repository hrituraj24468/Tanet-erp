from tkinter import*
import pandas as pd
import os
from tkinter import ttk
def addcustomer():
    cust = Toplevel()
    cust.title("ADD CUSTOMER (tanet)")
    cust.geometry("800x700")
    cust.maxsize(800,700)
    cust.minsize(800,700)
    if os.path.isdir("customers")==FALSE:
        os.mkdir("customers")

    frame=Frame(cust)
    yscroll=Scrollbar(frame)
    yscroll.place(x=750,height=200)
    table1=ttk.Treeview(frame,height=5,yscrollcommand=yscroll.set,show="headings",columns=("Customer No.","Customer Name"))
    table1.column("Customer No.",anchor='center')
    table1.column("Customer Name",anchor='center')
    table1.heading("Customer No.",text='Customer No.')
    table1.heading("Customer Name",text='Customer Name')
    table1.place(x=0,y=0,width=750,height=200)
    yscroll.config(command=table1.yview)
    frame.place(x=20,y=120,width=770,height=200)
    def inserting(e):
        managedat.delete(*managedat.get_children())
        try:
            item=table1.selection()
            for i in item:
                Number=table1.item(i,'values')[0]
            data=[]
            try:
                data=pd.read_csv(f"customers/{Number}.csv")
                data=data.to_numpy()
                datas=[]
                i=0
                for datas in data:
                    prn=datas[0]
                    unt=datas[1]
                    slp=datas[2]
                    dsnt=datas[3]
                    tt=datas[4]
                    pp=datas[5]
                    date=datas[6]
                    managedat.insert("",'end',i,values=(prn,unt,slp,dsnt,tt,date))
                    i=i+1
            except:
                pass
        except:
            pass
        
    table1.bind('<ButtonRelease-1>',inserting)
    def repeat():
        try:
            table1.delete(*table1.get_children())
            datastructure=[]
            products=[]
            srno=0
            pn=""
            datastructure=pd.read_csv("Customers.csv")
            datastructure=pd.DataFrame(datastructure)
            datastructure=datastructure.to_numpy()
            for products in datastructure:
                srno=products[0]
                pn=products[1]
                table1.insert("", 'end',products,values =(srno,pn))
        except:
            pass
    repeat()    
        
    cust.focus_set()
    Logo=Label(cust,text="TANET", font="segoescript 30 bold",background='orange').place(x=0,y=0,width=800,height=50)
    customernumber=Label(cust,text="Enter Customer No.=",font="segoescript 12 ")
    customernumber.place(x=20,y=80)
    customervar=StringVar()
    customervar.set("")
    customerentry=Entry(cust,textvariable=customervar,font="segoescript 12 ")
    customerentry.place(x=180,y=80)
    customerentry.focus_set()
    def focusnext(e):
        customernamedataentry.focus_set()
    def nextfocus(e):
        entry()
            
    customerentry.bind('<Return>',focusnext)
    customername=Label(cust,text="Name=",font="segoescript 12 ")
    customername.place(x=370,y=80)
    customernamedata=StringVar()
    customernamedata.set("")
    customernamedataentry=Entry(cust,textvariable=customernamedata,font="segoescript 12 ")
    customernamedataentry.place(x=435,y=80)
    customernamedataentry.bind('<Return>',nextfocus)
    warning=Label(cust,text="Do not enter Customer data starting with 0 (zero) with name or number , this will show error while processing... :-)")
    warning.place(x=20,y=55)

    def entry(): 
            data=[]
            data.append([customervar.get(),customernamedata.get()])
            data=pd.DataFrame(data,columns=["Number","Name"])
            try:
                datas=[]
                datas=pd.read_csv("Customers.csv")
                data=datas.append(data,ignore_index=True)
                print(data)
                data.to_csv("Customers.csv",index=False)
                person=[]
                person=pd.DataFrame(person,columns=["Product Name","Unit","Sale Price","Discount","Amount","Purchase Price","Date"])
                filenam="customers/"+customervar.get()+".csv"
                print(filenam)
                person.to_csv(filenam,index=False)

            except:
                data.to_csv("Customers.csv",index=False)
                person=[]
                person=pd.DataFrame(person,columns=["Product Name","Unit","Sale Price","Discount","Amount","Purchase Price","Date"])
                filenam="customers/"+customervar.get()+".csv"
                print(filenam)
                person.to_csv(filenam,index=False)
            repeat()    
            customerentry.delete(0,END)
            customernamedataentry.delete(0,END)
            customerentry.focus_set()
    entrydata=Button(cust,text="ADD CUSTOMER",relief=GROOVE,bg='grey71',command=entry)
    entrydata.place(x=630,y=75,width=160,height=30)

    frame2=Frame(cust)
    yscolling=Scrollbar(frame2)
    yscolling.place(x=750,height=300)
    managedat=ttk.Treeview(frame2,height=5,yscrollcommand=yscolling.set , show='headings',columns=("product name","UNIT","sale price","Discount","Amount","Date"))
    managedat.column("product name",width=120,anchor='center')
    managedat.column("UNIT",width=45,anchor='center')
    managedat.column("sale price",width=80,anchor='center')
    managedat.column("Discount",width=80,anchor='center')
    managedat.column("Amount",width=80,anchor='center')
    managedat.column("Date",width=80,anchor='center')
    managedat.heading('product name',text="Product Name")
    managedat.heading('UNIT',text='UNIT')
    managedat.heading('sale price',text="Sale Price")
    managedat.heading('Discount',text="Discount")
    managedat.heading('Amount',text="Amount")
    managedat.heading('Date',text="Date")
    managedat.place(width=750,height=300)
    yscolling.config(command=managedat.yview)
    frame2.place(x=20,y=350,width=770,height=300)