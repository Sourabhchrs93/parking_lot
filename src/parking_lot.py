from car import Car


class ParkingLot:
    def __init__(self,):
        self.size = None
        self.parking_lot = dict()
        self.min_available_slot = 1

    def create_parking_lot(self, size):
        if self.size is not None:
            print("parking lot already created")
            return
        if size < 1:
            raise ValueError("only non-zero positive value is allowed for slots")
        self.size = size
        print('Created a parking lot with {} slots'.format(self.size))
        return

    def park(self, reg_number, colour):
        if not self.is_exist():
            return
        if self.min_available_slot > self.size:
            print("Sorry, parking lot is full")
            return
        slot = self.min_available_slot
        car = Car(reg_number, colour)
        self.parking_lot[slot] = car

        self.min_available_slot = self.find_next_available_slot(slot)
        print('Allocated slot number: {}'.format(slot))
        return

    def leave(self, slot):
        if not self.is_exist():
            return
        if slot not in self.parking_lot:
            print("Slot {} is already empty".format(slot))
            return
        del self.parking_lot[slot]
        if slot < self.min_available_slot:
            self.min_available_slot = slot
        print("Slot number {} is free".format(slot))
        return

    def status(self):
        if not self.is_exist():
            return
        print('Slot No.\tRegistration No\tColour')
        for slot in range(1, self.size + 1):
            if slot in self.parking_lot:
                print(slot, '\t\t\t', self.parking_lot[slot].get_reg_no(), '\t', self.parking_lot[slot].get_colour())
            else:
                print(slot, '\t\t\t', None, '\t\t\t', None)
        return

    def registration_numbers_for_cars_with_colour(self, colour):
        if not self.is_exist():
            return
        car_list = []
        for slot in sorted(self.parking_lot):
            if self.parking_lot[slot].get_colour() == colour:
                car_list.append(self.parking_lot[slot].get_reg_no())
        print(', '.join(car_list))
        return

    def slot_numbers_for_cars_with_colour(self, colour):
        if not self.is_exist():
            return
        slot_list = []
        for slot in sorted(self.parking_lot):
            if self.parking_lot[slot].get_colour() == colour:
                slot_list.append(str(slot))
        print(', '.join(slot_list))
        return

    def slot_number_for_registration_number(self, reg_number):
        if not self.is_exist():
            return
        for slot in self.parking_lot:
            if self.parking_lot[slot].get_reg_no() == reg_number:
                print(slot)
                return
        print("Not found")
        return

    def find_next_available_slot(self, start_slot):
        for slot in range(start_slot+1, self.size +1):
            if slot not in self.parking_lot:
                return slot
        return self.size + 1

    def is_exist(self):
        if self.size is None:
            print('parking lot is not created')
            return False
        return True

