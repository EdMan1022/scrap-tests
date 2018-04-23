from custom_classes.transmissions import ManualTransmission
from custom_classes.my_class import ManualCar


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
