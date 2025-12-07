from RoomStatus import RoomStatus
from room import Room
from Hotel import Hotel

class Admin:
    def __init__(self):
        self.name = "Madam Eniife"
        self.password = "1234"
        self.room_number = 16

    def add_room(self, password, room_type, hotel):
        if password == self.password:
            hotel.add_room(room_type)
        else:
            raise ValueError("Passwords don't match")

    def view_all_rooms(self, hotel):
       return hotel.getRooms()

    def change_room_status(self, roomNumber,hotel):
        result = ""
        room = hotel.find_room(roomNumber)
        if room != 0 and room.getRoomStatus() != RoomStatus.OCCUPIED:
            room.setRoomStatus(RoomStatus.ONMAINTENANCE)
            return f"Room {room.getRoomNumber()} is on Maintenance"
        elif room == 0:
            return "Room not found"
        else:
            return "Room is currently Occupied"




