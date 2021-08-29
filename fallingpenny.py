import numpy as np

from pint import UnitRegistry, Quantity
from typing import Union, Tuple, List


def quadratic_formula(
        a: Union[float, int, Quantity],
        b: Union[float, int, Quantity],
        c: Union[float, int, Quantity]
) -> Tuple[Union[float, int, Quantity, None], Union[float, int, Quantity, None]]:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b - np.sqrt(delta))/(2 * a)
        x2 = (-b + np.sqrt(delta))/(2 * a)
    elif delta == 0:
        x1 = -b / 2 * a
        x2 = x1
    else:
        x1 = None
        x2 = None
    return x1, x2

def velocity(
        acceleration: Union[float, int, Quantity],
        time: Union[float, int, Quantity]
) -> Union[float, int, Quantity]:
    return acceleration * time

def distance(
        velocity: Union[float, int, Quantity],
        acceleration: Union[float, int, Quantity],
        time: Union[float, int, Quantity]
) -> Union[float, int, Quantity]:
    return acceleration * time ** 2 / 2 + velocity * time

def time(
        distance: Union[float, int, Quantity],
        acceleration: Union[float, int, Quantity, None] = None,
        velocity: Union[float, int, Quantity, None] = None
) -> Union[float, int, Quantity, List, None]:
    if velocity is None:
        return np.sqrt(2 * distance / acceleration)
    elif acceleration is None:
        return distance / velocity
    else:
        x1, x2 = quadratic_formula(acceleration / 2, velocity, (-1) * distance)
        positive = [x for x in (x1, x2) if x >= 0] or None
        return positive

def drag_force(density_of_fluid, velocity, area, drag_coefficient):
    return 1 / 2 * density_of_fluid * (velocity ** 2) * area * drag_coefficient

def force(mass, acceleration):
    return mass * acceleration


''' case 1: falling penny '''
gravitational_acceleration = 9.81
drop_time = 3.4

velocity_on_impact = velocity(acceleration=gravitational_acceleration, time=drop_time)
distance_to_impact = distance(velocity=0, acceleration=gravitational_acceleration, time=drop_time)


''' case 2: penny falling from the Empire State Building '''
gravitational_acceleration = 9.81
drop_distance = 381

time_to_impact = time(acceleration=gravitational_acceleration, distance=drop_distance)


''' case 3: introducing units to calculations '''
units = UnitRegistry()
meter = units.meter
second = units.second
foot = units.foot

gravitational_acceleration = 9.81 * meter * second ** 2
gravitational_acceleration_value = gravitational_acceleration.magnitude
gravitational_acceleration_unit = gravitational_acceleration.units

drop_time = 3.4 * second
drop_time_value = drop_time.magnitude
drop_time_unit = drop_time.units

velocity_on_impact = velocity(acceleration=gravitational_acceleration, time=drop_time)


''' case 4: throw at terminal velocity '''
drop_terminal_velocity = 29 * meter / second
drop_distance = 381 * meter

drop_time = time(velocity=drop_terminal_velocity, distance=drop_distance)


''' case 4: drag force'''
kilogram = units.kilogram
gravitational_acceleration = 9.81 * meter * second ** 2
air_density = 1.204 * kilogram / (meter ** 3)
penny_mass = 0.00356 * kilogram
penny_velocity = 5 * meter / second
penny_radius = 0.0203 * meter
penny_area = penny_radius ** 2 * np.pi
penny_drag_coeff = 1.15

penny_drag_force = drag_force(
    density_of_fluid=air_density,
    velocity=penny_velocity,
    area=penny_area,
    drag_coefficient=penny_drag_coeff
)

penny_gravitational_force = force(mass=penny_mass, acceleration=gravitational_acceleration)