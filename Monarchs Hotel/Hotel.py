import room
from RoomStatus import RoomStatus
from RoomType import RoomType
from room import Room


class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.count = 15

    def crete_default_rooms(self):
        for number in range(1, 16):
            if number < 6:
                room = Room(RoomType.SINGLE)
                room.setRoomNumber(number)
                self.rooms.append(room)
            elif number < 11:
                room = Room(RoomType.DOUBLE)
                room.setRoomNumber(number)
                self.rooms.append(room)
            elif number < 16:
                room = Room(RoomType.SUITE)
                room.setRoomNumber(number)
                self.rooms.append(room)


    def add_room(self, roomType):
        room = Room(roomType)
        self.count = self.count + 1
        room.setRoomNumber(self.count)
        self.rooms.append(room)

    def add_guest(self, guest):
        self.guests.append(guest)

    def getRooms(self):
        return self.rooms
    def get_number_of_Rooms(self):
        return len(self.rooms)

    def get_guests(self):
        return self.guests
    def get_guests_numbers(self):
        return len(self.guests)

    def find_room(self, roomNumber):
        find_room = 0
        for room in self.rooms:
            if room.getRoomNumber() == roomNumber:
                find_room = room

        return find_room




