from os import close, name, replace, sep
from sys import displayhook
from tkinter import font, ttk
from tkinter import*
from typing import Sized
import os
from PIL import Image,ImageTk 
from numpy import add, flatiter, number, product
from numpy.core.fromnumeric import prod
from numpy.lib.shape_base import split
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.indexes.api import all_indexes_same
from pandas.io.parsers import read_csv
import partyname as pyy
import addcustomer as ac
import datetime as dt
import keyboard
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.filedialog import askopenfilename



def printpdf():
    from re import split
    from tkinter.ttk import Separator
    from pandas.io.parsers import read_csv
    from reportlab.lib import colors
    from reportlab.pdfgen import canvas
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.platypus import Table , SimpleDocTemplate
    from reportlab.platypus import tables
    from reportlab.platypus.frames import Frame
    from reportlab.platypus.tables import TableStyle
    import num2words
    import os
    try:
        editdata=[]
        editdata=pd.DataFrame( read_csv("company information.csv"),columns=["filename","filenamesig","companyname","addresscol1","addresscol2","address col2"])
        editdata=editdata.to_numpy()
        editdatas=[]
        for editdatas in editdata:
            previouscompanylogo=editdatas[0]
            previouscompanysignature=editdatas[1]
            previouscompanyname=editdatas[2]
            previouscompanyaddress=editdatas[3]
            previouscompanyaddress2=editdatas[4]
            previouscompanyaddress3=editdatas[5]
    except:
        previouscompanylogo="docimage\Tanet.png"
        previouscompanysignature="docimage\signature.png"
        previouscompanyname='JS PETS AND PRODUCTS'
        previouscompanyaddress="7B-1 Ram Nagar Colony, In Front Of Kanchanpur Tower,"
        previouscompanyaddress2=" Mohaddipur, Gorakhpur"
        previouscompanyaddress3="Phone no.: 9792383230 Email: jspetsandproducts@gmail.com"

    name=previouscompanyname           
    abc=previouscompanyaddress    
    bcd=previouscompanyaddress2    
    cde=previouscompanyaddress3    
    styles = getSampleStyleSheet()
    style = styles["BodyText"]

    canv = Canvas("doc.pdf")

    Canvas.drawInlineImage(canv,image=previouscompanylogo,x=50,y=750,width=50,height=50)
    Canvas.drawRightString(canv,x=550,y=800,text=name)
    canv.setFont(psfontname='Courier',size=10)
    Canvas.drawRightString(canv,x=550,y=775,text=abc)
    Canvas.drawRightString(canv,x=550,y=765,text=bcd)
    Canvas.drawRightString(canv,x=550,y=755,text=cde)
    canv.line(0,735,800,735)
    canv.setFont(psfontname="Helvetica-Bold",size=18)
    canv.setFillColor("dodgerblue")
    Canvas.drawCentredString(canv,x=300,y=715,text="TAX INVOICE")
    canv.line(0,710,800,710)
    canv.setFont(psfontname="Times-Roman",size=14)
    canv.setFillColor("black")
    Canvas.drawString(canv,text="Bill To:",x=20,y=690)
    canv.setFont(psfontname="Times-Bold",size=14)
    Canvas.drawString(canv,text=str(dt.date.today()),x=500,y=685)
    naam=[]
    file=open("Name.txt",'r')
    naam=file.readline()
    print('\n\n')
    print(naam)
    Canvas.drawString(canv,text=str(naam),x=20,y=670)
    datas=[]
    alldata=[]
    data=pd.read_csv("forprinting.csv")
    data=data.to_numpy()
    for datas in data:
        rowdata=[]
        rowdata.append(datas[0])
        rowdata.append(datas[1])
        rowdata.append(datas[2])
        rowdata.append(datas[3])
        rowdata.append(datas[4])
        rowdata.append(datas[5])
        alldata.append(rowdata) 
    def tables():
        
        if (len(alldata))<20:
            flow=[]
            table1=[]
            tabledrawing=[["product name","UNIT","QTY","sale price","Discount%","Amount"]]
            trows=alldata
            print(len(trows))
            threader=Table([tabledrawing[0]],colWidths=[200,60,58,70,70,70])
            threader.setStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                ("BACKGROUND",(0,0),(-1,-1),colors.dodgerblue),
                ("FONT",(0,0),(-1,-1),"Times-Bold",12),
                ('TEXTCOLOR',(0,0),(-1,-1),colors.white)])
            flow.append(threader) 
            everything=(len(trows))

            for i in range(0,everything):                   
                trow=Table([trows[i-1]],colWidths=[200,60,58,70,70,70])      
                trow.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                    ("FONT",(0,0),(-1,-1),"Helvetica",10),
                    ('TEXTCOLOR',(0,0),(-1,-1),colors.black)]))
                flow.append(trow)
            
            frame=Frame(30,250,530,400,showBoundary=1,rightPadding=6,leftPadding=6)
            frame.addFromList(flow,canv)
        elif (len(alldata))>20:
            flow=[]
            table1=[]
            tabledrawing=[["product name","UNIT","QTY","sale price","Discount","Amount"]]
            trows=alldata
            print(len(trows))
            everything=(len(trows))
            threader=Table([tabledrawing[0]],colWidths=[200,60,58,70,70,70])
            threader.setStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                ("BACKGROUND",(0,0),(-1,-1),colors.dodgerblue),
                ("FONT",(0,0),(-1,-1),"Times-Bold",12),
                ('TEXTCOLOR',(0,0),(-1,-1),colors.white)])
            flow.append(threader)
            for i in range (0,everything):
                if i%20==0 and i>0:
                    frame=Frame(30,250,530,400,showBoundary=1,rightPadding=6,leftPadding=6)
                    frame.addFromList(flow,canv)
                    canv.showPage()    
                    Canvas.drawInlineImage(canv,image="docimage/Tanet.png",x=50,y=750,width=50,height=50)
                    Canvas.drawString(canv,x=400,y=800,text=name)
                    canv.setFont(psfontname='Courier',size=10)
                    Canvas.drawRightString(canv,x=550,y=775,text=abc)
                    Canvas.drawRightString(canv,x=550,y=765,text=bcd)
                    Canvas.drawRightString(canv,x=550,y=755,text=cde)
                    canv.line(0,735,800,735)
                    canv.setFont(psfontname="Helvetica-Bold",size=18)
                    canv.setFillColor("dodgerblue")
                    Canvas.drawCentredString(canv,x=300,y=715,text="TAX INVOICE")
                    canv.line(0,710,800,710)
                    canv.setFont(psfontname="Times-Roman",size=14)
                    canv.setFillColor("black")
                    Canvas.drawString(canv,text="Bill To:",x=20,y=690)
                    canv.setFont(psfontname="Times-Bold",size=14)
                    Canvas.drawString(canv,text=str(dt.date.today()),x=500,y=685)
                    naam=[]
                    file=open("Name.txt",'r')
                    naam=file.readline()
                    print('\n\n')
                    print(naam)
                    Canvas.drawString(canv,text=str(naam),x=20,y=670)
                    threader=Table([tabledrawing[0]],colWidths=[200,60,59,70,70,70])
                    threader.setStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ("BACKGROUND",(0,0),(-1,-1),colors.dodgerblue),
                        ("FONT",(0,0),(-1,-1),"Times-Bold",12),
                        ('TEXTCOLOR',(0,0),(-1,-1),colors.white)])
                    flow.append(threader)
                trow=Table([trows[i-1]],colWidths=[200,60,58,70,70,70])      
                trow.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                    ("FONT",(0,0),(-1,-1),"Helvetica",10),
                    ('TEXTCOLOR',(0,0),(-1,-1),colors.black)]))
                flow.append(trow)
            frame=Frame(30,250,530,400,showBoundary=1,rightPadding=6,leftPadding=6)
            frame.addFromList(flow,canv)
    tables()
    canv.drawCentredString(x=450,y=233,text="TOTAL=")
    canv.drawBoundary(canv,x=30,y=227,w=530,h=23)
    canv.drawBoundary(canv,x=30,y=197,w=530,h=30)
    canv.drawBoundary(canv,x=30,y=157,w=230,h=40)
    canv.drawBoundary(canv,x=30,y=97,w=230,h=60)
    canv.drawCentredString(x=450,y=200,text="Recieved:")
    data=pd.read_csv("forprinting.csv")
    data=pd.DataFrame(data,columns=["Product Name","Unit","Sale Price","Discount","Amount","Purchase Price","Date"])
    sum=str(float(int(data["Amount"].sum()*100)/100))
    canv.setFont(psfontname="Times-Roman",size=13)
    canv.drawString(x=480,y=233,text=sum)
    canv.drawString(x=480,y=200,text=sum)
    canv.setFillColor("dodgerblue")
    canv.setFont(psfontname="Times-Bold",size=15)
    canv.drawCentredString(x=450,y=150,text=f"For {name}")
    canv.setFont(psfontname="Times-Roman",size=10)
    canv.setFillColor("Black")
    canv.drawCentredString(x=450,y=80,text="Authorized Signatory")
    Canvas.drawImage(canv,image=previouscompanysignature,x=400,y=90,width=80,height=50)
    amounttowords=(float(int(data["Amount"].sum()*100)/100))
    numtoword=num2words.num2words(amounttowords)
    canv.setFillColor("dodgerblue")
    canv.setFont(psfontname="Helvetica-Bold",size=14)
    canv.drawString(x=32,y=215,text="In Words:")
    canv.setFont(psfontname="Times-Roman",size=9)
    canv.setFillColor("Black")
    canv.drawString(x=32,y=200,text=numtoword)
    canv.setFillColor("dodgerblue")
    canv.setFont(psfontname="Helvetica-Bold",size=14)
    canv.drawString(x=32,y=180,text="Payment Mode:")
    canv.setFont(psfontname="Times-Roman",size=13)
    canv.setFillColor("Black")
    canv.drawString(x=32,y=160,text="CASH")
    canv.setFillColor("dodgerblue")
    canv.setFont(psfontname="Helvetica-Bold",size=14)
    canv.drawString(x=32,y=140,text="Terms And Conditions:")
    canv.setFont(psfontname="Times-Roman",size=13)
    canv.setFillColor("Black")
    canv.drawString(x=32,y=120,text="Thanks For Purchasing With Us !")
    canv.drawString(x=32,y=107,text="VISIT AGAIN... :-)")
    canv.showPage()
    canv.save()


