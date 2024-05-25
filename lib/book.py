#!/usr/bin/env python3

class Book:
    def __init__(self, title, page):
      self.title = title
      self.page = page
    
    @property
    def page_count(self):
        """This is the page property"""
        return self._page
    
    @page_count.setter
    def page_count(self, page):
        if not isinstance(page, int):
            print("page_count must be an integer")
        else:
            self._page = page
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
        