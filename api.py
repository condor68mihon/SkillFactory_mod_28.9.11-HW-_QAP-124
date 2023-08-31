from pydantic import BaseModel
from typing import Optional
import requests
from settings import settings

class BookingRequest(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    additionalneeds: Optional[str] = None


class BookingResponse(BaseModel):
    bookingid: int
    booking: BookingRequest


def create_booking(booking_data: BookingRequest) -> BookingResponse:
    url = "https://example.com"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=booking_data.dict())

    if response.status_code == 200:
        return BookingResponse(**response.json())
    else:
        raise ValueError("Failed to create booking")


def get_booking(booking_id: int) -> BookingResponse:
    url = f"https://example.com/booking/{booking_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return BookingResponse(**response.json())
    else:
        raise ValueError("Failed to get booking")


def get_bookings() -> list[BookingResponse]:
    url = "https://example.com/booking"
    response = requests.get(url)

    if response.status_code == 200:
        bookings_data = response.json()
        bookings = []
        for booking_data in bookings_data:
            bookings.append(BookingResponse(**booking_data))
        return bookings
    else:
        raise ValueError("Failed to get bookings")


def update_booking(booking_id: int, booking_data: BookingRequest) -> BookingResponse:
    url = f"https://example.com/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(url, headers=headers, json=booking_data.dict())

    if response.status_code == 200:
        return BookingResponse(**response.json())
    else:
        raise ValueError("Failed to update booking")


def delete_booking(booking_id: int) -> None:
    url = f"https://example.com/booking/{booking_id}"
    response = requests.delete(url)

    if response.status_code != 204:
        raise ValueError("Failed to delete booking")
