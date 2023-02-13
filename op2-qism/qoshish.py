class Butun:
    def __init__(self,son=int()) -> None:
        self.data=son
    def set_data(self,a):
        if type(a) in (int,float):
            self.data=int(a)
        else:
            raise TypeError("Eror code te01")
    def get_data(self)->int:
        return self.data
    # + - * /
    def __add__(self,a):
        if isinstance(a,Butun):
            self.data+=a.get_data()
        elif isinstance(a,int):
            self.data+=a
        elif isinstance(a,float):
            self.data+=int(a)
        else:
            raise TypeError("Error code te02")
        return self
    def __sub__(self,a):
        if isinstance(a,Butun):
            self.data-=a.get_data()
        elif isinstance(a,int):
            self.data-=a
        elif isinstance(a,float):
            self.data-=int(a)
        else:
            raise TypeError("Error code te03")
        return self
    def __mul__(self,a):
        if isinstance(a,Butun):
            self.data*=a.get_data()
        elif isinstance(a,int):
            self.data*=a
        elif isinstance(a,float):
            self.data*=int(a)
        else:
            raise TypeError("Error code te03")
        return self
    def __truediv__(self,a):
            if isinstance(a,Butun):
                if a.get_data==0:
                    raise ZeroDivisionError("Zero Error")
                else:    
                    self.data=int(self.data/a.get_data())
            elif isinstance(a,int):
                if a==0:
                    raise ZeroDivisionError("Zero Error")
                else:
                    self.data=int(self.data/a)
            elif isinstance(a,float):
                if a==0:
                    raise ZeroDivisionError("Zero Error")
                else:
                    self.data=int(self.data/int(a))
            else:
                raise TypeError("Error code te03")
            return self
    def __len__(self):
        n=self.data
        cnt=0
        while n!=0:
            cnt+=1
            n//=10
        return cnt
    def __str__(self) -> str:
        return str(self.data)
try:
    b=Butun()
    58585858
    print(b)
except (TypeError,ZeroDivisionError) as te:
    print(str(te))
    # 171044743
    # 174214613