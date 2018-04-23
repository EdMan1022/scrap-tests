

class Car(object):

    wheels = 4

    engine_hp_unit = int
    engine_torque_unit = int
    braking_power_unit = int
    aerodynamic_resistance_unit = float

    _speed_unit = float

    def __init__(self, engine_hp: int, engine_torque: int, braking_power: int, current_speed=0.,):
        """
        Creates a specific car and specifies its base performance characteristics

        :param engine_hp: (int) Horsepower of the engine, used to accelerate the car
        :param engine_torque: (int) Torque of the engine, determines how much car can tow
        :param braking_power: (int) Braking power, determines how quickly car can stop
        :param current_speed: (float) The cars current speed, in meters per second
        """

        # Validate the types of the input parameters
        if type(engine_hp) is not self.engine_hp_unit:
            raise TypeError("Type of engine_hp is {}, needs to be {}".format(type(engine_hp),
                                                                             self.engine_hp_unit))
        if type(engine_torque) is not self.engine_torque_unit:
            raise TypeError("Type of engine_torque is {}, needs to be {}".format(type(engine_torque),
                                                                                 self.engine_torque_unit))
        if type(braking_power) is not self.braking_power_unit:
            raise TypeError("Type of braking_power is {}, needs to be {}".format(type(braking_power),
                                                                                 self.braking_power_unit))

        if type(current_speed) is not self._speed_unit:
            raise TypeError("Type of current_speed is {}, needs to be {}".format(type(current_speed),
                                                                                 self._speed_unit))

        self.engine_hp = engine_hp
        self.engine_torque = engine_torque
        self.braking_power = braking_power
        self.current_speed = current_speed

    def _accelerate(self):
        """
        Increases the speed of the car over the next second based on the cars engine_hp

        :return: None
        """


if __name__ == '__main__':
    viper = Car(engine_hp=600, engine_torque=650, braking_power=600, current_speed=40.0)


