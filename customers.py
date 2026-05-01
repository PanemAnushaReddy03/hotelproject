from db_connection import db, cur

class Customer:

    def add_customer(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        query = "INSERT INTO customers (name, phone) VALUES (%s, %s)"
        cur.execute(query, (name, phone))
        db.commit()

        print("Customer added!")

    def view_customers(self):
        cur.execute("SELECT * FROM customers")
        for i in cur.fetchall():
            print(i)