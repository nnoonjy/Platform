import datetime
import time
from enum import Enum
from abc import ABC

#Enumerations
class PaymentType(Enum):
    CREDIT_CARD, CASH = 1,2
    
class VehicleType(Enum):
    CAR, TRUCK, ELECTRONIC, MOTORCYCLE = 1,2,3,4
    
class ParkingTicketStatus(Enum):
    PAID, ACTIVE, DAILY_PASS, SALE = 1,2,3,4
    
class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, NONE = 1,2,3,4
    
#DataTypes
class Location:
    def __init__(self, streetAddress, city, country):
        self.streetAddresss = streetAddress
        self.city = city
        self.country = country
        
class Person:
    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        
class ParkingTicket:
    def __init__(self, ticketID, ticketStatus, payedAmount, carNumber, floor, vehicleType):
        self.ticketId = ticketID
        self.arriveTime = datetime.datetime.now()
        self.ticketStatus = ticketStatus
        self.payedAmount = payedAmount
        self.leaveTime = None
        self.carNumber = carNumber
        self.floor = floor
        self.vehicleType = vehicleType
    
#Account, Admin, Customer
class Account(ABC):
    def __init__(self, userId, userPassword, person, status = AccountStatus.ACTIVE):
        self.userId = userId
        self.userPassword = userPassword
        self.accountStatus = status
        self.person = person
        
        
class Admin(Account):
    def __init__(self, userId, userPassword, person, status = AccountStatus.ACTIVE):
        super().__init__(userId, userPassword, person, status)
        
    def modifyFee(self):
        None
    
    def modifyCarType(self):
        None
    
    def modifyParkingSpot(self):
        None
    
    def modifyTerminal(self):
        None
    
class Customer(Account):
    def __init__(self, userId, userPassword, status, carNumber, ticketStatus):
        super().__init__(userId, userPassword, status)
        self.carNumber = carNumber
        self.ticketStatus = ticketStatus
        
    def processTicket(self) -> ParkingTicketStatus:
        stat = input("choose ticket status\n\nPAID | ACTIVE | DAILY_PASS | SALE")
        #PAID, ACTIVE, DAILY_PASS, SALE = 1,2,3,4
        if stat == "PAID":
            return ParkingTicketStatus.PAID
        elif stat == "ACTIVE":
            return ParkingTicketStatus.ACTIVE
        elif stat == "DAILY_PASS":
            return ParkingTicketStatus.DAILY_PASS
        elif stat == "SALE":
            return ParkingTicketStatus.SALE
        else:
            raise Exception("wrong ticket status.")
        
#Terminal
class EntranceTerminal:
    def __init__(self, id, floor):
        self.id = id
        self.floor = floor
        
    def printTicket(self):
        pass
    
    def showStatus(self):
        pass
    
    def logIn(self):
        pass
        
class ExitTerminal:
    def __init__(self, id, floor):
        self.id = id
        self.floor = floor
        
    def paymentProcess(self, ticket:ParkingTicket):
        ticket.leaveTime = datetime.datetime.now()
        tmp_hour = ticket.leaveTime.hour - ticket.arriveTime.hour
        tmp_min = ticket.leaveTime.minute - ticket.arriveTime.minute
        
        if ticket.ticketStatus == ParkingTicketStatus.PAID:
            print(f'you already paid {ticket.payedAmount}')
        elif ticket.ticketStatus == ParkingTicketStatus.SALE:
            print(f'you should pay {tmp_hour *3000* 0.9}')
        elif ticket.ticketStatus == ParkingTicketStatus.DAILY_PASS:
            print('Thank you for Daily pass')
        elif ticket.ticketStatus == ParkingTicketStatus.ACTIVE:
            if tmp_min <= 15:
                print("it's free")
            else:
                print(f'you should pay {tmp_hour * 3000}')
        return 
    
    #ticketID, ticketStatus, payedAmount, carNumber, floor
    def scanTicket(self, ticket : ParkingTicket)-> tuple:
        return ticket.floor, ticket.ticketStatus, ticket.payedAmount
        
    
#ParkingSpot
class ParkingSpot(ABC):
    def __init__(self, spotNumber, type):
        self.spotNumber = spotNumber
        self.free = True
        self.type = type
        
    def ifFree(self) -> bool:
        return self.free
    
    def get_number(self):
        return self.spotNumber
    
class carSpot(ParkingSpot):
    def __init__(self, spotNumber, type):
        super().__init__(spotNumber, VehicleType.CAR)
    
class truckSpot(ParkingSpot):
    def __init__(self, spotNumber, type):
        super().__init__(spotNumber, VehicleType.TRUCK)
        
class motorcycleSpot(ParkingSpot):
    def __init__(self, spotNumber, type):
        super().__init__(spotNumber, VehicleType.MOTORCYCLE)
        
class electronicSpot(ParkingSpot):
    def __init__(self, spotNumber, type):
        super().__init__(spotNumber, VehicleType.ELECTRONIC)
        
    
#ParkingFloor
class ParkingFloor:
    def __init__(self, floor):
        self.floor = floor
        
    def isFullFloor(self) -> bool:
        pass
    
    def showFreeSpot(self):
        pass
    
    def updateStatus(self):
        pass
    
    def addParkingSpot(self):
        pass

#ParkingStatus
class ParkingStatus:
    def __init__(self, floor):
        self.floor = floor
        self.carFreeSpots = 0
        self.truckFreeSpots = 0
        self.electronicFreeSpots = 0
        self.motorcycleFreeSpots = 0
        
    def showStatus(self):
        pass
        
if __name__ == '__main__':
    while True:
        input = list(input().split())
        if input[0] == 'exit':
            print('program exit')
            break
        
        elif input[0] == 'display':
            pass
        
        elif input[0] == 'park':
            pass
        
        elif input[0] == 'unpark':
            pass
        
        elif input[0] == 'create_parking_lot':
            pass
        