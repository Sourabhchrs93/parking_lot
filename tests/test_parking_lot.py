import unittest
from src.parking_lot import ParkingLot


class TestParkingLot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parking = ParkingLot()
        cls.allocated_slot = 1

    def test_create_parking_lot(self):
        parking_slots = 4
        self.parking.create_parking_lot(parking_slots)
        self.assertEqual(self.parking.size, parking_slots, msg="Wrong parking lot created")

    def test_park(self):
        reg_number = 'KA-01-HH-2701'
        colour = 'White'
        self.parking.park(reg_number, colour)
        self.assertEqual(self.parking.parking_lot[self.allocated_slot]._reg_no, reg_number)
        self.assertEqual(self.parking.parking_lot[self.allocated_slot]._colour, colour)

    # next parking will go to slot no = 2

    def test_leave(self):
        slot = 2
        self.parking.leave(slot)
        keys = self.parking.parking_lot.keys()
        self.assertNotIn(slot, keys)
