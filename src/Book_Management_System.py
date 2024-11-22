# UNDER CONSTRUCTION !!!!!

'''
Objective: Write a program to help users manage their personal book collection. The program should
allow the user to add, remove, and search for books.
Requirements :
•User Input: The user will input commands like "ADD title, author", "REMOVE title", or "SEARCH
title".
•Book List: The program should maintain a list of books, where each book is represented by a dictionary
containing the book's title and author.
•Adding Books: When adding a book, the program should check to see if the book already exists in the
collection.
•Removing Books: When removing a book, the program should verify that the book is in the list.
•Searching for Books: When searching for a book, if found, the program should display "Book found:
title by author". If the book is not found, it should display "Book not found".
•Error Handling: If the user enters an incorrect command format, the program should prompt them with
"Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author."
'''

class App_book():

    def __init__(self):
        self.dic_book = {}

    def input(self):
        user_input = input(f"Type an option:\n"
                           f"ADD title, author,\n"
                           f"REMOVE title\n"
                           f"SEARCH title\n")

        if user_input.startswith('ADD'):
            self.title = user_input.split(', ')[0][4:]
            self.author = user_input.split(', ')[1]
            self.dic_book[self.title] = self.author
            return self.dic_book
        if user_input.startswith('REMOVE'):
            pass
        if user_input.startswith('SEARCH'):
            pass

        print(self.list_book)

    def add(self):
        pass

    def remove(self):
        pass

    def search(self):
        pass

if __name__ == '__main__':
    ab = App_book()
    ab.input()
    print(ab.dic_book)

