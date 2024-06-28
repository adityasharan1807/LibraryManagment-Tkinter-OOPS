import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime


# Initialize the database
def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        isbn TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        member_id INTEGER NOT NULL,
        issue_date TEXT NOT NULL,
        return_date TEXT,
        fine REAL,
        FOREIGN KEY(book_id) REFERENCES books(id),
        FOREIGN KEY(member_id) REFERENCES members(id)
    )
    ''')

    conn.commit()
    conn.close()


class LibraryApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()

        self.create_widgets()

    def create_widgets(self):
        # Book section
        self.book_frame = tk.LabelFrame(self.root,
                                        text="Books",
                                        padx=10,
                                        pady=10)
        self.book_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(self.book_frame, text="Title").grid(row=0, column=0)
        self.book_title = tk.Entry(self.book_frame)
        self.book_title.grid(row=0, column=1)

        tk.Label(self.book_frame, text="Author").grid(row=1, column=0)
        self.book_author = tk.Entry(self.book_frame)
        self.book_author.grid(row=1, column=1)

        tk.Label(self.book_frame, text="Year").grid(row=2, column=0)
        self.book_year = tk.Entry(self.book_frame)
        self.book_year.grid(row=2, column=1)

        tk.Label(self.book_frame, text="ISBN").grid(row=3, column=0)
        self.book_isbn = tk.Entry(self.book_frame)
        self.book_isbn.grid(row=3, column=1)

        self.add_book_button = tk.Button(self.book_frame,
                                         text="Add Book",
                                         command=self.add_book)
        self.add_book_button.grid(row=4, column=1)

        self.view_books_button = tk.Button(self.book_frame,
                                           text="View Books",
                                           command=self.view_books)
        self.view_books_button.grid(row=5, column=1)

        # Member section
        self.member_frame = tk.LabelFrame(self.root,
                                          text="Members",
                                          padx=10,
                                          pady=10)
        self.member_frame.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.member_frame, text="Name").grid(row=0, column=0)
        self.member_name = tk.Entry(self.member_frame)
        self.member_name.grid(row=0, column=1)

        tk.Label(self.member_frame, text="Email").grid(row=1, column=0)
        self.member_email = tk.Entry(self.member_frame)
        self.member_email.grid(row=1, column=1)

        self.add_member_button = tk.Button(self.member_frame,
                                           text="Add Member",
                                           command=self.add_member)
        self.add_member_button.grid(row=2, column=1)

        self.view_members_button = tk.Button(self.member_frame,
                                             text="View Members",
                                             command=self.view_members)
        self.view_members_button.grid(row=3, column=1)

        # Transaction section
        self.transaction_frame = tk.LabelFrame(self.root,
                                               text="Transactions",
                                               padx=10,
                                               pady=10)
        self.transaction_frame.grid(row=2, column=0, padx=10, pady=10)

        tk.Label(self.transaction_frame, text="Book ID").grid(row=0, column=0)
        self.transaction_book_id = tk.Entry(self.transaction_frame)
        self.transaction_book_id.grid(row=0, column=1)

        tk.Label(self.transaction_frame, text="Member ID").grid(row=1,
                                                                column=0)
        self.transaction_member_id = tk.Entry(self.transaction_frame)
        self.transaction_member_id.grid(row=1, column=1)

        tk.Label(self.transaction_frame,
                 text="Issue Date (YYYY-MM-DD)").grid(row=2, column=0)
        self.transaction_issue_date = tk.Entry(self.transaction_frame)
        self.transaction_issue_date.grid(row=2, column=1)

        self.add_transaction_button = tk.Button(self.transaction_frame,
                                                text="Issue Book",
                                                command=self.issue_book)
        self.add_transaction_button.grid(row=3, column=1)

        self.return_transaction_button = tk.Button(self.transaction_frame,
                                                   text="Return Book",
                                                   command=self.return_book)
        self.return_transaction_button.grid(row=4, column=1)

        self.fine_label = tk.Label(self.transaction_frame, text="Fine: $0.0")
        self.fine_label.grid(row=5, column=0, columnspan=2)

        self.view_transactions_button = tk.Button(
            self.transaction_frame,
            text="View Transactions",
            command=self.view_transactions)
        self.view_transactions_button.grid(row=6, column=1)

    def add_book(self):
        title = self.book_title.get()
        author = self.book_author.get()
        year = self.book_year.get()
        isbn = self.book_isbn.get()

        self.cursor.execute(
            'INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)',
            (title, author, year, isbn))
        self.conn.commit()
        messagebox.showinfo("Success", "Book added successfully!")

    def add_member(self):
        name = self.member_name.get()
        email = self.member_email.get()

        self.cursor.execute('INSERT INTO members (name, email) VALUES (?, ?)',
                            (name, email))
        self.conn.commit()
        messagebox.showinfo("Success", "Member added successfully!")

    def issue_book(self):
        book_id = self.transaction_book_id.get()
        member_id = self.transaction_member_id.get()
        issue_date = self.transaction_issue_date.get()

        self.cursor.execute(
            'INSERT INTO transactions (book_id, member_id, issue_date) VALUES (?, ?, ?)',
            (book_id, member_id, issue_date))
        self.conn.commit()
        messagebox.showinfo("Success", "Book issued successfully!")

    def return_book(self):
        book_id = self.transaction_book_id.get()
        member_id = self.transaction_member_id.get()
        return_date = self.transaction_issue_date.get(
        )  # reuse the field for return date

        self.cursor.execute(
            'UPDATE transactions SET return_date = ? WHERE book_id = ? AND member_id = ?',
            (return_date, book_id, member_id))
        self.conn.commit()

        fine = self.calculate_fine(book_id, member_id, return_date)
        self.fine_label.config(text=f"Fine: ${fine:.2f}")
        messagebox.showinfo("Success", "Book returned successfully!")

    def calculate_fine(self, book_id, member_id, return_date):
        self.cursor.execute(
            'SELECT issue_date FROM transactions WHERE book_id = ? AND member_id = ?',
            (book_id, member_id))
        issue_date = self.cursor.fetchone()[0]

        issue_date = datetime.datetime.strptime(issue_date, "%Y-%m-%d")
        return_date = datetime.datetime.strptime(return_date, "%Y-%m-%d")
        delta = return_date - issue_date

        fine_per_day = 1.0  # Example fine rate
        fine = max(0, (delta.days - 14) * fine_per_day)  # 2-week grace period

        self.cursor.execute(
            'UPDATE transactions SET fine = ? WHERE book_id = ? AND member_id = ?',
            (fine, book_id, member_id))
        self.conn.commit()

        return fine

    def view_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        self.show_data("Books", books)

    def view_members(self):
        self.cursor.execute("SELECT * FROM members")
        members = self.cursor.fetchall()
        self.show_data("Members", members)

    def view_transactions(self):
        self.cursor.execute("SELECT * FROM transactions")
        transactions = self.cursor.fetchall()
        self.show_data("Transactions", transactions)

    def show_data(self, title, data):
        view_window = tk.Toplevel(self.root)
        view_window.title(title)

        text = tk.Text(view_window)
        text.pack()

        for row in data:
            text.insert(tk.END, f"{row}\n")


if __name__ == "__main__":
    init_db()  # Ensure the database is initialized
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
