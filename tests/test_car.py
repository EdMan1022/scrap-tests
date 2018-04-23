import unittest
from custom_classes.my_class import IdealCar
import nose


class TestIdealCar(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_invalid_speed(self):
        nose.tools.assert_raises(ValueError, IdealCar, engine_power=500, engine_torque=500, braking_power=600,
                                 mass=1500., current_speed=-1., simulation_tick=1.)

    def test_wrong_argument_types(self):
        nose.tools.assert_raises(TypeError, IdealCar, engine_power='500', engine_torque=500, braking_power=600,
                                 mass=1500., current_speed=1., simulation_tick=1.)
        nose.tools.assert_raises(TypeError, IdealCar, engine_power=500, engine_torque='500', braking_power=600,
                                 mass=1500., current_speed=1., simulation_tick=1.)
        nose.tools.assert_raises(TypeError, IdealCar, engine_power=500, engine_torque=500, braking_power='600',
                                 mass=1500., current_speed=1., simulation_tick=1.)
        nose.tools.assert_raises(TypeError, IdealCar, engine_power=500, engine_torque=500, braking_power=600,
                                 mass='1500.', current_speed=1., simulation_tick=1.)
        nose.tools.assert_raises(TypeError, IdealCar, engine_power=500, engine_torque=500, braking_power=600,
                                 mass=1500., current_speed='1.', simulation_tick=1.)
        nose.tools.assert_raises(TypeError, IdealCar, engine_power=500, engine_torque=500, braking_power=600,
                                 mass=1500., current_speed=1, simulation_tick=1.)
        nose.tools.assert_raises(TypeError, IdealCar, engine_power=500, engine_torque=500, braking_power=600,
                                 mass=1500., current_speed=1., simulation_tick='1.')

