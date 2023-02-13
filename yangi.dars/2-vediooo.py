from datetime import datetime
class Human:
    def __init__(self) -> None:
        self._name=''
        self.age=0
        self.__birth_day=datetime.now().strftime("%d-%m-%Y")
        self._surname=''
    def set_name(self,ism):
        self._name=ism
    def set_surname(self,ochstva):
        self._surname=ochstva
    def set_birth(self,ts):
        self.__birth_day=ts
    def get_name(self):
        return self._name
    def get_age(self):
        return self.__age
    def get_surname(self):
        return self.get_surname
    def inc_age(self):
        hozir=datetime.now().year
        d=self.__birth_day.split('.')
        self.__age=hozir-int(d[2])
    def get_birth(self):
        return self.__birth_day
    def __str__(self) -> str:
        return "{0:<20} {1:<20} {2:<10} {3:<14}".format(self._name,self._surname,self.age,self.__birth_day)
class Ustoz(Human):
    def __init__(self) -> None:
        super().__init__()
        self._mutaxasisligi=''
        self._salary=0
        self._type=''
        self._work_place=''
        
    def set_fani(self,sps):
        self._mutaxasisligi=sps
    def set_salary(self,oylik):
        self._salary=oylik
    def set_type(self,tur):
        self._type=tur
    def set_place(self,ishjoy):
        self._work_place=ishjoy
    def __str__(self) -> str:
        return super().__str__()+"{0:<15} {1:<10} {2:<10} {3:<20}".format(self._mutaxasisligi,self._type,self._salary,self._work_place)

a=Ustoz()
ism=input("Please input your name: ")
familya=input("Please input your surname: ")
dobb=input("Please input your date of birth: ")
fan=input("Please input your direction: ")
lev=input("Please input your level: ")
maoshh=input("Please input your salary: ")
ish_joyi=input("Please input place of your work: ")
print("\n")
print("Information of Teacher::>>")
a.set_name(ism)
a.set_surname(familya)
a.set_birth(dobb)
a.set_fani(fan)
a.set_type(lev)
a.set_salary(maoshh)
a.set_place(ish_joyi)
a.inc_age()
print("____ISMI____       _FAMILYASI_        ______TUGULGANLIGI______    __MUTAXASISLIGI__   _LEVEL_   OYLIGI   ISHJOYI")
print(a)