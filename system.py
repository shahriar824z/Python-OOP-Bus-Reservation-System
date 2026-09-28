from models import Bus, Passenger

class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.fare = 500

    def show_fare(self):
        print(f'Ticket fare: ৳{self.fare}')

    def add_bus(self, number, route, seats):
        bus = Bus(number, route, seats)
        self.buses.append(bus)
        print(f'Bus {number} added successfully.')

    def book_ticket(self, bus_number, name, phone):
        found = False
        for bus in self.buses:
            if bus_number == bus.number:
                found = True
                if bus.book_seat(1):
                    self.show_fare()
                    passenger = Passenger(name, phone, bus)
                    self.passengers.append(passenger)
                break
        if not found:
            print(f'Bus {bus_number} not found.')

    def show_buses(self):
        print('---Our Current Buses---')
        for bus in self.buses:
            seat_word = "seats" if bus.available_seats() != 1 else "seat"
            print(f'Bus {bus.number}, {bus.route}, with {bus.available_seats()} available {seat_word}.')