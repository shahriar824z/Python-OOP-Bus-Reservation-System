# Bus Reservation System

A lightweight, object-oriented Python command-line application that models a real-time bus ticket booking platform. It features multi-role access (Admin and User) for managing bus fleets, verifying customer contact details, and booking seats.

## Features
- **Admin Management**: Secure login interface to register new bus routes, numbers, and total seat capacity.
- **Ticket Booking System**: Real-time seat allocation, passenger registration, and fare calculation.
- **Input Validation**: Phone number validation and seat boundary checks to prevent double booking.
- **Modular Structure**: Clean separation of models, system logic, and execution entry points.

## Project Structure

├── models.py      # Bus, Passenger, and Admin class definitions
├── system.py      # BusSystem core logic and state management
├── main.py        # Interactive CLI menu and entry point
└── README.md      # Documentation


## How to Run
```bash
python main.py
