import random

# Define the seat classes and their respective ranges
business_window = range(1, 6)
business_aisle = range(6, 11)
economy_window = range(11, 16)
economy_aisle = range(16, 21)

# Initialize the seat allocation data structure
seats = {seat: None for seat in range(1, 21)}

# Function to check if a seat is available
def is_seat_available(seat):
    return seats[seat] is None

# Function to assign the seat to the passenger
def assign_seat(seat, first_name, last_name):
    name = f"{first_name} {last_name}"
    seats[seat] = name

# shows confirmation that the seat has been booked to the passenger
def display_allocation(seat, seat_class, name):
    print("----------------------------------------------------")
    print("                      Success                       ")
    print("----------------------------------------------------")
    print(f"Seat {seat} ({seat_class}) has been allocated to {name}.")
    print("----------------------------------------------------")

# displays error screen if seat is already taken
def display_error():
    print("----------------------------------------------------")
    print("                      Error                         ")
    print("----------------------------------------------------")
    print("           Invalid seat selection. Please select     ")
    print("           an available seat from the options.       ")
    print("----------------------------------------------------")

# displays the seat map
def display_seat_map():
    print("----------------------------------------------------")
    print("                    Seat Map                        ")
    print("----------------------------------------------------")

    for seat in range(1, 21):
        seat_status = "Taken" if not is_seat_available(seat) else "Available"
        print(f"Seat {seat}: {seat_status}")

    print("----------------------------------------------------")

# displays the main menu with a welcome message
def display_menu():
    print("----------------------------------------------------")
    print("     Welcome to the Dio's Airline Seat Booking      ")
    print("                     System                         ")
    print("----------------------------------------------------")
    print("                    [1] Business Class Window        ")
    print("                    [2] Business Class Aisle         ")
    print("                    [3] Economy Class Window         ")
    print("                    [4] Economy Class Aisle          ")
    print("                    [5] Quick Book                   ")
    print("                    [6] Exit                         ")
    print("----------------------------------------------------")

    choice = input("Enter your choice (1-6): ")
    return choice

# displays confirmation screen
def display_confirmation(seat, seat_class, first_name, last_name):
    print("----------------------------------------------------")
    print("                Confirm Selected Seat?                ")
    print("----------------------------------------------------")
    print(f"Passenger: {first_name} {last_name}")
    print(f"Your allocated seat is: {seat} ({seat_class})")
    confirm = input("Please enter Y/N to accept this choice: ")
    return confirm.lower() == "y"

# idle screen for when it is not being used
def display_idle_screen():
    display_seat_map()
    print("     Welcome to the Dio's Airline Seat Booking      ")
    print("                     System                         ")
    print("                                                    ")
    print("     Please select an option to proceed.      ")
    print("----------------------------------------------------")

# Load seat allocations and passenger information from a text file
def load_seat_allocations():
    try:
        with open("seat_allocations.txt", "r") as file:
            for line in file:
                seat, name = line.strip().split(":")
                seats[int(seat)] = name
    except FileNotFoundError:
        # File doesn't exist, so no seat allocations yet
        pass

# Save seat allocations and passenger information to a text file
def save_seat_allocations():
    with open("seat_allocations.txt", "w") as file:
        for seat, name in seats.items():
            if name is not None:
                file.write(f"{seat}:{name}\n")

# Main loop
load_seat_allocations()

while True:
    display_idle_screen()
    input("Press any key to continue...")
    choice = display_menu()

    if choice == "1":
        seat = int(input("Enter seat number (1-5): "))
        if seat in business_window and is_seat_available(seat):
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if display_confirmation(seat, "Business Class Window", first_name, last_name):
                assign_seat(seat, first_name, last_name)
                display_allocation(seat, "Business Class Window", f"{first_name} {last_name}")
                save_seat_allocations()
            else:
                print("Seat selection canceled.")
        else:
            display_error()

    elif choice == "2":
        seat = int(input("Enter seat number (6-10): "))
        if seat in business_aisle and is_seat_available(seat):
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if display_confirmation(seat, "Business Class Aisle", first_name, last_name):
                assign_seat(seat, first_name, last_name)
                display_allocation(seat, "Business Class Aisle", f"{first_name} {last_name}")
                save_seat_allocations()
            else:
                print("Seat selection canceled.")
        else:
            display_error()

    elif choice == "3":
        seat = int(input("Enter seat number (11-15): "))
        if seat in economy_window and is_seat_available(seat):
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if display_confirmation(seat, "Economy Class Window", first_name, last_name):
                assign_seat(seat, first_name, last_name)
                display_allocation(seat, "Economy Class Window", f"{first_name} {last_name}")
                save_seat_allocations()
            else:
                print("Seat selection canceled.")
        else:
            display_error()

    elif choice == "4":
        seat = int(input("Enter seat number (16-20): "))
        if seat in economy_aisle and is_seat_available(seat):
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if display_confirmation(seat, "Economy Class Aisle", first_name, last_name):
                assign_seat(seat, first_name, last_name)
                display_allocation(seat, "Economy Class Aisle", f"{first_name} {last_name}")
                save_seat_allocations()
            else:
                print("Seat selection canceled.")
        else:
            display_error()

    elif choice == "5":
        available_seats = [seat for seat in seats if is_seat_available(seat)]
        if len(available_seats) > 0:
            seat = random.choice(available_seats)
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            seat_class = "Business Class" if seat <= 10 else "Economy Class"
            if seat in business_window or seat in economy_window:
                seat_class += " Window"
            else:
                seat_class += " Aisle"
            if display_confirmation(seat, seat_class, first_name, last_name):
                assign_seat(seat, first_name, last_name)
                display_allocation(seat, seat_class, f"{first_name} {last_name}")
                save_seat_allocations()
            else:
                print("Seat selection canceled.")
        else:
            print("No available seats.")

    elif choice == "6":
        print("Thank you for using Dio's Airline Seat Booking System.")
        break

    else:
        print("Invalid choice. Please select a valid option (1-6).")
