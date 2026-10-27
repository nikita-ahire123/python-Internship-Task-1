def main():
    while True:
        print("\n===== CAB BOOKING CHATBOT =====")
        print("1. Book Ride")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "2":
            print("Thank you for using Cab Booking Chatbot!")
            break

        elif choice == "1":

            # Choose cab type
            print("\nChoose Cab Type:")
            print("1. Auto")
            print("2. Sedan")
            print("3. SUV")

            cab_choice = input("Enter cab choice: ")

            if cab_choice == "1":
                cab_type = "Auto"
                rate = 12
            elif cab_choice == "2":
                cab_type = "Sedan"
                rate = 18
            elif cab_choice == "3":
                cab_type = "SUV"
                rate = 25
            else:
                print("Invalid cab choice!")
                continue

            # Predefined routes
            print("\nChoose Route:")
            print("1. Pune Station to Shivajinagar (5 km)")
            print("2. Swargate to Kothrud (8 km)")
            print("3. Hinjawadi to Wakad (10 km)")

            route_choice = input("Enter route choice: ")

            if route_choice == "1":
                source = "Pune Station"
                destination = "Shivajinagar"
                distance = 5
            elif route_choice == "2":
                source = "Swargate"
                destination = "Kothrud"
                distance = 8
            elif route_choice == "3":
                source = "Hinjawadi"
                destination = "Wakad"
                distance = 10
            else:
                print("Invalid route choice!")
                continue

            # Calculate fare
            fare = distance * rate

            print("\n===== BOOKING DETAILS =====")
            print("Cab Type:", cab_type)
            print("Source:", source)
            print("Destination:", destination)
            print("Distance:", distance, "km")
            print("Rate per km: Rs.", rate)
            print("Total Fare: Rs.", fare)

            # Confirm before sharing OTP
            print("\n1. Confirm & Share OTP")
            print("2. Cancel Ride")

            confirm = input("Enter your choice: ")

            if confirm == "2":
                print("Ride cancelled successfully.")
                continue

            elif confirm == "1":
                import random
                otp = random.randint(1000, 9999)

                print("\nBooking Confirmed!")
                print("Your OTP is:", otp)
                print("OTP shared. Ride cancellation is now locked.")
            else:
                print("Invalid choice. Booking not confirmed.")

        else:
            print("Invalid menu choice! Please try again.")


if __name__ == "__main__":
    main()