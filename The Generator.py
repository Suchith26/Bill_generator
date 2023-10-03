#sample

from pathlib import Path
from docxtpl import DocxTemplate
from docx2pdf import convert

print("SELECT THE FACTORY NUMBER")
print("1.Abhay")
print("2.Cheruku")
print("3.Baheti")
print("4.Shyam")
print("5.Maheshwari")
print("6.NICO guntur")
print("7.Mahesh FATS")

fac=int(input())

if(fac==1):
    document_path=Path(__file__).parent/"BILL SST ABHAY.docx"
    doc=DocxTemplate(document_path)
elif(fac==2):
    document_path=Path(__file__).parent/"BILL SST CHERUKUPALLY.docx"
    doc=DocxTemplate(document_path)
elif(fac==3):
    document_path=Path(__file__).parent/"BILL SST BAHETHI.docx"
    doc=DocxTemplate(document_path)    
elif(fac==4):
    document_path=Path(__file__).parent/"BILL SST SHYAM.docx"
    doc=DocxTemplate(document_path)    
elif(fac==5):
    document_path=Path(__file__).parent/"BILL SST Maheshwari.docx"
    doc=DocxTemplate(document_path)    
elif(fac==6):
    document_path=Path(__file__).parent/"BILL SST NICO.docx"
    doc=DocxTemplate(document_path)
elif(fac==7):
    document_path=Path(__file__).parent/"BILL SST Mahesh FATS.docx"
    doc=DocxTemplate(document_path)     

bil=0
Vno=""
date=""
through=""
bags=0
bagtype=""
qtls=0
rate=0
Amount=0
IGST=0
TTL=0


for i in range(0,8):
    if i==0:
        bil=int(input('bill no:'))
    elif i==1:
        Vno=str(input('vehicle no:'))
    elif i==2:
        date=str(input('Date:'))
    elif i==3:
        through=str(input('Through:'))
    elif i==4:
        bags=int(input('Bags:'))
    elif i==5:
        bagtype=str(input('Bag type:'))
    elif i==6:
        qtls=float(input('Quintals:'))
    elif i==7:
        rate=float(input('Rate:'))
   
rate=(rate*100)/105
rate=round(rate,2)
Amount=rate*qtls
Amount=round(Amount,2)
CGST=Amount*0.025
SGST=Amount*0.025
IGST=Amount*0.05
IGST=round(IGST,2)
CGST=round(CGST,2)
SGST=round(SGST,2)
TTL=Amount+IGST
TTL=round(TTL,2)

    
if(fac==1 or fac==6):
    context={"BIl":bil,
         "VNO":Vno,
         "DATE":date,
         "THR":through,
         "BAGS":bags,
         "TYPE":bagtype,
         "QTL":qtls,
         "RATE":rate,
         "AMT":Amount,
         "IGST":IGST,
          "TTL":TTL}
elif(fac==2 or fac==3 or fac==4 or fac==5 or fac==7):
    context={"BIl":bil,
         "VNO":Vno,
         "DATE":date,
         "THR":through,
         "BAGS":bags,
         "TYPE":bagtype,
         "QTL":qtls,
         "RATE":rate,
         "AMT":Amount,
         "SGST":SGST,
         "CGST":CGST,
          "TTL":TTL}

doc.render(context)#writing details into word doc

s="Bill no "
f=" SST.docx"
pdf=".pdf"
a=str(bil)
i=s+a+f
d=s+a+pdf
doc.save(Path(__file__).parent/i)#saving as the new word doc

#i='./bills/'+i

convert(r"C:\Users\Suchith\Desktop\bills\i",r"C:\Users\Suchith\Desktop\bills\d")
