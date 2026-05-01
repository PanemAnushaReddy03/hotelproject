from db_connection import db, cur
from datetime import datetime

class Booking:

    def book_room(self):
        room_id = int(input("Enter room id: "))
        customer_id = int(input("Enter customer id: "))
        check_in = input("Enter check-in date (YYYY-MM-DD): ")

        cur.execute("SELECT status FROM rooms WHERE room_id=%s", (room_id,))
        data = cur.fetchone()

        if data and data[0] == "available":
            cur.execute(
                "INSERT INTO bookings (room_id, customer_id, check_in) VALUES (%s,%s,%s)",
                (room_id, customer_id, check_in)
            )

            cur.execute("UPDATE rooms SET status='booked' WHERE room_id=%s", (room_id,))
            db.commit()

            print("Room booked successfully!")
        else:
            print("Room not available!")

    def checkout(self):
        booking_id = int(input("Enter booking id: "))
        checkout = input("Enter checkout date (YYYY-MM-DD): ")

        cur.execute("SELECT room_id, check_in FROM bookings WHERE booking_id=%s", (booking_id,))
        data = cur.fetchone()

        if data:
            room_id, check_in = data

            cur.execute("SELECT price FROM rooms WHERE room_id=%s", (room_id,))
            price = cur.fetchone()[0]

            d1 = datetime.strptime(str(check_in), "%Y-%m-%d")
            d2 = datetime.strptime(checkout, "%Y-%m-%d")

            days = (d2 - d1).days
            bill = days * price

            cur.execute("UPDATE rooms SET status='available' WHERE room_id=%s", (room_id,))
            cur.execute("UPDATE bookings SET check_out=%s WHERE booking_id=%s",
                        (checkout, booking_id))

            db.commit()

            print("Total bill:", bill)
        else:
            print("Invalid booking!")

    def cancel_booking(self):
        booking_id = int(input("Enter booking id: "))

        cur.execute("SELECT room_id FROM bookings WHERE booking_id=%s", (booking_id,))
        data = cur.fetchone()

        if data:
            room_id = data[0]

            cur.execute("DELETE FROM bookings WHERE booking_id=%s", (booking_id,))
            cur.execute("UPDATE rooms SET status='available' WHERE room_id=%s", (room_id,))
            db.commit()

            print("Booking cancelled!")
        else:
            print("Booking not found!")