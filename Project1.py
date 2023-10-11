import datetime
import time
from enum import Enum
from abc import ABC


# Enumerations
class PaymentType(Enum):
    CREDIT_CARD, CASH = 1, 2


class VehicleType(Enum):
    CAR, TRUCK, ELECTRONIC, MOTORCYCLE = 1, 2, 3, 4


class ParkingTicketStatus(Enum):
    PAID, ACTIVE, DAILY_PASS, SALE = 1, 2, 3, 4


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, NONE = 1, 2, 3, 4


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


class ParkingTicket:
    def __init__(
        self, ticketID, ticketStatus, payedAmount, carNumber, floor, spot, vehicleType
    ):
        self.ticketId = ticketID
        self.arriveTime = datetime.datetime.now()
        self.ticketStatus = ticketStatus
        self.payedAmount = payedAmount
        self.leaveTime = None
        self.carNumber = carNumber
        self.floor = floor
        self.spot = spot
        self.vehicleType = vehicleType


# Account, Admin, Customer
class Account(ABC):
    def __init__(self, userId, userPassword, person, status=AccountStatus.ACTIVE):
        self.userId = userId
        self.userPassword = userPassword
        self.accountStatus = status
        self.person = person


class Admin(Account):
    def __init__(self, userId, userPassword, person, status=AccountStatus.ACTIVE):
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
    def __init__(self, userId, userPassword, status, carNumber):
        super().__init__(userId, userPassword, status)
        self.carNumber = carNumber


class ParkingLot:
    def __init__(self, id, floors, spots) -> None:
        self.id = id
        self.entranceTerminal = EntranceTerminal(id, floors, spots)
        self.exitTerminal = ExitTerminal(1, 1)
        self.customers = []
        self.tickets = {}

    def logIn(self, idCounter, carNumber, carType):
        self.customers.append(
            Customer(idCounter, idCounter, AccountStatus.ACTIVE, carNumber)
        )
        result = self.entranceTerminal.parkingStatus.park(carType)
        if result != None:
            self.tickets[carNumber] = ParkingTicket(
                idCounter,
                ParkingTicketStatus.ACTIVE,
                0,
                carNumber,
                result[0],
                result[1],
                carType,
            )
        return result

    def logOut(self, carNumber):
        for index_customer, customer in enumerate(self.customers):
            if customer.carNumber == carNumber:
                del parkingLot.customers[index_customer]
                return True
        return False


# Terminal
class EntranceTerminal:
    def __init__(self, id, floors, spots):
        self.id = id
        self.parkingStatus = ParkingStatus(floors, spots)

    def printTicket(self):
        print("Ticket has been printed!")

    def showStatus(self):
        self.parkingStatus.displayFreeSpots(VehicleType.CAR)
        self.parkingStatus.displayFreeSpots(VehicleType.TRUCK)
        self.parkingStatus.displayFreeSpots(VehicleType.MOTORCYCLE)
        self.parkingStatus.displayFreeSpots(VehicleType.ELECTRONIC)


class ExitTerminal:
    def __init__(self, id, floor):
        self.id = id
        self.floor = floor

    def paymentProcess(self, ticket: ParkingTicket):
        ticket.leaveTime = datetime.datetime.now()
        tmp_hour = ticket.leaveTime.hour - ticket.arriveTime.hour
        tmp_min = ticket.leaveTime.minute - ticket.arriveTime.minute
        print(f"Vehicle with number {ticket.carNumber} unparked successfully!")
        if ticket.ticketStatus == ParkingTicketStatus.PAID:
            print(f"You already paid {ticket.payedAmount}")
        elif ticket.ticketStatus == ParkingTicketStatus.SALE:
            print(f"You should pay {tmp_hour *3000* 0.9}")
        elif ticket.ticketStatus == ParkingTicketStatus.DAILY_PASS:
            print("Thank you for Daily pass")
        elif ticket.ticketStatus == ParkingTicketStatus.ACTIVE:
            if tmp_min <= 15:
                print("It's free")
            else:
                print(f"You should pay {tmp_hour * 3000}")
        return

    # ticketID, ticketStatus, payedAmount, carNumber, floor
    def scanTicket(self, ticket: ParkingTicket) -> tuple:
        return ticket.floor, ticket.ticketStatus, ticket.payedAmount


# ParkingSpot
class ParkingSpot(ABC):
    def __init__(self, spotNumber, type):
        self.spotNumber = spotNumber
        self.free = True
        self.type = type

    def ifFree(self) -> bool:
        return self.free

    def get_number(self):
        return self.spotNumber


class CarSpot(ParkingSpot):
    def __init__(self, spotNumber):
        super().__init__(spotNumber, VehicleType.CAR)


class TruckSpot(ParkingSpot):
    def __init__(self, spotNumber):
        super().__init__(spotNumber, VehicleType.TRUCK)


