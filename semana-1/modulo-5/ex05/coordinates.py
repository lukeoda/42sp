class Coordinates:
    def __init__(self, lat: float, long: float):
        self.lat = lat
        self.long = long
    
    def __str__(self) -> str:
        return  f"Coordinates(lat={self.lat}, long={self.long})"

    def __eq__(self, other):
        if isinstance(other, Coordinates):
            return (self.lat == other.lat and
                    self.long == other.long)
        return False