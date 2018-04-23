import math


class Transmission(object):
    pass


class ManualTransmission(Transmission):

    def __init__(self, gear_data, final_drive_ratio, wheel_radius, redline, speed=0.):

        self.gears = []

        for key in gear_data:
            setattr(self, "gear_{}".format(key), gear_data[key])
            self.gears.append(getattr(self, "gear_{}".format(key), gear_data[key]))

        self.final_drive_ratio = final_drive_ratio
        self.wheel_radius = wheel_radius
        self.redline = redline

        self.rpm = None
        self._gear_index = 0
        self._gear = self.gears[self._gear_index]  # Start the transmission in first gear

        self._set_rpm_gear(speed)  # Find the first valid gear to initialize the car with

    def _calculate_current_rpm(self, speed):
        """
        Calculates the current rpm of the engine given the cars speed (in m/s)

        :param speed:
        :return:
        """
        self.rpm = speed * 60. * 1 / (self.wheel_radius * 2 * math.pi) * self._gear * self.final_drive_ratio

    def speed_from_transmission(self):
        """
        Calculates the cars speed given the transmission's current state

        :return: (float) Estimated road speed from the transmissions state (m/s)
        """
        return self.rpm * (1. / 60.) * self.wheel_radius * 2 * math.pi * 1 / (self._gear * self.final_drive_ratio)

    def _upshift(self):
        """
        Attempts to put the transmission into the next highest gear


        :return:
        """
        self._gear_index += 1
        self._gear = self.gears[self._gear_index]

    def manual_shift(self, gear_index):
        """
        Enables external user to try to shift the transmission into the given gear_index

        :return:
        """
        try:
            speed = self.speed_from_transmission()
            self._gear_index = gear_index
            self._gear = self.gears[self._gear_index]
            self.update_rpm(speed)
            print('--------CLUNK-----------')
        except ValueError:
            print('invalid_shift')

    def _set_rpm_gear(self, speed):
        """
        Sets the car to the first appropriate gear and engine speed based on a passed initial car speed

        First, this calls the _calculate_current_rpm method with the passed speed.
        This sets the rpm state given the current gear

        Next, this checks if the current rpm is valid (above stall rpm and below redline).
        If the rpm is above the redline, then this function calls the upshift method

        This process repeats until a valid speed is reached, or the car redlines in top gear.
        :return:
        """

        self._calculate_current_rpm(speed)
        invalid_gear = self.rpm > self.redline
        while invalid_gear:
            self._upshift()
            self._calculate_current_rpm(speed)
            invalid_gear = self.rpm > self.redline

    def update_rpm(self, speed):
        """
        Updates the rpm and gearing given the cars speed

        :param speed: (float) the cars current speed in m/s
        :return: None
        """
        self._calculate_current_rpm(speed)
        if self.rpm > self.redline:
            self.rpm = self.redline
            raise ValueError('rpm from given speed over redline')
        pass


