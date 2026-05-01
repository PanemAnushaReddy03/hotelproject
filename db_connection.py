import mysql.connector

# ---------------- CONNECTION ---------------- #
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anusha@1234",
    database="hotel",
    use_pure=True
)

cur = db.cursor()
print("db connection-succesfully")
 

# Rooms Table
cur.execute("""
CREATE TABLE IF NOT EXISTS rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_type VARCHAR(20),
    price DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'available'
)
""")

# Customers Table
cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    phone VARCHAR(15)
)
""")

# Bookings Table
cur.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    room_id INT,
    customer_id INT,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

print("Tables created successfully!")