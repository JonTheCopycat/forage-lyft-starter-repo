from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_palindrome(last_service_date, warning_light_on, tire_wear):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)
        
    
    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)
        return Car( CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date) )