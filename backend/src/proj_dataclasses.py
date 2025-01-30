from dataclasses import dataclass

@dataclass
class FlightInfo:
    arrival: str
    arrival_time_ahead: str
    delay: int
    departure: str
    duration: str
    is_best: bool
    price: int
    stops: int