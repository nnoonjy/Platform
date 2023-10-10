personalInfo = {
    "Admin": "1234"
}  # Admin정보가 default로 저장되어있음. 차가 추가될때마다 "차 번호":["차 종류", "층"] 형태로 추가
leftSpace = [
    [30, 10, 15, 15] for _ in range(5)
]  # 2차원 배열 형태로 일반차,전기차,오토바이,트럭 순으로 남은 좌석 기록


class carInfo:
    def __init__(self):
        self.id = id

    def newInfo(self, id, type):
        self.id = id
        self.type = type


def customerMode():
    carID = input("Enter your car ID : ")

    if carID in personalInfo:
        pass
    else:
        newCarInfo = []
        parkableSpace = []

        carType = int(
            input(
                "Enter your car type ( 1: General Car, 2: Electric Car, 3: Motorcycle, 4: Truck ) : "
            )
        )

        newCarInfo.append(carType)

        for i in range(5):
            parkableSpace.append(leftSpace[i][carType - 1])  # 층수별로 남은 공간 리스트에 저장

        # - todo. 층수별로 남은 갯수 안내

        floor = True
        chooseFloor = int(input("Choose the floor (1~5) : "))
        print(chooseFloor)
        while floor:
            if 1 <= chooseFloor <= 5:
                floor = False
                space = True
                while space:
                    if leftSpace[chooseFloor - 1][carType - 1] != 0:
                        space = False
                        print("Welcome !")
                        newCarInfo.append(chooseFloor)
                        personalInfo[carID] = newCarInfo  # 새로운 차 저장
                    else:
                        chooseFloor = int(
                            input("No space available on this floor. Choose again : ")
                        )

            else:
                chooseFloor = int(input("Wrong floor. Choose again (1~5) : "))


def adminMode():
    pass


if __name__ == "__main__":
    while True:
        mode = input("Enter the mode ( 1: Customer mode, 2: Admin mode ) : ")
        if mode == "1":
            customerMode()
        elif mode == "2":
            adminPass = input("Enter the password : ")
            if personalInfo["Admin"] == adminPass:
                adminMode()
            else:
                print("Wrong password. Please Start from the beginning.")

        print(personalInfo)
