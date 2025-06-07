import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Step 1: Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Authors (
    AuthorID TEXT PRIMARY KEY,
    Name TEXT,
    Country TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    BookID TEXT PRIMARY KEY,
    Title TEXT,
    Genre TEXT,
    PublishedYear INTEGER,
    AuthorID TEXT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Members (
    MemberID TEXT PRIMARY KEY,
    Name TEXT,
    Email TEXT,
    JoinDate TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Staff (
    StaffID TEXT PRIMARY KEY,
    Name TEXT,
    Role TEXT,
    Email TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Loans (
    LoanID TEXT PRIMARY KEY,
    MemberID TEXT,
    BookID TEXT,
    LoanDate TEXT,
    ReturnDate TEXT,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);
""")

print("✅ Tables created successfully.")


# Step 2: Insert Sample Data

# Authors
cursor.executemany("INSERT OR IGNORE INTO Authors VALUES (?, ?, ?);", [
    ("A001", "Chinua Achebe", "Nigeria"),
    ("A002", "J.K. Rowling", "UK"),
    ("A003", "Yuval Noah Harari", "Israel"),
    ("A004", "Dan Brown", "USA"),
    ("A005", "Chimamanda Ngozi Adichie", "Nigeria")
])

# Books
cursor.executemany("INSERT OR IGNORE INTO Books VALUES (?, ?, ?, ?, ?);", [
    ("B001", "Things Fall Apart", "Fiction", 1958, "A001"),
    ("B002", "Harry Potter", "Fantasy", 1997, "A002"),
    ("B003", "Sapiens", "History", 2011, "A003"),
    ("B004", "The Da Vinci Code", "Thriller", 2003, "A004"),
    ("B005", "Purple Hibiscus", "Drama", 2003, "A005")
])

# Members
cursor.executemany("INSERT OR IGNORE INTO Members VALUES (?, ?, ?, ?);", [
    ("M001", "Aisha Jallow", "aisha@example.com", "2023-01-10"),
    ("M002", "Baba Toure", "baba@example.com", "2023-02-15"),
    ("M003", "Fatima Conteh", "fatima@example.com", "2023-03-01"),
    ("M004", "Ousman Drammeh", "ousman@example.com", "2023-03-20"),
    ("M005", "Mariama Sowe", "mariama@example.com", "2023-04-05")
])

# Staff
cursor.executemany("INSERT OR IGNORE INTO Staff VALUES (?, ?, ?, ?);", [
    ("S001", "Admin One", "admin", "admin@example.com"),
    ("S002", "Librarian Musa", "librarian", "musa@example.com"),
    ("S003", "Librarian Awa", "librarian", "awa@example.com"),
    ("S004", "Receptionist Halima", "receptionist", "halima@example.com"),
    ("S005", "Security Bayo", "security", "bayo@example.com")
])

# Loans
cursor.executemany("INSERT OR IGNORE INTO Loans VALUES (?, ?, ?, ?, ?);", [
    ("L001", "M001", "B001", "2023-05-01", "2023-05-15"),
    ("L002", "M002", "B003", "2023-05-03", "2023-05-17"),
    ("L003", "M003", "B002", "2023-05-05", "2023-05-19"),
    ("L004", "M004", "B005", "2023-05-07", "2023-05-21"),
    ("L005", "M005", "B004", "2023-05-09", "2023-05-23")
])

print("✅ Sample data inserted.")



# Update a member's email
cursor.execute("""
UPDATE Members
SET Email = 'fatima.updated@example.com'
WHERE MemberID = 'M003';
""")
print("✅ Member email updated.")

# Replace a book record (same BookID)
cursor.execute("""
INSERT OR REPLACE INTO Books (BookID, Title, Genre, PublishedYear, AuthorID)
VALUES ('B003', 'Sapiens: Updated Edition', 'History', 2015, 'A003');
""")
print("✅ Book replaced.")


# Truncate the Staff table (delete all staff)
cursor.execute("DELETE FROM Staff;")
print("✅ Staff table truncated.")


conn.commit()
conn.close()