def quotationprintpdf():
    from re import split
    from tkinter.ttk import Separator
    from pandas.io.parsers import read_csv
    from reportlab.lib import colors
    from reportlab.pdfgen import canvas
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.platypus import Table , SimpleDocTemplate
    from reportlab.platypus import tables
    from reportlab.platypus.frames import Frame
    from reportlab.platypus.tables import TableStyle
    import num2words
    import os
    try:
        editdata=[]
        editdata=pd.DataFrame( read_csv("company information.csv"),columns=["filename","filenamesig","companyname","addresscol1","addresscol2","address col2"])
        editdata=editdata.to_numpy()
        editdatas=[]
        for editdatas in editdata:
            previouscompanylogo=editdatas[0]
            previouscompanysignature=editdatas[1]
            previouscompanyname=editdatas[2]
            previouscompanyaddress=editdatas[3]
            previouscompanyaddress2=editdatas[4]
            previouscompanyaddress3=editdatas[5]
    except:
        previouscompanylogo="docimage\Tanet.png"
        previouscompanysignature="docimage\signature.png"
        previouscompanyname='JS PETS AND PRODUCTS'
        previouscompanyaddress="7B-1 Ram Nagar Colony, In Front Of Kanchanpur Tower,"
        previouscompanyaddress2=" Mohaddipur, Gorakhpur"
        previouscompanyaddress3="Phone no.: 9792383230 Email: jspetsandproducts@gmail.com"

    name=previouscompanyname           
    abc=previouscompanyaddress    
    bcd=previouscompanyaddress2    
    cde=previouscompanyaddress3    
    styles = getSampleStyleSheet()
    style = styles["BodyText"]

    canv = Canvas("doc.pdf")

    Canvas.drawInlineImage(canv,image=previouscompanylogo,x=50,y=750,width=50,height=50)
    Canvas.drawRightString(canv,x=550,y=800,text=name)
    canv.setFont(psfontname='Courier',size=10)
    Canvas.drawRightString(canv,x=550,y=775,text=abc)
    Canvas.drawRightString(canv,x=550,y=765,text=bcd)
    Canvas.drawRightString(canv,x=550,y=755,text=cde)
    canv.line(0,735,800,735)
    canv.setFont(psfontname="Helvetica-Bold",size=18)
    canv.setFillColor("dodgerblue")
    Canvas.drawCentredString(canv,x=300,y=715,text="QUOTATION")
    canv.line(0,710,800,710)
    canv.setFont(psfontname="Times-Roman",size=14)
    canv.setFillColor("black")
    canv.setFont(psfontname="Times-Bold",size=14)
    Canvas.drawString(canv,text=str(dt.date.today()),x=500,y=685)
    datas=[]
    alldata=[]
    data=pd.read_csv("forprinting.csv")
    data=data.to_numpy()
    for datas in data:
        rowdata=[]
        rowdata.append(datas[0])
        rowdata.append(datas[1])
        rowdata.append(datas[2])
        rowdata.append(datas[3])
        rowdata.append(datas[4])
        rowdata.append(datas[5])
        alldata.append(rowdata) 
    def tables():
        
        if (len(alldata))<20:
            flow=[]
            table1=[]
            tabledrawing=[["product name","UNIT","QTY","sale price","Discount%","Amount"]]
            trows=alldata
            print(len(trows))
            threader=Table([tabledrawing[0]],colWidths=[200,60,58,70,70,70])
            threader.setStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                ("BACKGROUND",(0,0),(-1,-1),colors.dodgerblue),
                ("FONT",(0,0),(-1,-1),"Times-Bold",12),
                ('TEXTCOLOR',(0,0),(-1,-1),colors.white)])
            flow.append(threader) 
            everything=(len(trows))

            for i in range(0,everything):                   
                trow=Table([trows[i-1]],colWidths=[200,60,58,70,70,70])      
                trow.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                    ("FONT",(0,0),(-1,-1),"Helvetica",10),
                    ('TEXTCOLOR',(0,0),(-1,-1),colors.black)]))
                flow.append(trow)
            
            frame=Frame(30,250,530,400,showBoundary=1,rightPadding=6,leftPadding=6)
            frame.addFromList(flow,canv)
        elif (len(alldata))>20:
            flow=[]
            table1=[]
            tabledrawing=[["product name","UNIT","QTY","sale price","Discount","Amount"]]
            trows=alldata
            print(len(trows))
            everything=(len(trows))
            threader=Table([tabledrawing[0]],colWidths=[200,60,58,70,70,70])
            threader.setStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                ("BACKGROUND",(0,0),(-1,-1),colors.dodgerblue),
                ("FONT",(0,0),(-1,-1),"Times-Bold",12),
                ('TEXTCOLOR',(0,0),(-1,-1),colors.white)])
            flow.append(threader)
            for i in range (0,everything):
                if i%20==0 and i>0:
                    frame=Frame(30,250,530,400,showBoundary=1,rightPadding=6,leftPadding=6)
                    frame.addFromList(flow,canv)
                    canv.showPage()    
                    Canvas.drawInlineImage(canv,image="docimage/Tanet.png",x=50,y=750,width=50,height=50)
                    Canvas.drawString(canv,x=400,y=800,text=name)
                    canv.setFont(psfontname='Courier',size=10)
                    Canvas.drawRightString(canv,x=550,y=775,text=abc)
                    Canvas.drawRightString(canv,x=550,y=765,text=bcd)
                    Canvas.drawRightString(canv,x=550,y=755,text=cde)
                    canv.line(0,735,800,735)
                    canv.setFont(psfontname="Helvetica-Bold",size=18)
                    canv.setFillColor("dodgerblue")
                    Canvas.drawCentredString(canv,x=300,y=715,text="TAX INVOICE")
                    canv.line(0,710,800,710)
                    canv.setFont(psfontname="Times-Roman",size=14)
                    canv.setFillColor("black")
                    Canvas.drawString(canv,text="Bill To:",x=20,y=690)
                    canv.setFont(psfontname="Times-Bold",size=14)
                    Canvas.drawString(canv,text=str(dt.date.today()),x=500,y=685)
                    naam=[]
                    file=open("Name.txt",'r')
                    naam=file.readline()
                    print('\n\n')
                    print(naam)
                    Canvas.drawString(canv,text=str(naam),x=20,y=670)
                    threader=Table([tabledrawing[0]],colWidths=[200,60,59,70,70,70])
                    threader.setStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ("BACKGROUND",(0,0),(-1,-1),colors.dodgerblue),
                        ("FONT",(0,0),(-1,-1),"Times-Bold",12),
                        ('TEXTCOLOR',(0,0),(-1,-1),colors.white)])
                    flow.append(threader)
                trow=Table([trows[i-1]],colWidths=[200,60,58,70,70,70])      
                trow.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                    ("FONT",(0,0),(-1,-1),"Helvetica",10),
                    ('TEXTCOLOR',(0,0),(-1,-1),colors.black)]))
                flow.append(trow)
            frame=Frame(30,250,530,400,showBoundary=1,rightPadding=6,leftPadding=6)
            frame.addFromList(flow,canv)
    tables()
    canv.drawCentredString(x=450,y=233,text="TOTAL=")
    canv.drawBoundary(canv,x=30,y=227,w=530,h=23)
    canv.drawBoundary(canv,x=30,y=197,w=530,h=30)
    canv.drawBoundary(canv,x=30,y=157,w=230,h=40)
    canv.drawBoundary(canv,x=30,y=97,w=230,h=60)
    canv.drawCentredString(x=450,y=200,text="Recieved:")
    data=pd.read_csv("forprinting.csv")
    data=pd.DataFrame(data,columns=["Product Name","Unit","Sale Price","Discount","Amount","Purchase Price","Date"])
    sum=str(float(int(data["Amount"].sum()*100)/100))
    canv.setFont(psfontname="Times-Roman",size=13)
    canv.drawString(x=480,y=233,text=sum)
    canv.drawString(x=480,y=200,text=sum)
    canv.setFillColor("dodgerblue")
    canv.setFont(psfontname="Times-Bold",size=15)
    canv.drawCentredString(x=450,y=150,text=f"For {name}")
    canv.setFont(psfontname="Times-Roman",size=10)
    canv.setFillColor("Black")
    canv.drawCentredString(x=450,y=80,text="Authorized Signatory")
    Canvas.drawImage(canv,image=previouscompanysignature,x=400,y=90,width=80,height=50)
    amounttowords=(float(int(data["Amount"].sum()*100)/100))
    numtoword=num2words.num2words(amounttowords)
    canv.setFillColor("dodgerblue")
    canv.setFont(psfontname="Helvetica-Bold",size=14)
    canv.drawString(x=32,y=215,text="In Words:")
    canv.setFont(psfontname="Times-Roman",size=9)
    canv.setFillColor("Black")
    canv.drawString(x=32,y=200,text=numtoword)
    canv.setFillColor("dodgerblue")
    canv.setFont(psfontname="Helvetica-Bold",size=14)
    canv.drawString(x=32,y=180,text="Payment Mode:")
    canv.setFont(psfontname="Times-Roman",size=13)
    canv.setFillColor("Black")
    canv.drawString(x=32,y=160,text="CASH")
    canv.setFillColor("dodgerblue")
    canv.setFont(psfontname="Helvetica-Bold",size=14)
    canv.drawString(x=32,y=140,text="Terms And Conditions:")
    canv.setFont(psfontname="Times-Roman",size=13)
    canv.setFillColor("Black")
    canv.drawString(x=32,y=120,text="Thanks For Purchasing With Us !")
    canv.drawString(x=32,y=107,text="VISIT AGAIN... :-)")
    canv.showPage()
    canv.save()


