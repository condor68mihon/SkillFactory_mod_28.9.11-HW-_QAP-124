import unittest
from api import *


class TestAPI(unittest.TestCase):

    def test_create_booking(self):
        booking_data = BookingRequest(
            firstname="Mihon",
            lastname="Job",
            totalprice=100,
            depositpaid=True,
            additionalneeds="Breakfast"
        )
        created_booking = create_booking(booking_data)
        self.assertIsInstance(created_booking, BookingResponse)
        self.assertEqual(created_booking.booking.firstname, "John")
        self.assertEqual(created_booking.booking.lastname, "Doe")
        self.assertEqual(created_booking.booking.totalprice, 100)
        self.assertTrue(created_booking.booking.depositpaid)
        self.assertEqual(created_booking.booking.additionalneeds, "Breakfast")

    def test_get_booking(self):
        booking_id = 1
        booking = get_booking(booking_id)
        self.assertIsInstance(booking, BookingResponse)
        self.assertEqual(booking.bookingid, booking_id)

    def test_get_bookings(self):
        bookings = get_bookings()
        self.assertIsInstance(bookings, list)
        for booking in bookings:
            self.assertIsInstance(booking, BookingResponse)

    def test_update_booking(self):
        booking_id = 1
        updated_booking_data = BookingRequest(
            firstname="Updated",
            lastname="Booking",
            totalprice=200,
            depositpaid=False,
            additionalneeds=None
        )
        updated_booking = update_booking(booking_id, updated_booking_data)
        self.assertIsInstance(updated_booking, BookingResponse)
        self.assertEqual(updated_booking.booking.firstname, "Updated")
        self.assertEqual(updated_booking.booking.lastname, "Booking")
        self.assertEqual(updated_booking.booking.totalprice, 200)
        self.assertFalse(updated_booking.booking.depositpaid)
        self.assertIsNone(updated_booking.booking.additionalneeds)

    def test_delete_booking(self):
        booking_id = 1
        delete_booking(booking_id)
        with self.assertRaises(ValueError):
            get_booking(booking_id)

    def test_invalid_get_booking(self):
        invalid_booking_id = 99999
        with self.assertRaises(ValueError):
            get_booking(invalid_booking_id)

    def test_invalid_update_booking(self):
        invalid_booking_id = 99999
        invalid_booking_data = BookingRequest(
            firstname="Invalid",
            lastname="Booking",
            totalprice=200,
            depositpaid=False,
            additionalneeds=None
        )
        with self.assertRaises(ValueError):
            update_booking(invalid_booking_id, invalid_booking_data)

    def test_invalid_delete_booking(self):
        invalid_booking_id = 99999
        with self.assertRaises(ValueError):
            delete_booking(invalid_booking_id)


if __name__ == '__main__':
    unittest.main()
