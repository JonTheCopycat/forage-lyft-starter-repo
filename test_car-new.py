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

#=======================================================================================================
class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = util.YearsFromToday(3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

#=======================================================================================================
class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = util.YearsFromToday(3)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(1)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        warning_light_is_on = True

        car = CarFactory.create_palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

#=======================================================================================================
class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = util.YearsFromToday(5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

#=======================================================================================================
class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = util.YearsFromToday(5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = util.YearsFromToday(0)
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()