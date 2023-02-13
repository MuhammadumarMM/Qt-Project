class Date:
    def __init__(self) -> None:
        self._year="2023"
        self._day=1
        self._month="Fevral"
    def get_year(self)->str:
        return self._year
    def get_day(self)->int:
        return self._day
    def get_month(self)->str:
        return self._month
    def __str__(self) -> str:
        return "{0:4} {1:2} {2:10}".format(self.get_year(),self.get_day(),self.get_month())
c=Date()
# print(c)
class Ddate(Date):
    def __init__(self) -> None:
        super().__init__()
        # self._year="2024"
        # self._day=5
        # self._month="aprel"
    def __str__(self) -> str:
        return super().__str__()
    def change_year(self,b):
        self._year=b
    def change_day(self,b):
        self._day=b
    def change_month(self,b):
        self._month=b
b=Ddate()
b.change_year("2025")
b.change_month("Mart")
b.change_day(5)
print(b)