from datetime import datetime
from decimal import Decimal

class Ticket:
    def __init__(self, id: int, departure_time: datetime, arrival_zone: int, arrival_time: datetime,
                 route_number: int, departure_zone: int, buyer_id: int, is_used: bool, price: Decimal, place: str):
        self._id = id
        self._departure_time = departure_time
        self._arrival_zone = arrival_zone
        self._arrival_time = arrival_time
        self._route_number = route_number
        self._departure_zone = departure_zone
        self._buyer_id = buyer_id
        self._is_used = is_used
        self._price = price
        self._place = place

    def get_id(self):
        return self._id

    def get_departure_time(self):
        return self._departure_time

    def get_arrival_zone(self):
        return self._arrival_zone

    def get_arrival_time(self):
        return self._arrival_time

    def get_route_number(self):
        return self._route_number

    def get_departure_zone(self):
        return self._departure_zone

    def get_buyer_id(self):
        return self._buyer_iduu

    def get_is_used(self):
        return self._is_used

    def get_price(self):
        return self._price

    def get_place(self):
        return self._place

    def is_valid_for_purchase(self):
        # определение возможности покупки
        return not self._is_used