program=Tk()
program.geometry("1280x720+200+2")
program.maxsize(1280,720)
program.minsize(1280,720)

program.title("tanet")

def addfile():
    button1["bg"]="white"
    button1["text"]="ADD PRODUCT\t\t\t\t  <"
    try:
        button2["bg"]="Royalblue2"
        button2["text"]="CUSTOMER\t\t\t  \t>"
        button3["bg"]="Royalblue2"
        button3["text"]="STOCK MANAGEMENT\t\t\t >"
    except:
        pass    
    try:
        hoverfiles.place(x=0,y=50,width=1000,height=800)
    except:
        pass
    addtableframe=Frame(hoverfiles,background='white')
    tableframe=Frame(addtableframe)
    yscrollbar=Scrollbar(tableframe)
    yscrollbar.place(x=782,height=280)
    managedat=ttk.Treeview(tableframe,height=5 , show='headings' ,yscrollcommand=yscrollbar.set,columns=("Serial no.","product name","party name","UNIT","purchase price","sale price","quantity"))
    managedat.column("Serial no.",width=45,anchor='center')
    managedat.column("product name",width=120,anchor='center')
    managedat.column("party name",width=80,anchor='center')
    managedat.column("UNIT",width=45,anchor='center')
    managedat.column("purchase price",width=80,anchor='center')
    managedat.column("sale price",width=80,anchor='center')
    managedat.column("quantity",width=80,anchor='center')
    managedat.heading('Serial no.',text="Sr no.")
    managedat.heading('product name',text="Product Name")
    managedat.heading('party name',text="Party Name")
    managedat.heading('UNIT',text='UNIT')
    managedat.heading('purchase price',text="Purchase Price")
    managedat.heading('sale price',text="Sale Price")
    managedat.heading('quantity',text="Quantity")
    yscrollbar.config(command=managedat.yview)
    managedat.place(width=782,height=280)
    tableframe.place(x=30,y=280,width=800,height=280)
    try:
        
        datastructure=[]
        products=[]
        srno=""
        pn=""
        prn=""
        pp=0
        sp=0
        ut=0
        qty=0
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
            qty=products[6]
            managedat.insert("", 'end',products,values =(srno,pn,prn,ut,pp,sp,qty))
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
        party.geometry("500x500+200+0")
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
    partybutton=Button(addtableframe,text="ADD PARTY",width=20,height=1,command=newparty ,bg='grey78' ,relief=GROOVE ).place(x=700,y=40,width=100,height=40)
    gstno=Label(addtableframe ,text="SERIAL NO.=",background='white').place(x=20,y=70)
    entry1=IntVar()
    entry1.set("")
    def focustonameproduct(e):
        entrynam.focus_set()
    entryser=Entry(addtableframe ,textvariable=entry1)
    entryser.focus_set()
    entryser.place(x=100,y=70,width=100,height=20)
    entryser.bind("<Return>",focustonameproduct)

    def focustopurchaseprice(e):
        purchaseprice.set("")
        purchasepriceentry.focus_set()
        
    nameproduct=Label(addtableframe ,text="Name Product=",background='white').place(x=220,y=70)
    entry2=StringVar()
    entry2.set("")
    entrynam=Entry(addtableframe,textvariable=entry2)
    entrynam.place(x=310,y=70)
    entrynam.bind("<Return>",focustopurchaseprice)
    
    options=pyy.values()
    party=Label(addtableframe,text="Party=",background='white').place(x=54,y=109)
    partyvalue=StringVar()
    partyvalue.set("JS pets")
    partyval=ttk.Combobox(addtableframe,textvariable=partyvalue,values=options)
    partyval.place(x=95,y=108,width=130,height=25)

    def focustosaleprice(e):
        salepriceentry.focus_set()
        saleprice.set("")
        
    purchase=Label(addtableframe,text="Purchase Price=",background='white')
    purchase.place(x=270,y=110)
    purchaseprice=DoubleVar()
    purchaseprice.set(100.0)
    purchasepriceentry=Entry(addtableframe,textvariable=purchaseprice,font="segoescript 12 ")
    purchasepriceentry.place(x=370,y=110,width=100)
    purchasepriceentry.bind("<Return>",focustosaleprice)
    
    def focustoentry(e):
        Addproduct.focus_set()
        keyboard.press_and_release('Space')
        

    sale=Label(addtableframe,background='white',text="Sale price=")
    sale.place(x=500,y=110)
    saleprice=DoubleVar()
    saleprice.set(150)
    salepriceentry=Entry(addtableframe,textvariable=saleprice,font="segoescript 12 ")
    salepriceentry.place(x=590,y=110)
    salepriceentry.bind("<Return>",focustoentry)
    unitvalues=[]
    unitvalues=['Piece(PCS)','KiloGram(KG)','Centimeter(CM)','Bottles(BTL)','Inches(INCH)','litre(LTR)','Tablets(TBS)','Units(UNT)']
    pieces=Label(addtableframe,text="Unit=",font="segoescript 10 ",background='white').place(x=50,y=160)
    unitpiece=StringVar()
    unitpiece.set("Piece(PCS)")
    unitpieces=ttk.Combobox(addtableframe,textvariable=unitpiece,values=unitvalues)
    unitpieces.place(x=90,y=160)
    quantitylabel=Label(addtableframe,text="Quantity=",font="segoescript 10 ",background='white')
    quantitylabel.place(x=255,y=160)
    quantitytext=DoubleVar()
    quantitytextentry=Spinbox(addtableframe,textvariable=quantitytext,from_=1,to=99999999)
    quantitytextentry.place(x=320,y=160,width=50,height=25)
    def Addpro():
        data=[]
        data.append([entry1.get(),entry2.get(),partyvalue.get(),unitpiece.get(),purchaseprice.get(),saleprice.get(),quantitytext.get()])
        data=pd.DataFrame(data,columns=["serial no.","product name","party name","UNIT","purchase price","sale price","quantity"])
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
            qty=0
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
                qty=products[6]
                managedat.insert("", 'end',products,values =(srno,pn,prn,ut,pp,sp,qty))
            entry1.set("")
            entry2.set("")
            purchaseprice.set(0)
            saleprice.set(0)
            partyvalue.set("JS pets")    
            unitpiece.set("Piece(PCS)")
            quantitytext.set(1)
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
            qty=0
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
                qty=products[6]
                managedat.insert("", 'end',products,values =(srno,pn,prn,ut,pp,sp,qty))
            entry1.set("")
            entry2.set("")
            purchaseprice.set(0)
            saleprice.set(0)
            partyvalue.set("JS pets")    
            unitpiece.set("Piece(PCS)")   
            quantitytext.set(1) 
            entryser.focus_set()
            
    Addproduct=Button(addtableframe,text="ADD PRODUCT",relief=GROOVE,background='white',command=Addpro)
    Addproduct.place(x=50,y=220,width=750,height=40)
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
            qty=0
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
                qty=products[6]
                managedat.insert("", 'end',products,values =(srno,pn,prn,ut,pp,sp,qty))
            
        except:
            pass
    def hoverfilesclose():
        button1["bg"]="Royalblue2"
        button1["text"]="ADD PRODUCT\t\t\t\t  > "
        hoverfiles.place_forget()
        addtableframe.destroy()
            
    closeaddframe=Button(addtableframe,text='X',border=0,relief=GROOVE,background='red',command=hoverfilesclose)
    closeaddframe.place(x=950,y=0,width=30,height=30)
    removeproduct=Button(addtableframe,text="Delete Product",relief=GROOVE,background='grey70',command=delproduct)
    removeproduct.place(x=40,y=580,width=750,height=40)
    addtableframe.place(x=0,y=0,width=1000,height=800)
   

