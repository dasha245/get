import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = False):
        self.bus = smbus.SMbus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("")

        if not (0 <= number <= 4095):
            print("")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_date(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"число: {number}, отправленные по I2C данные [0x{(self.address << 1):02X}, 0x{first_byte:2X}, 0x{second_byte:2X}]\n")

    def set_voltage(self, voltage):
        if (0>voltage or voltage > 4095):
            print()
        self.set_number(int((voltage/self.dynamic_range)*4095))

if __name__ == "__main__":
    try:
        dac = MCP4725(5)
        while True:
            try:
                voltage = float(input("введите напряжение: "))
                dac.set_voltage(voltage)
            