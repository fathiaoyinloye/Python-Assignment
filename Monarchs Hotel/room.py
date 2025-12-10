from RoomStatus import RoomStatus
from RoomType import RoomType
class Room:

    def __init__(self, roomType: RoomType):
        self.__number = 0
        self.__type = roomType
        self.__price = roomType.value
        self.status = RoomStatus.AVAILABLE

    @property
    def getRoomNumber(self):
        return self.number
    def setRoomNumber(self, number):
        self.number = number
    @property
    def getRoomType(self):
        return self.type

    def setRoomType(self, roomType: RoomType):
        self.type = roomType

    def setRoomStatus(self, room_status: RoomStatus):
        self.status = room_status
    def getRoomStatus(self):
        return self.status
    def getRoomPrice(self):
        return self.price
