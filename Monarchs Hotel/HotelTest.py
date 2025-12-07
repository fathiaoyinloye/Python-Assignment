import unittest

import room
from Guest import Guest
from Hotel import Hotel
from RoomStatus import RoomStatus
from RoomType import RoomType
from admin import Admin
from booking import Bookings
from room import Room


class MyTestCase(unittest.TestCase):
  #  def setUp(self):
   #     hotel = Hotel()
    #    hotel.crete_default_rooms()
     #   admin = Admin()

    def test_that_an_hotel_has_rooms(self):
        hotel = Hotel()
        hotel.crete_default_rooms()
        admin = Admin()
        number_of_rooms = hotel.get_number_of_Rooms()
        self.assertEqual(15, number_of_rooms)


    def test_that_an_admin_can_add_to_the_available_rooms(self):
        hotel = Hotel()
        hotel.crete_default_rooms()
        admin = Admin()
        admin.add_room("1234", RoomType.SUITE, hotel)
        self.assertEqual(16, hotel.get_number_of_Rooms())

    def test_that_an_admin_can_view_rooms(self):
        hotel = Hotel()
        hotel.crete_default_rooms()
        admin = Admin()
        rooms = admin.view_all_rooms(hotel)
        admin.add_room("1234", RoomType.SUITE, hotel)
        #for room in rooms:
         #   print(room.getRoomNumber(), room.getRoomType().name, room.getRoomPrice(),  room.getRoomStatus().name)

    def test_that_an_admin_can_change_room_status(self):
        hotel = Hotel()
        hotel.crete_default_rooms()
        admin = Admin()
        actual = admin.change_room_status(1,hotel)
        self.assertEqual(actual,"Room 1 is on Maintenance")
    def test_that_an_admin_cannor_change_room_status_of_incorrect_room_number(self):
        hotel = Hotel()
        hotel.crete_default_rooms()
        admin = Admin()
        actual = admin.change_room_status(20,hotel)
        self.assertEqual(actual,"Room not found")

    def test_that_guest_can_book_a_room(self):
        hotel = Hotel()
        hotel.crete_default_rooms()
        admin = Admin()
        booking = Bookings()
        guest = Guest("fathia", "05678", 'dfghjk')
        booking.check_room_availability(hotel,RoomType.SUITE)
        response = booking.get_booked(hotel,RoomType.SUITE, guest)
        self.assertEqual(response,"You Have Successfully Booked Room 11 and your booking reference number is  BRN1")

    def test_that_a_room_is_booked_and_the_room_status_changed_to_is_occupied(self):
        hotel = Hotel()
        hotel.crete_default_rooms()
        admin = Admin()
        booking = Bookings()
        guest = Guest("fathia", "05678", 'dfghjk')
        room = booking.check_room_availability(hotel, RoomType.SUITE)
        response = booking.get_booked(hotel, RoomType.SUITE, guest)
        self.assertEqual(response, "You Have Successfully Booked Room 11 and your booking reference number is  BRN1")
        rooms = admin.view_all_rooms(hotel)
        self.assertEqual(RoomStatus.OCCUPIED, room.getRoomStatus())
        #for room in rooms:
        #   print(room.getRoomNumber(), room.getRoomType().name, room.getRoomPrice(), room.getRoomStatus().name)

    def test_that_two_guest_booked_a_room_and_refernce_number_is_different(self):
        hotel = Hotel()
        hotel.crete_default_rooms()
        admin = Admin()
        booking = Bookings()
        guest = Guest("fathia", "05678", 'dfghjk')
        booking.check_room_availability(hotel, RoomType.SUITE)
        response = booking.get_booked(hotel, RoomType.SUITE, guest)
        self.assertEqual(response, "You Have Successfully Booked Room 11 and your booking reference number is  BRN1")
        guest = Guest("bola", "05678", 'dfgjk')
        booking.check_room_availability(hotel, RoomType.SINGLE)
        response = booking.get_booked(hotel, RoomType.SINGLE, guest)
        self.assertEqual(response, "You Have Successfully Booked Room 1 and your booking reference number is  BRN2")


    def test_that_check_in_date_is_in_the_right_format(self):
        booking = Bookings()
        date_inputed = "43500"
        self.assertFalse(booking.check_date_validity(date_inputed))
        date_input = "2025-12-21"
        self.assertTrue(booking.check_date_validity(date_input))

    def test_that_a_guest_can_edit_their_details(self):
        guest = Guest("fathia", "05678", 'dfghjk')
        guest.set_name("Omotemmy")
        self.assertEqual(guest.get_name(), "Omotemmy")
        guest.set_email("fathiaOyinloye21@gmail.com")
        self.assertEqual(guest.get_email(), "fathiaOyinloye21@gmail.com")
        guest.set_phone_number("07048254250")
        self.assertEqual(guest.get_phone_number(), "07048254250")
