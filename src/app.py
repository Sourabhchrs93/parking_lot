import os, sys
from parking_lot import ParkingLot


class GetInputs:
    def __init__(self):
        self.parking = ParkingLot()

    def read_input_file(self, file):
        if not os.path.exists(file):
            print("file does not exist in given path")

        file_obj = open(file, 'r')
        try:
            while True:
                line = file_obj.readline()
                if line.endswith('\n'):
                    line = line[:-1]
                if line == '':
                    continue
                self.execute_operation(line)
        except StopIteration:
            file_obj.close()
        except Exception as ex:
            print("Error while processing file {}".format(ex))

    def execute_operation(self, cmd):
        input_line = cmd.split()

        operation = input_line[0]
        params = input_line[1:]
        if hasattr(self.parking, operation):
            get_attr = getattr(self.parking, operation)
            get_attr(*params)
        else:
            print('invalid Operation')
        return


if __name__ == "__main__":
    args = sys.argv
    print(args)
    if len(args) == 1:
        pass
        # get_inputs = GetInputs()
        # get_inputs.process_input()
    elif len(args) == 2:
        get_inputs = GetInputs()
        get_inputs.read_input_file(args[1])
    else:
        print("Wrong number of arguments.\n"
              "Usage:\n"
              "./parking_lot.py <filename> OR \n"
              "./parking_lot.py")

'''
from parking_lot import ParkingLot


parking = ParkingLot()

parking.create_parking_lot(4)

parking.park('KA-01-HH-1', 'White')
parking.park('KA-01-HH-2', 'White')
parking.park('KA-01-HH-3', 'White')
parking.park('KA-01-HH-4', 'Red')

parking.create_parking_lot(4)

parking.status()
parking.leave(3)
parking.leave(3)
parking.leave(2)

parking.park('KA-01-HH-22', 'Red')
parking.park('KA-01-HH-33', 'Red')

parking.status()

parking.leave(1)
parking.status()

parking.registration_numbers_for_cars_with_colour('Red')
parking.slot_numbers_for_cars_with_colour('Red')

parking.slot_number_for_registration_number('KA-01-HH-4')
parking.slot_number_for_registration_number('KA-01-HH-2')
'''