def pl():
    button3["bg"]="white"
    button3["text"]="STOCK MANAGEMENT\t\t\t <"
    try:
        button1["bg"]="Royalblue2"
        button1["text"]="ADD PRODUCT\t\t\t\t  > "
        button2["bg"]="Royalblue2"
        button2["text"]="CUSTOMER\t\t\t  \t> "        
    except:
        pass
    try:
        
        hoverfiles.place(x=0,y=50,width=1000,height=800)
        stockmanagementframe=Frame(hoverfiles,background='white')
    except:
        pass
    def hoverfilesclose():
        button3["bg"]="Royalblue2"
        button3["text"]="STOCK MANAGEMENT\t\t\t >"
        hoverfiles.place_forget()
        stockmanagementframe.destroy()
    closeaddframe=Button(stockmanagementframe,text='X',border=0,relief=GROOVE,background='red',command=hoverfilesclose)
    closeaddframe.place(x=950,y=0,width=30,height=30)
    tableframe=Frame(stockmanagementframe)
    yscrollbar=Scrollbar(tableframe)
    yscrollbar.place(x=882,height=500)
    managedat=ttk.Treeview(tableframe,height=5 , show='headings' ,yscrollcommand=yscrollbar.set,columns=("Serial no.","product name","party name","UNIT","purchase price","sale price","quantity"))
    managedat.column("Serial no.",width=45,anchor='center')
    managedat.column("product name",width=120,anchor='center')
    managedat.column("party name",width=80,anchor='center')
    managedat.column("UNIT",width=45,anchor='center')
    managedat.column("purchase price",width=80,anchor='center')
    managedat.column("sale price",width=80,anchor='center')
    managedat.column("quantity",width=80,anchor='center')
    managedat.heading('Serial no.',text="Sr no.")
    managedat.heading('product name',text="Product Name")
    managedat.heading('party name',text="Party Name")
    managedat.heading('UNIT',text='UNIT')
    managedat.heading('purchase price',text="Purchase Price")
    managedat.heading('sale price',text="Sale Price")
    managedat.heading('quantity',text="Quantity")
    yscrollbar.config(command=managedat.yview)
    managedat.place(width=882,height=500)
    tableframe.place(x=30,y=120,width=900,height=500)
    try:
        datastructure=[]
        products=[]
        srno=""
        pn=""
        prn=""
        pp=0
        sp=0
        ut=0
        qty=0
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
            qty=products[6]
            managedat.insert("", 'end',products,values =(srno,pn,prn,ut,pp,sp,qty))
    except:
        pass    
            
    stockmanagementframe.place(x=0,y=0,width=1000,height=800)

def addproducttask():
    button2["bg"]="white"
    button2["text"]="CUSTOMER\t\t\t  \t<"
    try:
        button1["bg"]="Royalblue2"
        button1["text"]="ADD PRODUCT\t\t\t\t  > "
        button3["bg"]="Royalblue2"
        button3["text"]="STOCK MANAGEMENT\t\t\t >"
    except:
        pass
    try:
        hoverfiles.place(x=0,y=50,width=1000,height=800)
    except:
        pass


    if os.path.isdir("customers")==FALSE:
        os.mkdir("customers")

    alldatacustomerframe=Frame(hoverfiles,background='white')
    customerframe=Frame(alldatacustomerframe)
    yscroll=Scrollbar(customerframe)
    yscroll.place(x=750,height=200)
    table1=ttk.Treeview(customerframe,height=5,yscrollcommand=yscroll.set,show="headings",columns=("Customer No.","Customer Name"))
    table1.column("Customer No.",anchor='center')
    table1.column("Customer Name",anchor='center')
    table1.heading("Customer No.",text='Customer No.')
    table1.heading("Customer Name",text='Customer Name')
    table1.place(x=0,y=0,width=750,height=200)
    yscroll.config(command=table1.yview)
    customerframe.place(x=20,y=120,width=770,height=200)
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

    customernumber=Label(alldatacustomerframe,text="Enter Customer No.=",font="segoescript 12 ",background='white')
    customernumber.place(x=20,y=80)
    customervar=StringVar()
    customervar.set("")
    customerentry=Entry(alldatacustomerframe,textvariable=customervar,font="segoescript 12 ")
    customerentry.place(x=180,y=80)
    customerentry.focus_set()
    def focusnext(e):
        customernamedataentry.focus_set()
    def nextfocus(e):
        entry()
            
    customerentry.bind('<Return>',focusnext)
    customername=Label(alldatacustomerframe,text="Name=",font="segoescript 12 ",background='white')
    customername.place(x=370,y=80)
    customernamedata=StringVar()
    customernamedata.set("")
    customernamedataentry=Entry(alldatacustomerframe,textvariable=customernamedata,font="segoescript 12 ")
    customernamedataentry.place(x=435,y=80)
    customernamedataentry.bind('<Return>',nextfocus)
    warning=Label(alldatacustomerframe,text="Do not enter Customer data starting with 0 (zero) with name or number , this will show error while processing... :-)",background='white')
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
    entrydata=Button(alldatacustomerframe,text="ADD CUSTOMER",relief=GROOVE,bg='grey71',command=entry)
    entrydata.place(x=630,y=75,width=160,height=30)

    tableframe=Frame(alldatacustomerframe)
    yscolling=Scrollbar(tableframe)
    yscolling.place(x=750,height=300)
    managedat=ttk.Treeview(tableframe,height=5,yscrollcommand=yscolling.set , show='headings',columns=("product name","UNIT","sale price","Discount","Amount","Date"))
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
    tableframe.place(x=20,y=350,width=770,height=300)
    alldatacustomerframe.place(x=0,y=0,width=1000,height=900)
    def hoverfilesclose():
        button2["bg"]="Royalblue2"
        button2["text"]="CUSTOMER\t\t\t  \t> " 
        hoverfiles.place_forget()
        alldatacustomerframe.destroy()
            
    closeaddframe=Button(alldatacustomerframe,text='X',border=0,relief=GROOVE,background='red',command=hoverfilesclose)
    closeaddframe.place(x=950,y=0,width=30,height=30)

