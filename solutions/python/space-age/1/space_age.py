EARTH_YEAR_SECONDS = 31_557_600

ORBITAL_PERIODS = {
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "earth": 1.0,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
}

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        
    def _years_on(self, orbital_period):
        return round(self.seconds / (EARTH_YEAR_SECONDS * orbital_period), 2)        
        
    def on_mercury(self):
        return self._years_on(ORBITAL_PERIODS["mercury"])
        
    def on_earth(self):
        return self._years_on(ORBITAL_PERIODS["earth"])
        
    def on_venus(self):
        return self._years_on(ORBITAL_PERIODS["venus"])
        
    def on_mars(self):
        return self._years_on(ORBITAL_PERIODS["mars"])
        
    def on_jupiter(self):
        return self._years_on(ORBITAL_PERIODS["jupiter"])
        
    def on_saturn(self):
        return self._years_on(ORBITAL_PERIODS["saturn"])
        
    def on_uranus(self):
        return self._years_on(ORBITAL_PERIODS["uranus"])
        
    def on_neptune(self):
        return self._years_on(ORBITAL_PERIODS["neptune"])

