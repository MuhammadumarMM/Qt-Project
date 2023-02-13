
class Car:
    def  __init__(self) -> None:
        self.__nom="Captico"
        self.__dvg=120
        self.__year=2020
        self.color="black"
        self.wina="turbo"
    def get_nom(self)->str:
        return self.__nom
    def get_dvg(self)->int:
        return self.__dvg
    def get_year(self)->int:
        return self.__year
    def set_color(self,col):
        self.color=col
    def set_wina(self,win):
        self.wina=win
    def __str__(self) -> str:
        return "{n:7} {d:3} {y:4} {c:5} {w:5}".format(n=self.__nom,d=self.__dvg,y=self.__year,c=self.color,w=self.wina)
c=Car()
# print(c)
class Ycar(Car):
    def __init__(self) -> None:
        super().__init__()
        self.rul="Mers"
        c.__nom="Maluba"
    def __str__(self) -> str:
        return super().__str__()+"{0:4} {1:6}".format(self.rul,c.__nom)
d=Ycar()
print(d)