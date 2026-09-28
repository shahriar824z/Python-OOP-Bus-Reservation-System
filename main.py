from models import Admin
from system import BusSystem

def main():
    system = BusSystem()
    admin = Admin('admin', '1234')

    system.add_bus("B1010AC", "Dhaka to Rajshahi", 25)

    while True:
        print('\n---//-User-Menu-//---')
        print('1. Admin Login\n2. Book Ticket\n3. View Buses\n4. Exit')

        choice = input('Enter your choice: ').strip()

        if choice == '1':
            username = input('Enter your username: ').strip()
            password = input('Enter your password: ').strip()
            
            if admin.login(username, password):
                while True:
                    print('\n---//-Admin-Menu-//---')
                    print('1. Add Bus\n2. View All Buses\n3. Logout')

                    admin_choice = input('Enter your choice: ').strip()

                    if admin_choice == '1':
                        number = input('Enter bus number: ').strip()
                        route = input('Enter route (e.g., Dhaka to Rajshahi): ').strip()
                        if not number or not route:
                            print('Invalid input.\nBus number and route cannot be empty.')
                        elif any(bus.number == number for bus in system.buses):
                            print(f'Bus {number} already exists.')
                        else:
                            try:
                                seats = int(input('Enter total number of seats: '))
                                if seats > 0:
                                    system.add_bus(number, route, seats)
                                else:
                                    print('Invalid input.\nNumber of seats must be positive.')
                            except ValueError:
                                print('Invalid input.\nPlease enter a whole number for seats.')

                    elif admin_choice == '2':
                        system.show_buses()

                    elif admin_choice == '3':
                        print('Logged out successfully.')
                        break

                    else:
                        print('Invalid input.\nPlease enter a number between 1 and 3.')

        elif choice == '2':
            bus_number = input('Enter bus number: ').strip()
            name = input('Enter your name: ').strip()
            phone = input('Enter your phone number: ').strip()

            if phone.isdigit() or (phone.startswith('+') and phone[1:].isdigit()):
                system.book_ticket(bus_number, name, phone)
            else:
                print('Enter a valid Phone number.')

        elif choice == '3':
            system.show_buses()

        elif choice == '4':
            print('Exiting system...')
            break

        else:
            print('Invalid input.\nPlease enter a number between 1 and 4.')

if __name__ == '__main__':
    main()