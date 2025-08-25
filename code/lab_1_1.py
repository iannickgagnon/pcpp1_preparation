class MobilePhone:
    
    def __init__(self, number):
        self.number = number
        
    def turn_on(self):
        return f"mobile phone {self.number} is turned on"
    
    def turn_off(self):
        return "mobile phone is turned off"
        
    def call(self, number):
        return f"calling {number}"
    
phone_1 = MobilePhone('450-123-4567')
phone_2 = MobilePhone('450-890-1234')

print(phone_1.turn_on())
print(phone_2.turn_on())
print(phone_1.call(phone_2.number))
print(phone_1.turn_off())
print(phone_2.turn_off())
