from room import Room
from customers import Customer
from booking import Booking

r = Room()
c = Customer()
b = Booking()

while True:
    print("1.Add Room")
    print("2.View Rooms")
    print("3.Available Rooms")
    print("4.Add Customer")
    print("5.View Customers")
    print("6.Book Room")
    print("7.Checkout")
    print("8.Cancel Booking")
    print("9.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        r.add_room()
    elif ch == "2":
        r.view_rooms()
    elif ch == "3":
        r.available_rooms()
    elif ch == "4":
        c.add_customer()
    elif ch == "5":
        c.view_customers()
    elif ch == "6":
        b.book_room()
    elif ch == "7":
        b.checkout()
    elif ch == "8":
        b.cancel_booking()
    elif ch == "9":
        print("Thank you!")
        break
    else:
        print("Invalid choice")