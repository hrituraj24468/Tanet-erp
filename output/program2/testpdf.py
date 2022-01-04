from re import split
from tkinter.ttk import Separator
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Table , SimpleDocTemplate
import pandas as pd
from reportlab import *
import datetime
from reportlab.platypus import tables
from reportlab.platypus.frames import Frame
from reportlab.platypus.tables import TableStyle
import num2words
import time
import os

def printpdf():
    name='JS PETS AND PRODUCTS'
    abc="7B-1 Ram Nagar Colony, In Front Of Kanchanpur Tower,"
    bcd=" Mohaddipur, Gorakhpur"
    cde="Phone no.: 9792383230 Email: jspetsandproducts@gmail.com"
    styles = getSampleStyleSheet()
    style = styles["BodyText"]

    canv = Canvas("doc.pdf")

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
    Canvas.drawString(canv,text=str(datetime.date.today()),x=500,y=685)
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
        alldata.append(rowdata) 
    def tables():
        
        if (len(alldata))<20:
            flow=[]
            table1=[]
            tabledrawing=[["product name","UNIT","sale price","Discount","Amount"]]
            trows=alldata
            print(len(trows))
            threader=Table([tabledrawing[0]],colWidths=[230,70,70,70,70])
            threader.setStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                ("BACKGROUND",(0,0),(-1,-1),colors.dodgerblue),
                ("FONT",(0,0),(-1,-1),"Times-Bold",12),
                ('TEXTCOLOR',(0,0),(-1,-1),colors.white)])
            flow.append(threader) 
            everything=(len(trows))

            for i in range(0,everything):                   
                trow=Table([trows[i-1]],colWidths=[230,70,70,70,70])      
                trow.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                    ("FONT",(0,0),(-1,-1),"Helvetica",10),
                    ('TEXTCOLOR',(0,0),(-1,-1),colors.black)]))
                flow.append(trow)
            
            frame=Frame(30,250,530,400,showBoundary=1,rightPadding=6,leftPadding=6)
            frame.addFromList(flow,canv)
        elif (len(alldata))>20:
            flow=[]
            table1=[]
            tabledrawing=[["product name","UNIT","sale price","Discount","Amount"]]
            trows=alldata
            print(len(trows))
            everything=(len(trows))
            threader=Table([tabledrawing[0]],colWidths=[230,70,70,70,70])
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
                    Canvas.drawString(canv,text=str(datetime.date.today()),x=500,y=685)
                    naam=[]
                    file=open("Name.txt",'r')
                    naam=file.readline()
                    print('\n\n')
                    print(naam)
                    Canvas.drawString(canv,text=str(naam),x=20,y=670)
                    threader=Table([tabledrawing[0]],colWidths=[230,70,70,70,70])
                    threader.setStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ("BACKGROUND",(0,0),(-1,-1),colors.dodgerblue),
                        ("FONT",(0,0),(-1,-1),"Times-Bold",12),
                        ('TEXTCOLOR',(0,0),(-1,-1),colors.white)])
                    flow.append(threader)
                trow=Table([trows[i-1]],colWidths=[230,70,70,70,70])      
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
    Canvas.drawImage(canv,image="docimage/signature.png",x=400,y=90,width=80,height=50)
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
  
