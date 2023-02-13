from datetime import datetime
class Employee:
    name=''
    surname=''
    birth=''
    salary=0.0
    beginwork=''
    reyting=0.0
    idCard=0
    def input(self):
        self.name=input("Please your name: ")
        self.surname=input("Please your surname: ")
        self.birth=input("Please your birthday: ")
        self.salary=float(input("Please your salary: "))
        self.beginwork=input("Please your beginwork: ")
        self.reyting=float(input("Please your reting: "))
        self.idCard=int(input("Please idCard: "))
    def age(self):
        curYear=datetime.now().year
        ls=self.birth.split('-')
        bYear=int(ls[len(ls)-1])
        return curYear-bYear
    def yillik(self):
        return self.salary*12
    def staj(self):
        ishYear=datetime.now().year
        lss=self.beginwork.split('-')
        cYear=int(lss[len(lss)-1])
        return ishYear-cYear
    def __str__(self) -> str:
        return f"{self.name}    {self.surname}  {self.birth}  {self.salary}  {self.beginwork}   {self.reyting}  {self.idCard}"
    def prnt(self):
        print(f"{self.name}    {self.surname}  {self.birth}  {self.salary}  {self.beginwork}   {self.reyting}  {self.idCard}")
# h=Employee()
# h.input()
# print(str(h.name)+"ning yoshi: "+str(h.age())+" da " +"yillik daromad " +str(h.yillik())+" dollar " + " Ish boshlaganiga "+str(h.daromad())+" yil boldi")
class Company:
    lss=[]
    company_name=''
    com_dir_FIO=''
    com_salary=0.0
    def add(self,p):
        self.lss.append(p)
    def royhat(self):
        for i in self.lss:
            print(i.prnt())
    def mx(self):
        max=0
        for i in range(len(self.lss)):
            if self.lss[i].staj()>self.lss[max].staj():
                max=i
        return self.lss[max]
    def nx(self):
        min=0
        for i in range(len(self.lss)):
            if self.lss[i].age()<self.lss[min].age():
                min=i
        return self.lss[min]
    def sarala(self):
        self.lss.sort(key= lambda x : x.name)
    def wovall(self):
        for i in range(len(self.lss)):
            self.lss[i].prnt()
    def sarala1(self):
        self.lss.sort(key= lambda x : x.reyting)
    def wovall1(self):
        for i in range(len(self.lss)):
            self.lss[i].prnt()
    def chop(self,idCard):
        for i in self.lss:
            if i.idCard==idCard:
                self.lss.remove(i)
                break
i=Company()
l=True
while l:
    print("\n")
    print("1-Yangi ishchi qo'shish")
    print("2-Xodimlar royhati")
    print("3-Companiyada eng maksimal stajga ega bo'lga hodim malumoti")
    print("4-Eng yosh hodim")
    print("5-Xodimlarni ismi bo'yicha saralash")
    print("6-Xodiml;arni reyting bo'yicha saralash")
    print("7-Xodimlarni o'chirish")
    print("\n")
    cmd=input()
    match cmd:
        case "1":
            ishchi=Employee()
            ishchi.input()
            i.add(ishchi)
            print("ADDED")
        case "2":
            i.royhat()
        case "3":
            print(str(i.mx()))
        case "4":
            print(str(i.nx()))
        case "5":
            i.sarala()
            i.wovall()
        case "6":
            i.sarala1()
            i.wovall1()
        case "7":
            s=int(input("Idni kiriting: "))
            i.chop(s)
