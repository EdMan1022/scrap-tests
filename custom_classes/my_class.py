

class Car(object):

    wheels = 4

    engine_power_unit = int
    engine_torque_unit = int
    braking_power_unit = int
    aerodynamic_resistance_unit = float
    mass_unit = float

    _speed_unit = float
    _mps_to_mph = 2.23694

    def __init__(self, engine_power: int, engine_torque: int, braking_power: int, mass: float,
                 current_speed=0., ):
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

        self.engine_power = engine_power
        self.engine_torque = engine_torque
        self.braking_power = braking_power
        self.current_speed = current_speed
        self.mass = mass

    def mph(self):
        """
        Display the current speed of the car in miles per hour

        :return: (float) current speed of the car converted to miles per hour
        """
        return self.current_speed * self._mps_to_mph

    def _current_acceleration(self):
        """
        Derives the current instantaneous acceleration of the car from its mass and power (over the next second)

        :return: (float) current acceleration in m/s^2
        """
        return self.engine_power

    def _accelerate(self):
        """
        Increases the speed of the car over the next second based on the cars engine_hp

        :return: None
        """


if __name__ == '__main__':
    viper = Car(engine_power=485, engine_torque=813, braking_power=600, current_speed=20.3, mass=1521.)

    print(viper.mph())