class MotorcycleSpot(ParkingSpot):
    def __init__(self, spotNumber):
        super().__init__(spotNumber, VehicleType.MOTORCYCLE)


class ElectronicSpot(ParkingSpot):
    def __init__(self, spotNumber):
        super().__init__(spotNumber, VehicleType.ELECTRONIC)


# ParkingFloor
class ParkingFloor:
    def __init__(self, floor, spots):
        self.floor = floor
        self.spots = []
        self.__numberOfSpots = 0
        for _ in range(spots):
            self.spots.append(CarSpot(self.__numberOfSpots))
            self.__numberOfSpots += 1
            self.spots.append(TruckSpot(self.__numberOfSpots))
            self.__numberOfSpots += 1
            self.spots.append(MotorcycleSpot(self.__numberOfSpots))
            self.__numberOfSpots += 1
            self.spots.append(ElectronicSpot(self.__numberOfSpots))
            self.__numberOfSpots += 1

    def isFullFloor(self, type) -> bool:
        for spot in self.spots:
            if spot.type.name == type and spot.free == True:
                return True
        return False

    def showFreeSpot(self, type):
        freeSpots = []
        for spot in self.spots:
            if spot.free == True and spot.type.name == type:
                freeSpots.append(spot)
        return freeSpots

    def showOccupiedSpot(self, type):
        occupiedSpots = []
        for spot in self.spots:
            if spot.free == False and spot.type.name == type:
                occupiedSpots.append(spot)
        return occupiedSpots

    def updateStatus(self, spotNumber, status):
        for spot in self.spots:
            if spot.spotNumber == spotNumber:
                spot.free = status
                return


# ParkingStatus
class ParkingStatus:
    def __init__(self, floor, spots):
        self.__floors = []
        self.__numberOfFloors = floor
        for i in range(floor):
            self.__floors.append(ParkingFloor(i, spots))

    def displayCount(self, type):
        for floor in self.__floors:
            freeSpots = floor.showFreeSpot(type)
            print(
                f"Number of free spots for {type} on Floor {floor.floor}: {len(freeSpots)}"
            )

    def displayFreeSpots(self, type):
        for floor in self.__floors:
            freeSpots = floor.showFreeSpot(type)
            if len(freeSpots) == 0:
                print(f"No free spots for {type} in Floor {floor.floor}!")
            else:
                print(
                    f"Free spots for {type} on Floor {floor.floor}: {[spot.spotNumber for spot in freeSpots]}"
                )

    def displayOccupiedSpots(self, type):
        for floor in self.__floors:
            occupiedSpots = floor.showOccupiedSpot(type)
            if len(occupiedSpots) == 0:
                print(f"All spots are free for {type} in Floor {floor.floor}!")
            else:
                print(
                    f"Occupied spots for {type} on Floor {floor.floor}: {[spot.spotNumber for spot in occupiedSpots]}",
                )

    def park(self, type):
        for index_floor in range(len(self.__floors)):
            for index_spot in range(len(self.__floors[index_floor].spots)):
                if (
                    self.__floors[index_floor].spots[index_spot].free == True
                    and self.__floors[index_floor].spots[index_spot].type.name == type
                ):
                    self.__floors[index_floor].spots[index_spot].free = False
                    return (index_floor, index_spot)
        return None

    def unpark(self, floorNumber, spotNumber):
        self.__floors[floorNumber].spots[spotNumber].free = True


if __name__ == "__main__":
    parkingLot = None
    idCounter = 0
    while True:
        user_input = list(input().split())
        if user_input[0] == "exit":
            print("program exit")
            break

        elif user_input[0] == "display":
            if user_input[1] == "free_slots":
                parkingLot.entranceTerminal.parkingStatus.displayFreeSpots(
                    user_input[2]
                )
            elif user_input[1] == "occupied_slots":
                parkingLot.entranceTerminal.parkingStatus.displayOccupiedSpots(
                    user_input[2]
                )
            else:
                parkingLot.entranceTerminal.parkingStatus.displayCount(user_input[2])

        elif user_input[0] == "park":
            result = parkingLot.logIn(idCounter, user_input[2], user_input[1])
            if result != None:
                print(
                    f"Parked vehicle! Ticket ID: {parkingLot.id}_{result[0]}_{result[1]}"
                )
            else:
                print("Parking lot full!")
            idCounter += 1
        elif user_input[0] == "unpark":
            result = parkingLot.logOut(user_input[1])
            if result == True:
                parkingLot.exitTerminal.paymentProcess(
                    parkingLot.tickets[user_input[1]]
                )
                parkingLot.entranceTerminal.parkingStatus.unpark(
                    parkingLot.tickets[user_input[1]].floor,
                    parkingLot.tickets[user_input[1]].spot,
                )
            else:
                print("Ticket not found!")
        elif user_input[0] == "create_parking_lot":
            parkingLot = ParkingLot(
                user_input[1], int(user_input[2]), int(user_input[3])
            )
        else:
            print("Command unknown!")
