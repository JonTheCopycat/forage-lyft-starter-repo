from car import Car

from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine

from battery import SpindlerBattery
from battery import NubbinBattery

class CarFactory:
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        return Car( CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date) )
    
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        return Car( WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date) )
        
    
    def create_palindrome(last_service_date, warning_light_on):
        return Car( SternmanEngine(warning_light_on), SpindlerBattery(last_service_date) )
    
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        return Car( WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date) )
        
    
    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        return Car( CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date) )