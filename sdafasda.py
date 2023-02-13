from datetime import datetime
class Human:
    def init(self) -> None:
        self._name=''
        self.age=0
        self.__birth_day=datetime.now().strftime("%d-%m-%Y")
        self._surname=''
    def set_name(self,ism):
        self._name=ism
    def set_surname(self,famil):
        self._surname=famil
    def set_birth(self,dobb):
        self.__birth_day=dobb
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
    def __str(self) -> str:
        return "\tName     : {ism:<20}\n\tFamily   : {famil:<20}\n\tAge      : {yosh:<10}\n\tDOB      : {dob:<14}".format(ism=self._name,famil=self._surname,yosh=self.age,dob=self.__birth_day)
class Teacher(Human):
    def __init(self) -> None:
        super().init()
        self._fani=''
        self._salary=0
        self._type=''
        self._work_place=''
    def set_fani(self,t):
        self._fani=t
    def set_salary(self,s):
        self._salary=s
    def set_type(self,tt):
        self._type=tt
    def set_place(self,aa):
        self._work_place=aa
    def str(self) -> str:
        return super().str()+"\n\tDirection: {fani:<15}\n\tLevel    : {toifa:<10}\n\tSalary   : {maosh:<10}\n\tWorkplace: {place:<20}".format(fani=self._fani,toifa=self._type,maosh=self._salary,place=self._work_place)

tech=Teacher()
ism=input("Please input your name: ")
familya=input("Please input your surname: ")
dobb=input("Please input your date of birth: ")
fan=input("Please input your direction: ")
lev=input("Please input your level: ")
maoshh=input("Please input your salary: ")
ish_joyi=input("Please input place of your work: ")
print()
print("Information of Teacher::>>")
tech.set_name(ism)
tech.set_surname(familya)
tech.set_birth(dobb)
tech.set_fani(fan)
tech.set_type(lev)
tech.set_salary(maoshh)
tech.set_place(ish_joyi)
tech.inc_age()
print(tech.str())