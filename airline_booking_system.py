class Flight:
    def __init__(self, flight_id, source, destination, seats, fare):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare


class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Booking:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight

    def book_ticket(self):
        if self.flight.seats > 0:
            self.flight.seats -= 1
            print("\n Ticket Booked Successfully")
            print("Passenger Name :", self.passenger.name)
            print("Passenger Age  :", self.passenger.age)
            print("Flight ID      :", self.flight.flight_id)
            print("Route          :", self.flight.source, "->", self.flight.destination)
            print("Fare           :", self.flight.fare)
            print("Seats Left     :", self.flight.seats)
        else:
            print("\n No seats available")


# --------- Main Program ---------

# Flight objects
flight1 = Flight(101, "Chennai", "Delhi", 2, 5500)
flight2 = Flight(102, "Bangalore", "Mumbai", 1, 4500)
flight3 = Flight(103, "Hyderabad", "Kolkata", 5, 6000)
# Passenger input
name = input("Enter Passenger Name: ")
age = int(input("Enter Passenger Age: "))

# Show flights
print("\nAvailable Flights")
print("1.", flight1.flight_id, flight1.source, "->", flight1.destination,
      "Seats:", flight1.seats, "Fare:", flight1.fare)
print("2.", flight2.flight_id, flight2.source, "->", flight2.destination,
      "Seats:", flight2.seats, "Fare:", flight2.fare)
print("3.", flight3.flight_id, flight3.source, "->", flight3.destination,
      "Seats:", flight3.seats, "Fare:", flight3.fare)

# Choose flight
fid = int(input("\nEnter Flight ID to book: "))

# Passenger object
passenger = Passenger(name, age)

# Booking
if fid == flight1.flight_id:
    booking = Booking(passenger, flight1)
    booking.book_ticket()
elif fid == flight2.flight_id:
    booking = Booking(passenger, flight2)
    booking.book_ticket()
else:
    print("\n Invalid Flight ID")
