from abc import ABC
from abc import abstractmethod
class Phone(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def call(self):
        raise NotImplementedError("Hotalik")
    @abstractmethod
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
a=MobeliPhone()
