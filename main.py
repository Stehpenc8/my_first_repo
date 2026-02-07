class Vehicle:
    def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color 
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = True 

    def start_engine(self):
        if self.engine_on == False and self.reserve > 0:
            self.engine_on = True 
            return 'Engine on'
        return 'Error, engine cant be launched because engine is already started or fuel supply is empty'
    
    def stop_engine(self):
        if self.engine_on == True:
            self.engine_on = False 
            return 'Engine off'
        return 'Error, engine has already turned off'
    
    def drive(self, distance):
        if self.engine_on == False:
            return 'Car cant drive because engine off'
        if self.reserve / self.consumption * 100 < distance:
            return 'Low fuel level'
        self.mileage -= distance
        self.reserve -= distance / self.consumption * 100 
        return f'The car passed {distance} km. Fuel reserve {self.reserve} l.'
    
    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return f'Cars mileage {self.mileage}km.'
    
    def get_reserve(self):
        return f'Fuel reserve: {self.reserve}l.'
    