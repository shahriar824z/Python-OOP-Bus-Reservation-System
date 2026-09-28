class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self, number):
        if 0 < number <= self.available_seats():
            self.booked_seats += number
            print(f'{number} seat has booked for you.')
            return True
        elif number > self.available_seats():
            print(f'There is only {self.available_seats()} seats available.')
            return False
        else:
            print('The number of seats you want to book must be positive.')
            return False


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print('Admin access granted.')
            return True
        elif username != self.username and password == self.password:
            print('Invalid username.')
        elif username == self.username and password != self.password:
            print('Wrong password.')
        else:
            print('Invalid username and password.')
        return False