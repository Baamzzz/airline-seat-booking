# ✈️ Airline Seat Booking System

A command-line seat booking application for a 20-seat passenger aircraft, written in Python. Passengers can pick a specific seat by class and position, or let the system quick-book a random free seat. Bookings are saved to a text file, so they persist between runs.

> Built for the **Introduction to Programming** module (Foundation Year, Bournemouth University, 2022–23).

## Features

- **Four seat classes**: Business Window, Business Aisle, Economy Window, Economy Aisle
- **Choose your own seat** within a class, with availability checking
- **Quick Book**: automatically assigns a random available seat and tells you its class and position
- **Confirmation step** (Y/N) before a booking is finalised
- **Live seat map** showing which seats are taken or available
- **Persistent storage**: bookings are saved to `seat_allocations.txt` and reloaded on startup
- **Error handling** for taken seats, out-of-range seats and invalid menu choices

## Seat layout

| Seats  | Class          | Position |
|--------|----------------|----------|
| 1–5    | Business       | Window   |
| 6–10   | Business       | Aisle    |
| 11–15  | Economy        | Window   |
| 16–20  | Economy        | Aisle    |

## Getting started

Requires Python 3.6+ and uses only the standard library.

```bash
git clone https://github.com/<your-username>/airline-seat-booking.git
cd airline-seat-booking
python seat_booking.py
```

## Example

```
----------------------------------------------------
     Welcome to the Dio's Airline Seat Booking
                     System
----------------------------------------------------
                    [1] Business Class Window
                    [2] Business Class Aisle
                    [3] Economy Class Window
                    [4] Economy Class Aisle
                    [5] Quick Book
                    [6] Exit
----------------------------------------------------
Enter your choice (1-6): 5
Enter your first name: John
Enter your last name: Smith
----------------------------------------------------
                Confirm Selected Seat?
----------------------------------------------------
Passenger: John Smith
Your allocated seat is: 5 (Business Class Window)
Please enter Y/N to accept this choice: y
----------------------------------------------------
                      Success
----------------------------------------------------
Seat 5 (Business Class Window) has been allocated to John Smith.
----------------------------------------------------
```

## How it works

- Seats are stored in a **dictionary** mapping seat number → passenger name (`None` if free), so availability checks and bookings are O(1) lookups.
- Each seat class is defined as a `range`, which makes it easy to validate that a chosen seat belongs to the selected class.
- Each screen (menu, confirmation, success, error, seat map) is its own function, keeping the main loop readable.
- Bookings are written to a simple `seat:name` text file after every confirmed booking and read back in when the program starts.

## What I learned

- Using branching (`if`/`elif`/`else`) and loops to drive a menu-based program
- Breaking a program into small, reusable functions
- Choosing an appropriate data structure for the problem
- Reading from and writing to files for persistence
- Testing a program against a specification

## Possible improvements

- Validate numeric input so that typing a letter for a seat number doesn't crash the program
- Remove the repeated booking logic across menu options by moving it into one shared function
- Allow cancelling or changing an existing booking
- Add unit tests
