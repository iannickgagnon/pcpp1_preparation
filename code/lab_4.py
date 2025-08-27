
# This is an example that illustrated Method Resolution Order (MRO)
class Scanner:
    
    def scan(self):
        print("Scanning from Scanner!")
        
class Printer:
    
    def print(self):
        print("Printing from Printer!")

class Fax:
    
    def print(self):
        print("Printing from Fax!")
    
    def send(self):
        print("Sending from Fax!")

class MultiFunctionDevice_SPF(Scanner, Printer, Fax):
    pass
    
class MultiFunctionDevice_SFP(Scanner, Fax, Printer):
    pass

# Runner code
device_spf = MultiFunctionDevice_SPF()
device_sfp = MultiFunctionDevice_SFP()

device_spf.print() # Inherits from Printer before Fax
device_sfp.print() # Inherits from Fax before Printer
