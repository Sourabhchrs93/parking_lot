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
            line = file_obj.readline()
            while line:
                if line.endswith('\n'):
                    line = line[:-1]
                self.execute_operation(line)
                line = file_obj.readline()
        except StopIteration:
            file_obj.close()
        except Exception as ex:
            print("Error while processing file {}".format(ex))

    def process_cmd(self):
        try:
            while True:
                stdin_input = input("Enter command: ")
                if stdin_input == 'exit':
                    return 
                self.execute_operation(stdin_input)
        except (KeyboardInterrupt, SystemExit):
            return
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
    if len(args) == 1:
        pass
        get_inputs = GetInputs()
        get_inputs.process_cmd()
    elif len(args) == 2:
        get_inputs = GetInputs()
        get_inputs.read_input_file(args[1])
    else:
        print("Wrong number of arguments.\n"
              "Usage:\n"
              "./parking_lot.py <filename> OR \n"
              "./parking_lot.py")
