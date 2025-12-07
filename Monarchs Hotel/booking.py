
from Guest import Guest
from Hotel import Hotel
from RoomStatus import RoomStatus
from RoomType import RoomType


class Bookings:

    def __init__(self):
         self.bookings = {}
         self.reference_number = "BRN"
         self.count = 0
         self.check_in_date = 0
         self.check_out_date = 0
         self.number_of_days = 0
         self.payment = 0


    def check_room_availability (self, hotel : Hotel, room_type : RoomType):
        room_booked = 0
        for room in hotel.getRooms():
            if room.getRoomType() == room_type:
                room_booked = room
                room.setRoomStatus(RoomStatus.OCCUPIED)
                break
        return room_booked
    def set_number_of_days (self, number_of_days):
        self.number_of_days = number_of_days

    def get_number_of_days(self):
        return self.number_of_days

    def get_booked(self,hotel : Hotel, room_type : RoomType, guest: Guest):
      room_booked =  self.check_room_availability(hotel, room_type)
      if room_booked != 0:
          self.count = self.count + 1
          booking = []
          booking.append(guest)
          booking.append(room_booked)
          self.payment = self.payment + room_type.value * self.number_of_days
          booking.append(self.payment)
          booking_reference_number = f"BRN{self.count}"
          booking.append(booking_reference_number)
          booking.append(f"Your Check in date: {self.check_in_date}, and your check out date: {self.check_out_date}")
          self.bookings[booking_reference_number] = booking

          return f"You Have Successfully Booked Room {room_booked.getRoomNumber()} and your booking reference number is  {booking_reference_number}"
      else:
          return "room not available"



    def check_date_validity(self,inputed_date):
        from datetime import datetime
        try:
            date = datetime.strptime(inputed_date, "%Y-%m-%d")
            self.check_in_date = date
            return True
        except ValueError:
            return False

    def calculate_check_out_date(self, date):
        from datetime import timedelta
        check_in_date = date
        duration = timedelta(days = self.number_of_days)
        check_out_date = date + duration
        self.check_out_date = check_out_date

    def get_all_bookings(self):
        return self.bookings














