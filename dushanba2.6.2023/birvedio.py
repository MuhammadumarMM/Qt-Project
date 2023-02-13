class Phone:
    def __init__(self) -> None:
        pass
    def call(self):
        raise NotImplementedError("Hotalik")
    def send_massege(self):
        raise NotImplementedError("Xatolik")
class MobeliPhone(Phone):
    def __init__(self,m:str) -> None:
        super().__init__()
        self.__mark=''
    def call(self):
        print("Calling")
    def send_massege(self,s:str):
        print("Sms.."+s)
sms=MobeliPhone("SAMSUNG")
sms.call()
sms.send_massege("Hello")