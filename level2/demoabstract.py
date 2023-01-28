from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def payment(self,amt):
        pass
    def gen_slip(self,amt):
        print(amt)
class Creditcard(payment):
    def payment(self,amt):
        print("paid amount using credit card")
    def gen_slip(self,amt):
        print(amt)
class Debitcard(payment):
    def payment(self,amt):
        print("paid amount using debit card")
    def gen_slip(self,amt):
        print(amt)
obj1=Creditcard()
obj1.payment(350)
obj1.gen_slip(350)
obj2=Debitcard()
obj2.payment(1200)
obj2.gen_slip(1200)
