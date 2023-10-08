import unittest
from car import Car
from car_factory import CarFactory
import util

from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.battery import Battery
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = util.YearsFromToday(3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())




if __name__ == '__main__':
    unittest.main()