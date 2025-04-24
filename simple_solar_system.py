#simple_solar_system.py

from solarSystem import SolarSystem, Sun, Planet

solar_system = SolarSystem(width=1400, height=900)

sun = Sun(solar_system, mass=10_000)
planets = (
    Planet(
        solar_system,
        mass=1,
        position=(-350, 0),
        velocity=(0, 4),
    ),
    Planet(
        solar_system,
        mass=2,
        position=(-270, 0),
        velocity=(0, 7)
    ),
    Planet(
        solar_system,
        mass=3,
        position=(-500, 0),
        velocity=(0, 3)
    ),
)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()

sun.draw()

#temporary lines
import turtle
turtle.done()
