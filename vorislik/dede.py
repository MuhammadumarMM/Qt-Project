from datetime import datetime
class Date:
    def __init__(self,*args) ->None:
        if len(args)==1:
            s=args[0].split('.')
            self.day=int(s[0])
            self.month=int(s[1])
            self.year=int(s[2])
        elif len(args)==3:
            self.day=int(args[0])
            self.month=int(args[1])
            self.year=int(args[2])
        else:
            self.day=datetime.now().day
            self.month=datetime.now().month
            self.year=datetime.now().year
    # def set_day(self)
    def __str__(self) -> str:
        return "{d:2}-{m:2}-{y:4}".format(d=self.day,m=self.month,y=self.year)
d=Date()
print(d)