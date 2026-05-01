from db_connection import db, cur

class Room:

    def add_room(self):
        room_type = input("Enter room type: ")
        price = float(input("Enter price: "))

        query = "INSERT INTO rooms (room_type, price) VALUES (%s, %s)"
        cur.execute(query, (room_type, price))
        db.commit()

        print("Room added successfully!")

    def view_rooms(self):
        cur.execute("SELECT * FROM rooms")
        for i in cur.fetchall():
            print(i)

    def available_rooms(self):
        cur.execute("SELECT * FROM rooms WHERE status='available'")
        for i in cur.fetchall():
            print(i)