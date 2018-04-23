import math

from custom_classes.transmissions import ManualTransmission


class IdealCar(object):

    wheels = 4

    engine_power_unit = int
    engine_torque_unit = int
    braking_power_unit = int
    aerodynamic_resistance_unit = float
    mass_unit = float
    simulation_unit = float

    _speed_unit = float
    _mps_to_mph = 2.23694
    _noise_interval = 40

    def __init__(self, engine_power: int, engine_torque: int, braking_power: int, mass: float,
                 current_speed=0., simulation_tick=1.):
        """
        Creates a specific car and specifies its base performance characteristics

        :param engine_power: (int) Power of the engine (in Kilowatts), used to accelerate the car
        :param engine_torque: (int) Torque of the engine (in Newton-Meters), determines how much car can tow
        :param braking_power: (int) Braking power (in horsepower), determines how quickly car can stop
        :param mass: (float) Mass of the car, in kilograms
        :param current_speed: (float) The cars current speed, in meters per second
        """

        # Validate the types of the input parameters
        if type(engine_power) is not self.engine_power_unit:
            raise TypeError("Type of engine_power is {}, needs to be {}".format(type(engine_power),
                                                                                self.engine_power_unit))
        if type(engine_torque) is not self.engine_torque_unit:
            raise TypeError("Type of engine_torque is {}, needs to be {}".format(type(engine_torque),
                                                                                 self.engine_torque_unit))
        if type(braking_power) is not self.braking_power_unit:
            raise TypeError("Type of braking_power is {}, needs to be {}".format(type(braking_power),
                                                                                 self.braking_power_unit))
        if type(current_speed) is not self._speed_unit:
            raise TypeError("Type of current_speed is {}, needs to be {}".format(type(current_speed),
                                                                                 self._speed_unit))
        if type(mass) is not self.mass_unit:
            raise TypeError("Type of mass is {}, needs to be {}".format(type(mass),
                                                                        self.mass_unit))
        if type(simulation_tick) is not self.simulation_unit:
            raise TypeError("Type of simulation tick is {}, needs to be {}".format(type(simulation_tick),
                                                                                   self.simulation_unit))

        self.engine_power = engine_power
        self.engine_torque = engine_torque
        self.braking_power = braking_power
        self.current_speed = current_speed
        self.mass = mass
        self.simulation_tick = simulation_tick
        self._current_time = 0.
        self._current_ke = .5 * self.mass * self.current_speed ** 2.

    def _speed(self):
        """
        Derives the current speed of the car from it's Kinetic energy

        :return: (float) current speed in meters/second
        """
        return ((2 * self._current_ke) / self.mass) ** .5

    def ms(self):
        return self._speed()

    def mph(self):
        """
        Display the current speed of the car in miles per hour

        :return: (float) current speed of the car converted to miles per hour
        """
        return self._speed() * self._mps_to_mph

    def _accelerate(self):
        """
        Increases the speed of the car over the next simulation time step based on the cars engine_power

        :return: None
        """
        self._current_ke += self.engine_power * self.simulation_tick

    def _engine_noise(self):
        print('vrrrrrrrmmmmm')

    def accelerate_for_time(self, time):
        """
        Accelerates the car for the entered time

        :param time: (int, float) Time car will accelerate for in seconds
        :return: None
        """
        number_of_acceleration_steps = int(math.floor(time / self.simulation_tick))
        for i in range(number_of_acceleration_steps):
            self._accelerate()

            if i % self._noise_interval == 0:
                self._engine_noise()


class ManualCar(IdealCar):
    """
    Introduces logic to handle a cars power output given its current RPM and gearing

    """

    rpm_unit = float
    _tach_scale = 10.

    def __init__(self, engine_power: int, engine_torque: int, braking_power: int, mass: float,
                 transmission: ManualTransmission, current_speed=0., simulation_tick=1.):
        """
        Adds the transmission to the parent init function
        """

        super(ManualCar, self).__init__(engine_power, engine_torque, braking_power, mass, current_speed,
                                        simulation_tick)

        self.transmission = transmission

    def _set_speed(self, speed):
        """
        Sets the car's kinetic energy from a given external speed

        :param speed:
        :return:
        """
        self._current_ke = .5 * self.mass * speed ** 2.

    def _accelerate(self):
        """
        Adds a transmission validation check to the accelerate step

        If the transmission is above the redline, return the engine speed to the redline
        and return the car's road speed to the speed derived from redline
        :return: None
        """
        super(ManualCar, self)._accelerate()
        try:
            self.transmission.update_rpm(self._speed())
        except ValueError:
            self._set_speed(self.transmission.speed_from_transmission())

    def _engine_noise(self):

        if self.transmission.rpm == self.transmission.redline:
            print('SCRREEEEEEE')
        else:
            print('|' * int((self.transmission.rpm / self.transmission.redline) * self._tach_scale))


if __name__ == '__main__':

    current_speed = 0.

    gears_data = {
        1: 2.26,
        2: 1.58,
        3: 1.19,
        4: 1.00,
        5: 0.77,
        6: 0.63,
    }
    transmission = ManualTransmission(gear_data=gears_data, final_drive_ratio=3.55, wheel_radius=.2413,
                                      redline=6150., speed=current_speed)

    viper = ManualCar(engine_power=485000, engine_torque=813, braking_power=600, current_speed=current_speed,
                      mass=1521., simulation_tick=.001, transmission=transmission)

    viper.accelerate_for_time(.25)

    viper.transmission.manual_shift(2)

    viper.accelerate_for_time(1.)

    viper.transmission.manual_shift(3)

    viper.accelerate_for_time(1.)

    print(viper.mph())

