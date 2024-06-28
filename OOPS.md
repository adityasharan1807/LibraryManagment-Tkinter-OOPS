Key OOPS concepts used:

1. ### Classes and Objects
* Class: A blueprint for creating objects. In this project, the LibraryApp class serves as the blueprint for the application.
* Object: An instance of a class. When we create an instance of LibraryApp, it initializes the Tkinter window and its components.


2. ### Encapsulation
 * Encapsulation involves bundling data and methods that operate on that data within one unit, such as a class.
 * The LibraryApp class encapsulates the data (attributes like self.book_title, self.member_name) and methods (like add_book, add_member) required for the application's functionality.
3. ### Abstraction
 * Abstraction involves hiding complex implementation details and showing only the essential features of the object.
 * The GUI components and database operations are abstracted into the methods of the LibraryApp class. Users interact with high-level methods like add_book without needing to know the underlying database queries.
 4. ### Inheritance
 * In this specific project, inheritance is not explicitly used. However, it could be implemented if we extend the functionality with more specific types of books, members, or specialized forms of transactions by inheriting from base classes.
 5. ### Polymorphism
 * Polymorphism allows methods to do different things based on the object it is acting upon. In this project, polymorphism is not explicitly demonstrated, but it could be used if we had different classes of users or books that overrode certain methods from their parent classes.
 Example: LibraryApp Class