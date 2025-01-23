class RBI:
    def register(self):
        print('RBI Register Method')
class SBI:
    def createaccount(self):
        print('SBI Class Method')
class CreditCard:
    def services(self):
        print('CreditCard Services')
class Customer(RBI,SBI,CreditCard):
    def display(self):
        print('Customer Class display Method')
C1=Customer()
C1.register()
C1.createaccount()
C1.services()
C1.display()
