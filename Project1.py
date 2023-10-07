from enum import Enum

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
    
#Account, Admin, Customer

#ParkingSpot

#ParkingFloor

#ParkingStatus

#ParkingLot(only one object for whole parking lot)