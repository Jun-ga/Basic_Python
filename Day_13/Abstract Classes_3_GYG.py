![13](https://user-images.githubusercontent.com/56713634/72675517-a8516c00-3ac8-11ea-9e03-0e03b61bc3a0.jpg)
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print('Title: ' + self.title)
        print('Author: ' + self.author)
        print('Price: ' + str(self.price))
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
