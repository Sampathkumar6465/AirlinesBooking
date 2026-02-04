class AirlineReservation:
    def __init__(self):
        self.flights = {
            "AI101": 5,
            "AI202": 3,
            "AI303": 2
        }
        self.passengers = []

    def show_flights(self):
        print("\nAvailable Flights:")
        for flight, seats in self.flights.items():
            print(f"Flight: {flight} | Seats Available: {seats}")

    def book_ticket(self, name, flight):
        if flight in self.flights:
            if self.flights[flight] > 0:
                self.passengers.append((name, flight))
                self.flights[flight] -= 1
                print(f"\nTicket booked successfully for {name} on {flight}")
            else:
                print("\nNo seats available")
        else:
            print("\nInvalid flight number")

    def cancel_ticket(self, name):
        for passenger in self.passengers:
            if passenger[0] == name:
                self.passengers.remove(passenger)
                self.flights[passenger[1]] += 1
                print(f"\nTicket cancelled for {name}")
                return
        print("\nPassenger not found")

    def show_passengers(self):
        print("\nPassenger List:")
        if not self.passengers:
            print("No passengers")
        for p in self.passengers:
            print(f"Name: {p[0]} | Flight: {p[1]}")


# -------- Main Program --------
airline = AirlineReservation()

while True:
    print("\n✈️ Airline Reservation System")
    print("1. Show Flights")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Show Passengers")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        airline.show_flights()

    elif choice == 2:
        name = input("Enter passenger name: ")
        flight = input("Enter flight number: ")
        airline.book_ticket(name, flight)

    elif choice == 3:
        name = input("Enter passenger name to cancel: ")
        airline.cancel_ticket(name)

    elif choice == 4:
        airline.show_passengers()

    elif choice == 5:
        print("Thank you for using Airline Reservation System ✨")
        break

    else:
        print("Invalid choice")
