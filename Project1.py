from enum import Enum

# Enumerations

PaymentType = {1: "CREDIT_CARD", 2: "CASH"}
VehicleType = {1: "CAR", 2: "TRUCK", 3: "ELECTRONIC", 4: "MOTORCYCLE"}
ParkingTicketStatus = {1: "PAID", 2: "ACTIVE", 3: "DAILY_PASS", 4: "SALE"}
AccountStatus = {1: "ACTIVE", 2: "CLOSED", 3: "CANCLED", 4: "NONE"}

# class PaymentType(Enum):
#     CREDIT_CARD, CASH = 1,2

# class VehicleType(Enum):
#     CAR, TRUCK, ELECTRONIC, MOTORCYCLE = 1,2,3,4

# class ParkingTicketStatus(Enum):
#     PAID, ACTIVE, DAILY_PASS, SALE = 1,2,3,4

# class AccountStatus(Enum):
#     ACTIVE, CLOSED, CANCELED, NONE = 1,2,3,4


# DataTypes
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


# Account, Admin, Customer
class Account:
    def __init__(self, userId, userPassword, status):
        self.userId = userId
        self.userPassword = userPassword
        self.status = status


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
    def __init__(self, carNumber):
        self.carNumber = carNumber

    def processTicket():
        pass


# ParkingSpot
class ParkingSpot:
    def __init__(self, spotNumber, free, type, isFree):
        self.spotNumber = spotNumber
        self.free = free
        self.type = type
        self.isFree = isFree


class carSpot(ParkingSpot):
    print("This is car spot.")


class truckSpot(ParkingSpot):
    pass


class motorcycleSpot(ParkingSpot):
    pass


class electronicSpot(ParkingSpot):
    pass


# ParkingFloor
class parkingFloor:
    def __init__(self):
        pass


# ParkingStatus
class parkingStatus:
    def __init__(self):
        pass


# ParkingLot(only one object for whole parking lot)
class parkingLot:
    def __init__(self):
        pass


if __name__ == "__main__":
    pass
