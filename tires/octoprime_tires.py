from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        sum = 0.0
        for i in self.tire_wear:
            sum += i
            
        return sum >= 3.0