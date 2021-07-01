## 0701 파이썬 수업

```python
import requests 
from bs4 import BeautifulSoup

url='http://www.kric.go.kr/jsp/industry/rss/citystapassList.jsp?q_org_cd=A010010024&q_fdate=2021'

response = requests.get(url) //requests 매서드로 url을 가져온다.
html = response.content

bsoup = BeautifulSoup(html, "html.parser")
btab=bsoup.find("table",{"class":"listtbl_c100"} )
btrs=btab.find("tbody").find_all("tr")
btdcols= btrs[1].find_all("td",{"class" : "tdcol"})
btds = btrs[1].find_all("td")

passengers= []

for tr in btrs[1:] :
    dic = {}
    tds = tr.find_all("td")
    dic['station']=tds[0].text
    dic['ride']=tds[2].text
    dic['alight']=tds[3].text
    passengers.append(dic)
    
    from tkinter import Tk, ttk, Label, Button, Text, END

window=Tk()
window.title("인원관리 프로그램")
window.geometry("400x400")
window.resizable(0,0)

title= "지하철 승하차 인원관리"
title_feature=Label(window, text=title, font =  ("Noto ",20))
title_feature.pack(padx=10,pady=15)

treeTable=ttk.Treeview(window)
treeTable["columns"]=("station","ride","alight")
treeTable.column("#0",width = 50)
treeTable.column("station",width = 100)
treeTable.column("ride",width = 50)
treeTable.column("alight",width = 50)

treeTable.heading("#0", text="NO.", anchor = "center")
treeTable.heading("station", text= "역이름", anchor= "center")
treeTable.heading("ride", text= "승차인원", anchor= "center")
treeTable.heading("alight", text= "하차인원", anchor= "center")


def setTableItem() :
    treeTable.delete(*treeTable.get_children())
    for idx, report in enumerate(passengers) :
        idx= idx+1
        station = report['station']
        ride = report['ride']
        alight = report['alight']
        treeTable.insert("", 'end', iid=None, text=str(idx), values=[station,ride,alight])

        
        

treeTable.place(x=10, y=90, width=380, height=200)
setTableItem()


window.mainloop()

```

실행화면</br>

![image](https://user-images.githubusercontent.com/77717717/124070260-80658680-da78-11eb-967b-ccfd34b65bc0.png)


## 코드 활용 
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
    dic['자영업자현황']=th[0].text
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
from tkinter import Tk, ttk, Label, Button, Text, END

window=Tk()
window.title
window.title("자영업자 현황")
window.geometry("650x300")
window.resizable(0,0)

title= "자영업자 현황"
title_feature=Label(window, text=title, font =  ("Noto ",20))
title_feature.pack(padx=10,pady=15)

treeTable=ttk.Treeview(window)
treeTable["columns"]=("자영업자현황","천십오","천십육","천십칠","천십팔","천십구","천이십")
treeTable.column("#0",width = 50)
treeTable.column("자영업자현황",width = 130,anchor="center")
treeTable.column("천십오",width = 50,anchor="center")
treeTable.column("천십육",width = 50,anchor="center")
treeTable.column("천십칠",width = 50,anchor="center")
treeTable.column("천십팔",width = 50,anchor="center")
treeTable.column("천십구",width = 50,anchor="center")
treeTable.column("천이십",width = 50,anchor="center")

treeTable.heading("#0", text="NO.", anchor = "center")
treeTable.heading("자영업자현황", text= "자영업자현황", anchor= "center")
treeTable.heading("천십오", text= "2015", anchor= "center")
treeTable.heading("천십육", text= "2016", anchor= "center")
treeTable.heading("천십칠", text= "2017", anchor= "center")
treeTable.heading("천십팔", text= "2018", anchor= "center")
treeTable.heading("천십구", text= "2019", anchor= "center")
treeTable.heading("천이십", text= "2020", anchor= "center")

def setTableItem() :
    treeTable.delete(*treeTable.get_children())
    for idx, report in enumerate(passengers) :
        idx= idx+1
        자영업자현황=report['자영업자현황']
       
        천십오 = report['천십오']
        천십육 = report['천십육']
        천십칠 = report['천십칠']
        천십팔 = report['천십팔']
        천십구 = report['천십구']
        천이십 = report['천이십']
        treeTable.insert("", 'end', iid=None, text=str(idx), values=[자영업자현황,천십오,천십육,천십칠,천십팔,천십구,천이십])
        
        
treeTable.place(x=10, y=90, width=600, height=150)
setTableItem()
window.mainloop()
```
## 
![image](https://user-images.githubusercontent.com/77717717/124088766-3b4c4f00-da8e-11eb-8113-6f76f845aa05.png)


