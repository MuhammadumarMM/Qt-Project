class PassTransport:
    def __init__(self) -> None:
        self.name=""
        self.cnt_plase=0
        self.m_speed=2.0
        self.country=""
        self.company="UZ_AUTO_MOTORS"
    def set_name(self,name="Metro_Tash"):
        self.name=name
    def set_cnt_plase(self,cn=int()):
        self.cnt_plase=cn
    def set_max_speed(self,sped=float()):
        if (type(sped) in (float,int)) and (sped>15) and (sped<400):
            self.m_speed=sped
        else:
            raise Exception("Xatolik")
    def set_company(self,com="UZ_AUTO"):
        if isinstance(com,str) and com!="GM":
            raise Exception("Bunday kompaniya yoqku")
        self.company=com
    def set_country(self,coun="Uzb"):
        self.country=coun
    def __str__(self) -> str:
        return "{0:^15} {1:<2}-person {2:<7.3f} mil/sec {3:<7} {4:<15}".format(
            self.name,self.cnt_plase,self.m_speed,self.country,self.company
        )
class Car(PassTransport):
    def __init__(self) -> None:
        super().__init__()
        self.color=""
        self.date=""
    def set_color(self,color="red"):
        self.color=color
    def set_date(self,date="12-12-2002"):
        self.date=date
    def __str__(self) -> str:
        return super().__str__()+"{0:^10} {1:^11}".format(self.color,self.date)
try:
    cap=Car()
    cap.set_name("Capciko")
    cap.set_date("12-12-2021")
    cap.set_color="ChoclateColor"
    cap.set_cnt_plase(5)
    cap.set_max_speed(360)
    print(str(cap))
except Exception as e:
    print(e)