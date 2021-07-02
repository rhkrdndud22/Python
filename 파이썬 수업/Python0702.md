## 0702 파이썬 과제

```python

import requests
from bs4 import BeautifulSoup

url='https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=2779'

response = requests.get(url)
html = response.content

bsoup = BeautifulSoup(html, "html.parser")
btab=bsoup.find("div",{"class":"con_table of_auto wid100p"})
btrs=btab.find("tbody").find_all("tr")
btdcols= btrs[0].find_all("th",{"class" : "tl"})
btds = btrs[0].find_all("td")

passengers=[]

for tr in btrs[0:] :
    dic = {}
    th=tr.find_all("th",{"class": "tl"})
    tds = tr.find_all("td")
    dic['분류']=th[0].text
    dic['이천십']=tds[0].text
    dic['천십일']=tds[1].text
    dic['천십이']=tds[2].text
    dic['천십삼']=tds[3].text
    dic['천십사']=tds[4].text
    dic['천십오']=tds[5].text
    dic['천십육']=tds[6].text
    dic['천십칠']=tds[7].text
    dic['천십팔']=tds[8].text
    dic['천십구']=tds[9].text
    dic['천이십']=tds[10].text
    
    
    
    passengers.append(dic)

def STM() :
    treeTable.delete(*treeTable.get_children())
    for idx, report in enumerate(passengers) :
        idx= idx+1
        분류=report['분류']
       
        천십오 = report['천십오']
        천십육 = report['천십육']
        천십칠 = report['천십칠']
        천십팔 = report['천십팔']
        천십구 = report['천십구']
        천이십 = report['천이십']
        treeTable.insert("", 'end', iid=None, text=str(idx), values=[분류,천십오,천십육,천십칠,천십팔,천십구,천이십])
        
        


import requests
from bs4 import BeautifulSoup

url1='https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=2477'
response1 = requests.get(url1)
html1 = response1.content

bsoup1 = BeautifulSoup(html1, "html.parser")
btab1=bsoup1.find("div",{"class":"con_table of_auto wid100p"})
btrs1=btab1.find("tbody").find_all("tr")
btdcols1= btrs1[0].find_all("th",{"class" : "tl","data-id":"t247"})
btds1 = btrs1[0].find_all("td")

pas=[]

for tr in btrs1[0:7] :
    dic = {}
    th=tr.find_all("th",{"class": "tl"})
    tds = tr.find_all("td")
    dic['분류']=th[0].text
    dic['일육']=tds[0].text
    dic['일칠']=tds[1].text
    dic['일팔']=tds[2].text
    dic['일구']=tds[3].text
    dic['이공']=tds[4].text
    
   
   
    pas.append(dic)

def STN() :
    treeTable.delete(*treeTable.get_children())
    for idx, report in enumerate(pas) :
        idx= idx+1
        분류=report['분류']
        일육 = report['일육']
        일칠 = report['일칠']
        일팔 = report['일팔']
        일구 = report['일구']
        이공 = report['이공']
       
        treeTable.insert("", 'end', iid=None, text=str(idx), values=[분류,일육,일칠,일팔,일구,이공])    
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk, ttk, Label, Button, Text, END

win = Tk()
win.title("Raspberry Pi UI")
win.geometry('100x100+200+200')

window=Tk()
window.title
window.title("현황판")
window.geometry("650x300")
window.resizable(0,0)
title= "현황판"
title_feature=Label(window, text=title, font =  ("Noto ",20))
title_feature.pack(padx=10,pady=15) 


treeTable=ttk.Treeview(window)
treeTable["columns"]=("분류","천십오","천십육","천십칠","천십팔","천십구","천이십")
treeTable.column("#0",width = 50)
treeTable.column("분류",width = 130,anchor="center")
treeTable.column("천십오",width = 50,anchor="center")
treeTable.column("천십육",width = 50,anchor="center")
treeTable.column("천십칠",width = 50,anchor="center")
treeTable.column("천십팔",width = 50,anchor="center")
treeTable.column("천십구",width = 50,anchor="center")
treeTable.column("천이십",width = 50,anchor="center")

treeTable.heading("#0", text="NO.", anchor = "center")
treeTable.heading("분류", text= "분류", anchor= "center")
treeTable.heading("천십오", text= "2015", anchor= "center")
treeTable.heading("천십육", text= "2016", anchor= "center")
treeTable.heading("천십칠", text= "2017", anchor= "center")
treeTable.heading("천십팔", text= "2018", anchor= "center")
treeTable.heading("천십구", text= "2019", anchor= "center")
treeTable.heading("천이십", text= "2020", anchor= "center")      









def ok():
    str = 'nothing selected'
    if radVar.get() == 1:
        
        str = "자영업자를 현황을 보여드리겠습니다"
        messagebox.showinfo("Button Clickec", str)
        treeTable.place(x=10, y=90, width=600, height=150)
        STM()
          
        
    if radVar.get() == 2:
        
        str = "회사원 현황을 보여드리겠습니다"
        messagebox.showinfo("Button Clickec", str)
        treeTable.place(x=10, y=90, width=600, height=150)
        STN()
        
        
        
radVar = IntVar()
r1=ttk.Radiobutton(win, text="자영업자현황", variable=radVar,  value=1)
r1.grid(column=0, row=0)
r2=ttk.Radiobutton(win, text="회사원 현황", variable=radVar, value=2)
r2.grid(column=0, row=1)
action = ttk.Button(win, text = "Click Me", command = ok)
action.grid(column=0, row=2)
win.mainloop() 
```

![image](https://user-images.githubusercontent.com/77717717/124237816-e9b9c800-db52-11eb-9ced-0721d3edda2c.png)
![image](https://user-images.githubusercontent.com/77717717/124237875-fa6a3e00-db52-11eb-98f7-a9e9b27da73d.png)
![image](https://user-images.githubusercontent.com/77717717/124237946-0bb34a80-db53-11eb-8e29-cf165d076264.png)
![image](https://user-images.githubusercontent.com/77717717/124237989-1a016680-db53-11eb-9a12-251642b2218f.png)

