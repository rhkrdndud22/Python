## 0710 파이썬 수업

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
