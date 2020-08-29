import os
#yeni fayl hazrilamaq
#faylin icindeki melumatlari pxumaq
#fayli silmek
#fayla her hansi melumat elave etmek
# faylla elaqe yaratmaq
#fayl uzerinde hansi islerin aparilacagin qeyd etmek(bunu oxumaq yazmaq ya deyisdirmek ucun muraciet edirem)

#fayla connection
#conn=open("data.txt","r")
#print(conn.read())
##filea melumat yaz
class User:
    def __init__(self, name,surname):
     self.name=name
     self.surname=surname
     self.addDatatoFile()
    def addDatatoFile(self):
        txt=f"{self.name} \{self.surname} \n"
        conn=open("data.txt","a")
        conn.write(txt)
User("Nigar","Mammadova")
User("Unknown","Unknown")
