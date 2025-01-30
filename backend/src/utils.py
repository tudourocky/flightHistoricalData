from fast_flights import FlightData, Passengers, Result, get_flights

def load_flights(f_date, start, end, f_trip, f_seat, adult, child, infant, infants_lap):
    # fetch_mode = "fallback"
    # flight_data = FlightData(date=date, from_airport=start, to_airport=end)
    # passen = Passengers(adults=passengers, children=0, infants_in_seat=0, infants_on_lap=0)
    # result: Result = get_flights(flight_data, trip, seat, passen, fetch_mode)

    result: Result = get_flights(
        flight_data=[
            FlightData(date=f_date, from_airport=start, to_airport=end)
        ],
        trip=f_trip,
        seat=f_seat,
        passengers=Passengers(adults=int(adult), children=int(child), infants_in_seat=int(infant), infants_on_lap=int(infants_lap)),
        fetch_mode="fallback",
    )

    for flight in result:
        print(flight + "\n")

    return result