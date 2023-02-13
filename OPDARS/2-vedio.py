from datetime import datetime
class Person:
    name=''
    surname=''
    birth=''
    adress=''
    psSeriya=''
    psDig=0
    def rn(self):
        print("yugur toxtama yugur")
    def input(self):
        self.name=input("Please your name: ")
        self.surname=input("Please your surname: ")
        self.birth=input("Please your Birthday: ")
    def age(self):
        curYear=datetime.now().year
        # dd-mm-yyyy
        ls=self.birth.split('-')
        bYear=int(ls[len(ls)-1])
        return curYear-bYear
h=Person()
h.input()
print(str(h.name)+"ning yoshi: "+str(h.age())+" da")