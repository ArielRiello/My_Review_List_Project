# My_Review_List_Project

The "My Review List Project" is an entertainment manager application that allows users to record, rate, and make notes about Animes, Movies, and Series. With this app, you can keep a record of titles you have watched, assign personal ratings, and provide descriptions for each item.

### Key features

* Title Registration: 

The app lets you enter the names of Animes, Movies, and Series that you have watched or plan to watch.

* Personal Rating: 

You can assign personal ratings and scores to each title based on your own experience.

* Descriptive Notes: 

Provide detailed descriptions and notes about each item, including your impressions, favorite characters, or memorable moments.

* Easy Recommendation: 

Use the app to remember titles you would like to recommend to your friends, ensuring you are always ready to suggest a good movie or series.

* Quick Reference: 

Refer to your personal list to recall names of titles you have watched, view your ratings, and check whether they were good or bad before recommending them to someone.

The "My Review List Project" is a handy tool for personal organization, helping you keep track of your entertainment experiences and enhancing your recommendations to friends and family.

---

### Technologies

The "My Review List Project" utilizes several technologies to create a functional and user-friendly application for managing entertainment titles such as Animes, Movies, and Series. Here's an explanation of the technologies used:

* Python: 

Python is the core programming language used to develop the application. It's known for its simplicity and readability, making it a great choice for building desktop applications.

* Tkinter: 

Tkinter is a standard GUI (Graphical User Interface) library in Python that is used to create the application's user interface. It provides a range of widgets (buttons, labels, text entry, etc.) and is widely used for building desktop applications.

* SQLite Database: 

SQLite is a lightweight, serverless, and self-contained relational database engine. It's used to store and manage the data entered by users, such as titles, ratings, and descriptions. SQLite is well-suited for small to medium-sized applications.

* Datetime: 

The datetime module is a Python library used to work with dates and times. It's used in the application to record the date and time when a new entry is added or an existing entry is updated.

* Combobox and Radiobutton Widgets: 

Tkinter provides Combobox widgets for dropdown lists and Radiobutton widgets for selecting options. These widgets are used to create user-friendly interfaces for selecting categories, genres, and rating scores.

* Toplevel Windows: 

Toplevel windows are used to create pop-up dialog boxes for actions such as updating and deleting entries. These windows provide a separate space for user interaction without affecting the main application window.

* Event Handling: 

The application uses event handling to respond to user actions. For example, when the user selects a category in the Combobox, an event handler updates the list of available titles based on that category.

* Custom Functions: 

Custom functions are defined to perform actions such as saving data, updating records, and deleting entries. These functions encapsulate the logic required for these operations.

Overall, the "My Review List Project" is built using Python and Tkinter for the graphical user interface, SQLite for data storage, and other Python libraries for handling dates and events. This combination of technologies allows users to easily manage and review their entertainment choices.