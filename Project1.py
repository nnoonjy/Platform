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
    def __init__(self, ticketID, ticketStatus, payedAmount, carNumber):
        self.ticketId = ticketID
        self.arriveTime = datetime.datetime.now()
        self.ticketStatus = ticketStatus
        self.payedAmount = payedAmount
        self.leaveTime = None
        self.carNumber = carNumber
    
#Account, Admin, Customer
class Account(ABC):
    def __init__(self, userId, userPassword, person, status = AccountStatus.ACTIVE):
        self.userId = userId
        self.userPassword = userPassword
        self.accountStatus = status
        self.person = person
        
        
class Admin(Account):
    def modifyFee(self):
        pass
    
    def modifyCarType(self):
        pass
    
    def modifyParkingSpot(self):
        pass
    
    def modifyTerminal(self):
        pass
    
class Customer(Account):
    def __init__(self, userId, userPassword, status, carNumber, ticketStatus):
        super().__init__(userId, userPassword, status)
        self.carNumber = carNumber
        self.ticketStatus = ticketStatus
        
    def processTicket(self) -> ParkingTicket:
        stat = input("choose ticket status")
        # need nested if statements
        
#Terminal
class Terminal(ABC):
    def __init__(self, id, floor):
        self.id = id
        self.floor = floor

class EntranceTerminal(Terminal):
    def __init__(self, id, floor):
        super().__init__(id, floor)
        
    def printTicket(self):
        pass
    
    def showStatus(self):
        pass
    
    def logIn(self):
        pass
        
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
        self.carFreeSpot = None

#ParkingLot(only one object for whole parking lot)