frame1= Frame(program , width=300 , height=800 , bg='Royalblue2',pady=60)
button1=Button(frame1 , text="ADD PRODUCT\t\t\t\t  >" ,bg='Royalblue2'  , command=addfile , relief=GROOVE)
try:
    editdata=[]
    editdata=pd.DataFrame( read_csv("company information.csv"),columns=["filename","filenamesig","companyname","addresscol1","addresscol2","address col2"])
    editdata=editdata.to_numpy()
    editdatas=[]
    for editdatas in editdata:
        previouscompanylogo=editdatas[0]
        previouscompanysignature=editdatas[1]
        previouscompanyname=editdatas[2]
        previouscompanyaddress=editdatas[3]
        previouscompanyaddress2=editdatas[4]
        previouscompanyaddress3=editdatas[5]

    load = Image.open(previouscompanylogo)
    load=load.resize((65,65),Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label(frame1,image=render)
    img.place( y=0,relx=0.5,anchor=CENTER)
    companylabel=Label(frame1,text=previouscompanyname,foreground='white',   background='Royalblue2',relief=FLAT,border=0)
    companylabel.place(y=50,relx=0.5,anchor=CENTER)   

except:
    load = Image.open("docimage\Tanet.png")
    load=load.resize((65,65),Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label(frame1,image=render)
    img.place( y=0,relx=0.5,anchor=CENTER)
    companylabel=Label(frame1,text='JS PETS AND PRODUCTS',foreground='white',   background='Royalblue2',relief=FLAT,border=0)
    companylabel.place(y=50,relx=0.5,anchor=CENTER)
def billing():
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
                textname=Label(frame20,text="Name=",font=" 10 ",background='white')
                textname.place(x=20,y=100)
                customernamevaribale=StringVar()
                customernamevaribale.set(datas.values[0][1])
                customernames=Entry(frame20,font=" 10 ",textvariable=customernamevaribale)
                customernames.place(x=100,y=100)
                customernames['state']=DISABLED
                totalamount=Label(frame20,text="Grand Total:",font=" 10 ",background='white')
                totalamount.place(x=300,y=100)
                totalamountvaribale=DoubleVar()
                totalamountvaribale.set("")
                totalamountdisplay=Entry(frame20,font=" 10 ",textvariable=totalamountvaribale)
                totalamountdisplay.place(x=420,y=100,width=120)
                totalamountdisplay['state']=DISABLED
                purchaseprice=DoubleVar()
                purchaseprice.set("")
                def customerproductsearch():
                    add = Toplevel()
                    add.focus_set()
                    add.title("customer add (tanet)")
                    add.geometry("900x550+300+150")
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
                        
                Customerproduct=Button(frame20,text="ADD PRODUCT FOR CUSTOMER",font="segoescript 12 ",relief=GROOVE,bg='white',command=customerproductsearch)
                Customerproduct.place(x=20,y=140,width=770,height=40)
                Customerproduct.bind("<Enter>",hover)
                Customerproduct.bind("<Leave>",leave)
                Customerproduct.focus_set()
                frame3=Frame(frame20)
                scollingtable=Scrollbar(frame3)
                scollingtable.place(x=750,height=200)
                managedat=ttk.Treeview(frame3,height=5 ,yscrollcommand=scollingtable.set, show='headings',columns=("product name","UNIT","QTY","MRP","Discount","AMOUNT","PP"))
                managedat.column("product name",width=228,anchor='center')
                managedat.column("UNIT",width=105,anchor='center')
                managedat.column("QTY",width=95,anchor='center')
                managedat.column("MRP",width=90,anchor='center')
                managedat.column("Discount",width=90,anchor='center')
                managedat.column("AMOUNT",width=140,anchor='center')
                managedat.heading('product name',text="Product Name")
                managedat.heading('UNIT',text='UNIT')
                managedat.heading('QTY',text='QTY')
                managedat.heading('MRP',text="MRP")
                managedat.heading('Discount',text="Discount")
                managedat.heading('AMOUNT',text="AMOUNT")
                managedat.place(width=750,height=200)
                scollingtable.config(command=managedat.yview)
                frame3.place(x=20,y=200,width=770,height=200)
                Productname=Label(frame20,text="Product name=",font=" 12 ",background='white')
                Productname.place(x=20,y=410)
                productnamevar=StringVar()
                productnamevar.set("")
                productnamedisplay=Entry(frame20,textvariable=productnamevar,font=" 10 ",state=DISABLED)
                productnamedisplay.place(x=160,y=414)
                productmrp=Label(frame20,text="MRP=",font=" 8 ",bg='white')
                productmrp.place(x=400,y=410)
                productmrpvar=DoubleVar()
                productmrpvar.set(0.0)
                productmrpdisplay=Entry(frame20,textvariable=productmrpvar,state=DISABLED,font=" 8 ",bg='white')
                productmrpdisplay.place(x=465,y=410,width=110)
                discountcalculation=Label(frame20,text="Discount%=",font=" 1 ",bg="white")
                discountcalculation.place(x=20,y=451)
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
                discountper=Spinbox(frame20,border=1,font=" 1 ",increment=0.5,command=changes,textvariable=discountpervar,from_=0 , to=100)            
                discountper.place(x=130,y=453,width=80,height=26)
                discountper.bind('<Return>',changess)
                discountprice=Label(frame20,text="Discount(Rs.)=",font=" 1 ",bg="white")
                discountprice.place(x=220,y=450)
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
                discountpriceentry=Spinbox(frame20,border=1,from_=0,to=999999,command=change,textvariable=discountpricevar,font=" 8 ",bg='white')
                discountpriceentry.place(x=360,y=450,width=80)
                discountpriceentry.bind('<Return>',changesss)
                qty=Label(frame20,text="QTY=",font=" 1 ",bg='white')
                qty.place(x=440,y=450)
                qtyvar=IntVar()
                qtyinput=Spinbox(frame20,textvariable=qtyvar,command=calqty,from_=1,to=999,border=1,font=" 1 ",bg='white')
                qtyinput.place(x=500,y=450,width=50)
                totalprice=Label(frame20,text="TOTAL=",font=" 1 ",bg="white")
                totalprice.place(x=20,y=500)
                totalpricevar=DoubleVar()
                totalpricevar.set(0)
                totalpricedisplay=Entry(frame20,border=1,textvariable=totalpricevar,font=" 1 ",bg='white')
                totalpricedisplay.place(x=110,y=500,width=100)
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
                        unt=unitvar.get()
                        productqty=qtyvar.get()
                        mrp=productmrpvar.get()
                        dscnt=discountpervar.get()
                        grandtotal=totalpricevar.get()
                        print(f"value of pp={purchaseprice.get()}")
                        products.append([name,unt,dscnt,grandtotal,purchaseprice.get()])
                        print(products)
                        managedat.insert("", 'end',products,values=(name,unt,productqty,mrp,dscnt,grandtotal,purchaseprice.get()*qtyvar.get()))
                        alldaata=[]
                        tot=0
                        tota=0
                        for i in managedat.get_children():
                            tot=managedat.item(i)['values'][5]
                            tota=tota+float(tot)
                        print(tota)
                        totalamountvaribale.set(tota) 
                        productnamevar.set("")
                        unitvar.set("")
                        productmrpvar.set(0)
                        totalpricevar.set("")
                        purchaseprice.set("")
                        totalpricevar.set(0)
                        discountpervar.set(0.0)
                        discountpricevar.set(0)
                        qtyvar.set(1)
                    except:
                        productnamevar.set("")
                        unitvar.set("")
                        productmrpvar.set("")
                        totalpricevar.set("")
                        purchaseprice.set("")   
                        totalpricevar.set(0)
                        discountpervar.set(0.0)
                        discountpricevar.set(0)

                def addbuttonentry(e):
                    addbutton['background']='white'
                def addbuttonout(e):
                    addbutton['bg']='grey90'
                unit=Label(frame20,text="Unit=",bg='white',font=" 2 ")
                unit.place(x=605,y=410)
                unitvar=StringVar()
                unitvar.set("")
                unitentry=Entry(frame20,textvariable=unitvar,font=" 1 ",bg='white',state=DISABLED)
                unitentry.place(x=660,y=410,width=80)
                addbutton=Button(frame20,text="ADD PRODUCT",bg='grey90',relief=GROOVE,command=addtable)
                addbutton.place(x=270,y=493,width=200,height=40)
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
                deletebutton=Button(frame20,text="REMOVE PRODUCT",bg='red',relief=GROOVE,command=deltable)
                deletebutton.place(x=350,y=540,width=270,height=50)
                deletebutton.bind('<Enter>',delbuttonentry)
                deletebutton.bind('<Leave>',delbuttonout)
                def prttable():
                    try:
                        i=[]
                        alldata=[]
                        for i in managedat.get_children():
                            pn,unt,qty,slp,dsp,tt,pp=managedat.item(i)['values']
                            alldata.append([pn,unt,qty,slp,dsp,tt,pp,str(dt.date.today())])            
                        all=pd.DataFrame(alldata,columns=["Product Name","Unit","QTY","Sale Price","Discount","Amount","Purchase Price","Date"])
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
                            all=pd.DataFrame(all,columns=["Product Name","Unit","QTY","Sale Price","Discount","Amount","Purchase Price","Date"])
                            all.to_csv("alldataforcalculation.csv",index=False)
                        except:
                            all.to_csv("alldataforcalculation.csv",index=False)
                        printpdf()
                        webbrowser.open("doc.pdf")           
                        openbilling()

                    except:
                        print("exception working bro...")
                
                def prbuttonentry(e):
                    printbutton['background']='white'
                def prbuttonout(e):
                    printbutton['bg']='lawngreen'
                printbutton=Button(frame20,text="PRINT INVOICE",bg='lawngreen',relief=GROOVE,command=prttable)
                printbutton.place(x=30,y=540,width=300,height=50)
                printbutton.bind('<Enter>',prbuttonentry)
                printbutton.bind('<Leave>',prbuttonout)
                
            billing()
            

        except:
            print("exception working...")
            ac.addcustomer()
    try:
        hoverfiles.place(x=0,y=50,width=1000,height=800)
    except:
        pass        


    frame20=Frame(hoverfiles,background='white')
    def hoverfilesclose():
        hoverfiles.place_forget()
        frame20.destroy()
            
    closeaddframe=Button(frame20,text='X',border=0,relief=GROOVE,background='red',command=hoverfilesclose)
    closeaddframe.place(x=950,y=0,width=30,height=30)
    customernumber=Label(frame20,text="ENTER CUSTOMER NO.=",font="segoescript 12 ",background='white').place(x=20,y=40)
    nobutton=Button(frame20,text="Check",command=checkbutton,relief=GROOVE)
    nobutton.place(x=450,y=38,width=120,height=30)
    numvar=StringVar()
    numvar.set("")
    numberentry=Entry(frame20,textvariable=numvar,font="segoescript 12 ", border=2)
    numberentry.focus_set()
    numberentry.place(x=220,y=40,height=25,width=200)
    def focustoclick(e):
        nobutton.focus_set()
        keyboard.press_and_release('Space') 
    numberentry.bind("<Return>",focustoclick)
    frame20.place(width=1000,height=800)

def dashboards():
    try:
        hoverfiles.place(x=0,y=50,width=1000,height=800)
    except:
        pass
    dashboardframe=Frame(hoverfiles,bg='white')
    def hoverfilesclose():
        hoverfiles.place_forget()
        dashboardframe.destroy()
            
    closeaddframe=Button(dashboardframe,text='X',border=0,relief=GROOVE,background='red',command=hoverfilesclose)
    closeaddframe.place(x=950,y=0,width=30,height=30)
    try:
        datastructures=[]
        datastructure=pd.read_csv("alldataforcalculation.csv")
        
        
        datastructures=pd.DataFrame(datastructure,columns=["Product Name","Unit","Sale Price","Discount","Amount","Purchase Price","Date"])
        
        purchases=float(int(datastructures["Purchase Price"].sum()*100)/100)
        amount=float(int(datastructures["Amount"].sum()*100)/100)
        total=amount-purchases
        
        amountmargin=Label(dashboardframe,text=f"SOLD OF=₹{amount}",font="Helvetica 12 ",background='white')
        amountmargin.place(x=50,y=60)
        purchasesmargin=Label(dashboardframe,text=f"PURCHASED OF=₹{purchases}",font="Helvetica 12 ",background='white')
        purchasesmargin.place(x=50,y=90)
        Profitmargin=Label(dashboardframe,text=f"EARNED=₹{total}",font="Helvetica 12 ",background='white')
        Profitmargin.place(x=50,y=120)
        
        figure1 = plt.Figure(figsize=(6,5), dpi=80)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, dashboardframe)
        bar1.get_tk_widget().place(x=40,y=150)
        datastructures = datastructures[["Amount","Date"]].groupby("Date").sum()
        datastructures.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('SALES')

    except:
        pass
    try:
        def angleofpie(n):
            return 360*n/1000
        datastructures=[]
        datastructure=pd.read_csv("alldataforcalculation.csv")
        datastructures=pd.DataFrame(datastructure,columns=["Product Name","Unit","Sale Price","Discount","Amount","Purchase Price","Date"])

        amountsum=datastructures["Amount"].sum()
        print(amountsum)
        purchasepricesum=datastructures["Purchase Price"].sum()
        print(purchasepricesum)
        totalofbothamtsumprprcesum=int(amountsum)
        calculationpieplot=int((int(purchasepricesum)/totalofbothamtsumprprcesum)*1000)

        pieplotofprofit=Canvas(dashboardframe,width=300,height=300,background="white")

        pieplotofprofit.place(x=600,y=200)    
        pieplotofprofit.create_arc((50,50,250,250),fill="royalblue1",outline="royalblue1",start=angleofpie(0),extent=angleofpie(calculationpieplot))
        if int(amountsum)<int(purchasepricesum):
            pieplotofprofit.create_arc((50,50,250,250),fill="red",outline="red",start=angleofpie(calculationpieplot),extent=angleofpie(1000-calculationpieplot))
            displaylabelprofitprice=Label(dashboardframe,text=f"Loss={(1000-calculationpieplot)/10}%",bg="white",fg="red").place(x=820,y=240)
        else:
            pieplotofprofit.create_arc((50,50,250,250),fill="lawngreen",outline="lawngreen",start=angleofpie(calculationpieplot),extent=angleofpie(1000-calculationpieplot))
            displaylabelprofitprice=Label(dashboardframe,text=f"profit={(1000-calculationpieplot)/10}%",bg="white",fg="lawngreen").place(x=820,y=240)            
        displaylabelpurchaseprice=Label(dashboardframe,text=f"sold={calculationpieplot/10}%",bg="white",fg="royalblue1").place(x=800,y=210)
        
    except:
        pass
    
    dashboardframe.place(width=1000,height=800)

def editprofile():
    try:
        hoverfiles.place(x=0,y=50,width=1000,height=800)
    except:
        pass
    editprofileframe=Frame(hoverfiles,bg='white')
    def hoverfilesclose():
        hoverfiles.place_forget()
        editprofileframe.destroy()
            
    closeaddframe=Button(editprofileframe,text='X',border=0,relief=GROOVE,background='red',command=hoverfilesclose)
    closeaddframe.place(x=950,y=0,width=30,height=30)
    filename=StringVar()
    filenamesig=StringVar()


    companylogo=Label(editprofileframe,text="    Change Company LOGO",bg='white')
    companylogo.place(x=5,y=30)
    def editprofilepic():
        
        filename.set(askopenfilename(filetypes=(("PNG", "*.png"),("JPG", "*.jpg"),("All Files","*.*")))) 
        print(filename.get())
        try:
            editcompanylogo=Image.open(filename.get())
            editcompanylogo=editcompanylogo.resize((70,70),Image.ANTIALIAS)
            rendercompanylogo=ImageTk.PhotoImage(editcompanylogo)
            imga=Label(editprofileframe,image=rendercompanylogo)
            imga.image=rendercompanylogo
            imga.place(x=45,y=110)
        except:
            pass
    editprofilechoice=Button(editprofileframe,text="UPLOAD COMPANY LOGO",command=editprofilepic,relief=FLAT,bg="silver",pady=15)
    editprofilechoice.place(x=10,y=50)
    companynamelabel=Label(editprofileframe,text="Company Name :",bg='white',font="segoescript  ")
    companynamelabel.place(x=440,y=25)
    companynameentryvar=StringVar()
    companynameentryvar.set("")
    companynameentry=Entry(editprofileframe,font=" 1 ",textvariable=companynameentryvar)
    companynameentry.place(x=610,y=25,width=250)
    companyaddresslabel=Label(editprofileframe,text="ADDRESS :",bg='white')
    companyaddresslabel.place(x=550,y=100)
    companyaddressvar=StringVar()
    companyaddressvar.set(" ")
    companyaddressentry= Entry(editprofileframe,textvariable=companyaddressvar)
    companyaddressentry.place(x=610,y=100,width=250,height=20)

    companyaddressvar1=StringVar()
    companyaddressvar1.set(" ")
    companyaddressentry1=Entry(editprofileframe,textvariable=companyaddressvar1)
    companyaddressentry1.place(x=610,y=125,width=250,height=20)
    
    companyphoneemail=Label(editprofileframe,text="PHONE NO. and Email ID : ",bg='white')
    companyphoneemail.place(x=460,y=150)

    companyaddresscaution=Label(editprofileframe,text="do not remove phone no. nd email in text box this will be printed directly on billing page",bg='white')
    companyaddresscaution.place(x=450,y=180)
    
    companyaddressvar2=StringVar()
    companyaddressvar2.set("Phone No.=  ,Email ID=  ")
    companyaddressentry2=Entry(editprofileframe,textvariable=companyaddressvar2)
    companyaddressentry2.place(x=610,y=150,width=250,height=20)

    

    def signature():
        filenamesig.set(askopenfilename(filetypes=(("PNG", "*.png"),("JPG", "*.jpg"),("All Files","*.*")))) 
        print(filenamesig.get())
        try:
            editcompanysignature=Image.open(filenamesig.get())
            editcompanysignature=editcompanysignature.resize((200,65),Image.ANTIALIAS)
            rendercompanysignature=ImageTk.PhotoImage(editcompanysignature)
            imgsignature=Label(editprofileframe,image=rendercompanysignature)
            imgsignature.image=rendercompanysignature
            imgsignature.place(x=160,y=280)

        except:
            pass


    signaturelabel=Label(editprofileframe,text="SIGNATURE :",font=" 1 " , bg='white')
    signaturelabel.place(y=230,x=20)
    signatureentry=Button(editprofileframe,text="UPLOAD SIGNATURE",command=signature,bg='silver',border=1)
    signatureentry.place(x=160,y=230,width=200,height=30)

    def configureprofilefunc():
        data=[]
        
        data.append([filename.get(),filenamesig.get(),companynameentryvar.get(),companyaddressvar.get(),companyaddressvar1.get(),companyaddressvar2.get()])
        data=pd.DataFrame(data,columns=["filename","filenamesig","companyname","addresscol1","addresscol2","address col2"])
        print(data)
        data.to_csv("company information.csv",index=False)
        editingload = Image.open(filename.get())
        editingload=editingload.resize((65,65),Image.ANTIALIAS)
        editingrender = ImageTk.PhotoImage(editingload)
        img.configure(image=editingrender)
        img.image=editingrender

        companylabel["text"]=companynameentryvar.get()

    confugureprofile=Button(editprofileframe,text="SAVE",command=configureprofilefunc,bg='royalblue')
    confugureprofile.place(y=250,relx=0.75,anchor=CENTER,width=100,height=30)

    try:
        editdata=[]
        editdata=pd.DataFrame(read_csv("company information.csv"),columns=["filename","filenamesig","companyname","addresscol1","addresscol2","address col2"])
        editdata=editdata.to_numpy()
        editdatas=[]
        for editdatas in editdata:
            previouscompanylogo=editdatas[0]
            previouscompanysignature=editdatas[1]
            previouscompanyname=editdatas[2]
            previouscompanyaddress=editdatas[3]
            previouscompanyaddress2=editdatas[4]
            previouscompanyaddress3=editdatas[5]




        editcompanylogo=Image.open(previouscompanylogo)
        filename.set(previouscompanylogo)
        editcompanylogo=editcompanylogo.resize((70,70),Image.ANTIALIAS)
        rendercompanylogo=ImageTk.PhotoImage(editcompanylogo)
        imga=Label(editprofileframe,image=rendercompanylogo)
        imga.image=rendercompanylogo
        imga.place(x=45,y=110)

        editcompanysignature=Image.open(previouscompanysignature)
        filenamesig.set(previouscompanysignature)
        editcompanysignature=editcompanysignature.resize((200,65),Image.ANTIALIAS)
        rendercompanysignature=ImageTk.PhotoImage(editcompanysignature)
        imgsignature=Label(editprofileframe,image=rendercompanysignature)
        imgsignature.image=rendercompanysignature
        imgsignature.place(x=160,y=280)

        companynameentryvar.set(previouscompanyname)
        companyaddressvar.set(previouscompanyaddress)
        companyaddressvar1.set(previouscompanyaddress2)
        companyaddressvar2.set(previouscompanyaddress3)

    except:
        pass
    editprofileframe.place(width=1000,height=800)

def previousbill():
    try:
        hoverfiles.place(x=0,y=50,width=1000,height=800)
    except:
        pass
    previousbillframe=Frame(hoverfiles,bg='white')
    def hoverfilesclose():
        hoverfiles.place_forget()
        previousbillframe.destroy()
            
    closeaddframe=Button(previousbillframe,text='X',border=0,relief=GROOVE,background='red',command=hoverfilesclose)
    closeaddframe.place(x=950,y=0,width=30,height=30)
    


    previousbillframe.place(width=1000,height=800)  

def quotation():
    try:
        hoverfiles.place(x=0,y=50,width=1000,height=800)
    except:
        pass
    frame20=Frame(hoverfiles,bg='white')
    def hoverfilesclose():
        hoverfiles.place_forget()
        frame20.destroy()
            
    closeaddframe=Button(frame20,text='X',border=0,relief=GROOVE,background='red',command=hoverfilesclose)
    closeaddframe.place(x=950,y=0,width=30,height=30)
    
    

    totalamount=Label(frame20,text="Grand Total:", bg='white')
    totalamount.place(x=500,y=600)
    totalamountvaribale=DoubleVar()
    totalamountvaribale.set("")
    totalamountdisplay=Entry(frame20,font=" 10 ", textvariable=totalamountvaribale)
    totalamountdisplay.place(x=600,y=600,width=120)
    totalamountdisplay['state']=DISABLED
    purchaseprice=DoubleVar()
    purchaseprice.set("")
    def customerproductsearch():
        add = Toplevel()
        add.focus_set()
        add.title("customer add (tanet)")
        add.geometry("900x550+300+150")
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
        yscrollbar.config(command=managedata.yview)
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
        tableformation()
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
                        
    Customerproduct=Button(frame20,text="ADD PRODUCT FOR CUSTOMER",font="segoescript 12 ",relief=GROOVE,bg='white',command=customerproductsearch)
    Customerproduct.place(x=20,y=140,width=770,height=40)
    Customerproduct.bind("<Enter>",hover)
    Customerproduct.bind("<Leave>",leave)
    Customerproduct.focus_set()
    frame3=Frame(frame20)
    scollingtable=Scrollbar(frame3)
    scollingtable.place(x=750,height=200)
    managedat=ttk.Treeview(frame3,height=5 ,yscrollcommand=scollingtable.set, show='headings',columns=("product name","UNIT","QTY","MRP","Discount","AMOUNT","PP"))
    managedat.column("product name",width=228,anchor='center')
    managedat.column("UNIT",width=105,anchor='center')
    managedat.column("QTY",width=95,anchor='center')
    managedat.column("MRP",width=90,anchor='center')
    managedat.column("Discount",width=90,anchor='center')
    managedat.column("AMOUNT",width=140,anchor='center')
    managedat.heading('product name',text="Product Name")
    managedat.heading('UNIT',text='UNIT')
    managedat.heading('QTY',text='QTY')
    managedat.heading('MRP',text="MRP")
    managedat.heading('Discount',text="Discount")
    managedat.heading('AMOUNT',text="AMOUNT")
    managedat.place(width=750,height=200)
    scollingtable.config(command=managedat.yview)
    frame3.place(x=20,y=200,width=770,height=200)
    Productname=Label(frame20,text="Product name=",font=" 12 ",background='white')
    Productname.place(x=20,y=410)
    productnamevar=StringVar()
    productnamevar.set("")
    productnamedisplay=Entry(frame20,textvariable=productnamevar,font=" 10 ",state=DISABLED)
    productnamedisplay.place(x=160,y=414)
    productmrp=Label(frame20,text="MRP=",font=" 8 ",bg='white')
    productmrp.place(x=400,y=410)
    productmrpvar=DoubleVar()
    productmrpvar.set(0.0)
    productmrpdisplay=Entry(frame20,textvariable=productmrpvar,state=DISABLED,font=" 8 ",bg='white')
    productmrpdisplay.place(x=465,y=410,width=110)
    discountcalculation=Label(frame20,text="Discount%=",font=" 1 ",bg="white")
    discountcalculation.place(x=20,y=451)
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
    discountper=Spinbox(frame20,border=1,font=" 1 ",increment=0.5,command=changes,textvariable=discountpervar,from_=0 , to=100)            
    discountper.place(x=130,y=453,width=80,height=26)
    discountper.bind('<Return>',changess)
    discountprice=Label(frame20,text="Discount(Rs.)=",font=" 1 ",bg="white")
    discountprice.place(x=220,y=450)
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
    discountpriceentry=Spinbox(frame20,border=1,from_=0,to=999999,command=change,textvariable=discountpricevar,font=" 8 ",bg='white')
    discountpriceentry.place(x=360,y=450,width=80)
    discountpriceentry.bind('<Return>',changesss)
    qty=Label(frame20,text="QTY=",font=" 1 ",bg='white')
    qty.place(x=440,y=450)
    qtyvar=IntVar()
    qtyinput=Spinbox(frame20,textvariable=qtyvar,command=calqty,from_=1,to=999,border=1,font=" 1 ",bg='white')
    qtyinput.place(x=500,y=450,width=50)
    totalprice=Label(frame20,text="TOTAL=",font=" 1 ",bg="white")
    totalprice.place(x=20,y=500)
    totalpricevar=DoubleVar()
    totalpricevar.set(0)
    totalpricedisplay=Entry(frame20,border=1,textvariable=totalpricevar,font=" 1 ",bg='white')
    totalpricedisplay.place(x=110,y=500,width=100)
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
    def addtable():
        try:
            products=[]
            name=productnamevar.get()
            unt=unitvar.get()
            productqty=qtyvar.get()
            mrp=productmrpvar.get()
            dscnt=discountpervar.get()
            grandtotal=totalpricevar.get()
            print(f"value of pp={purchaseprice.get()}")
            products.append([name,unt,dscnt,grandtotal,purchaseprice.get()])
            print(products)
            managedat.insert("", 'end',products,values=(name,unt,productqty,mrp,dscnt,grandtotal,purchaseprice.get()*qtyvar.get()))
            alldaata=[]
            tot=0
            tota=0
            for i in managedat.get_children():
                tot=managedat.item(i)['values'][5]
                tota=tota+float(tot)
            print(tota)
            totalamountvaribale.set(tota) 
            productnamevar.set("")
            unitvar.set("")
            productmrpvar.set(0)
            totalpricevar.set("")
            purchaseprice.set("")
            totalpricevar.set(0)
            discountpervar.set(0.0)
            discountpricevar.set(0)
            qtyvar.set(1)
        except:
            productnamevar.set("")
            unitvar.set("")
            productmrpvar.set("")
            totalpricevar.set("")
            purchaseprice.set("")   
            totalpricevar.set(0)
            discountpervar.set(0.0)
            discountpricevar.set(0)

    def addbuttonentry(e):
        addbutton['background']='white'
    def addbuttonout(e):
        addbutton['bg']='grey90'
    unit=Label(frame20,text="Unit=",bg='white',font=" 2 ")
    unit.place(x=605,y=410)
    unitvar=StringVar()
    unitvar.set("")
    unitentry=Entry(frame20,textvariable=unitvar,font=" 1 ",bg='white',state=DISABLED)
    unitentry.place(x=660,y=410,width=80)
    addbutton=Button(frame20,text="ADD PRODUCT",bg='grey90',relief=GROOVE,command=addtable)
    addbutton.place(x=270,y=493,width=200,height=40)
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
    deletebutton=Button(frame20,text="REMOVE PRODUCT",bg='red',relief=GROOVE,command=deltable)
    deletebutton.place(x=350,y=540,width=270,height=50)
    deletebutton.bind('<Enter>',delbuttonentry)
    deletebutton.bind('<Leave>',delbuttonout)
    def prttable():
        try:
            i=[]
            alldata=[]
            for i in managedat.get_children():
                pn,unt,qty,slp,dsp,tt,pp=managedat.item(i)['values']
                alldata.append([pn,unt,qty,slp,dsp,tt,pp,str(dt.date.today())])            
                all=pd.DataFrame(alldata,columns=["Product Name","Unit","QTY","Sale Price","Discount","Amount","Purchase Price","Date"])
                all.to_csv("forprinting.csv",index=False)

            quotationprintpdf()
            webbrowser.open("doc.pdf")           
            openbilling()

        except:
            print("exception working bro...")
            
    def prbuttonentry(e):
        printbutton['background']='white'
    def prbuttonout(e):
        printbutton['bg']='lawngreen'
    printbutton=Button(frame20,text="PRINT INVOICE",bg='lawngreen',relief=GROOVE,command=prttable)
    printbutton.place(x=30,y=540,width=300,height=50)
    printbutton.bind('<Enter>',prbuttonentry)
    printbutton.bind('<Leave>',prbuttonout)
                
    frame20.place(width=1000,height=800)  
        
button1.place(x=0,y=100,width=300,height=50)
button2=Button(frame1 , text="CUSTOMER\t\t\t  \t>" ,bg='Royalblue2' , command=addproducttask,relief=GROOVE)
button2.place(x=0,y=151,width=300,height=50)
button3=Button(frame1 , text="STOCK MANAGEMENT\t\t\t >",bg='Royalblue2',relief=GROOVE, command=pl)
button3.place(x=0,y=202,width=300,height=50)
button4=Button(frame1,border=0 , text="DASHBOARD",bg='white',foreground='black',relief=GROOVE, command=dashboards)
button4.place(y=80,relx=0.5,anchor=CENTER,width=180,height=30)
button5=Button(frame1, text="BILLING",bg='lawngreen',relief=GROOVE, command=billing)
button5.place(y=284,relx=0.5,anchor=CENTER,width=300,height=70)
button6=Button(frame1 , text="EDIT",bg='white',foreground='black',relief=RAISED, command=editprofile)
button6.place(y=20,relx=0.9,anchor=CENTER, width=50,height=30)
frame1.pack(side=LEFT , anchor='e', fill=Y)
button7=Button(frame1 , text="PREVIOUS BILL\t\t\t\t>",bg='Royalblue2',relief=GROOVE, command=previousbill)
button7.place(x=0,y=320,width=300,height=50)
button8=Button(frame1 , text="QUOTATION\t\t\t\t>",bg='Royalblue2',relief=GROOVE, command=quotation)
button8.place(x=0,y=370,width=300,height=50)
button9=Button(frame1 , text="IN FUTURE\t\t\t\t>",bg='Royalblue2',relief=GROOVE, command=quotation)
button9.place(x=0,y=420,width=300,height=50)


frame2= Frame(program , width=800 , height=1000 , bg='white' )
label1=Label(frame2,text='TANET' , font=("comicsans 30 bold"),bg='orange' , padx=1000).pack(side=TOP)
time=Label(frame1,text=f"Date={dt.date.today()}",font="segoescript 12 ",foreground='white' ,background='Royalblue2').place(relx=0.5,anchor=CENTER,y=630)
billingguide=Label(frame2,text="<------------------- choose for billing",background='white').place(y=350,relx=0.12,anchor=CENTER)
editprofileguide=Label(frame2,text="<------------------- Edit Profile company , name , address , signature",background='white').place(y=80,relx=0.2,anchor=CENTER)

    
hoverfiles=Frame(frame2,bg='white')
def openbilling():
    billing()
openbilling()
hoverfiles.place(x=0,y=50,width=1000,height=800)
frame2.pack(side=RIGHT , fill=Y)
program.mainloop()