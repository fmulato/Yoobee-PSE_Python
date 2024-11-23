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

import json
import os

class App_book():

    def __init__(self):
        if os.path.exists('book.json'):
            with open('book.json', 'r') as file:
                self.dic_book = json.load(file)
        else:
            self.dic_book = {}

        self.title = ''
        self.author = ''

    def input(self):
        self.user_input = input(f"=================\n"
                           f"Type an option:\n"
                           f"ADD title, author,\n"
                           f"REMOVE title\n"
                           f"SEARCH title\n"
                           f"EXIT\n"
                           f"-->").upper()

        if self.user_input.startswith('ADD') and \
            len(self.user_input.split(', ')) ==2 and \
            self.user_input[3] == ' ':
            self.add(self.user_input)

        elif self.user_input.startswith('REMOVE'):
            self.remove(self.user_input)

        elif self.user_input.startswith('SEARCH'):
            self.search(self.user_input)

        elif self.user_input.startswith('EXIT'):
            print("Goodbye")
            quit()

        else:
            print("Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author.")


    def add(self, user_input):

        title = self.user_input.split(', ')[0][4:].upper()
        author = self.user_input.split(', ')[1].upper()

        if title in self.dic_book.keys():
            print("Book already exist in the collection")
        else:
            self.dic_book[title] = author
        return self.dic_book

    def remove(self, user_input):
        title = self.user_input.split(', ')[0][7:].upper()
        if title not in self.dic_book.keys():
            print("Book doesn't exist in the collection")
        else:
            self.dic_book.pop(user_input[7:])
        return self.dic_book

    def search(self, user_input):
        title = self.user_input.split(', ')[0][7:].upper()
        if title not in self.dic_book.keys():
            print("Book not found")
        else:
            print(f"Book found: {title} by {self.dic_book[title]}")
        return self.dic_book

if __name__ == '__main__':

    ab = App_book()

    while True:
        ab.input()

    # Save into a JSON file
    with open('book.json', 'w') as file:
        json.dump(ab.dic_book, file, indent=4)

