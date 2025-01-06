import datetime

class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.date_purchased = None
        self.depreciation_function = None
    
class Room:

    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def calculate_depreciation(self, date):
        for item in self.items:
            item.date_purchased = date
            item.depreciation_function = lambda x: x * 0.9

class House:

    def __init__(self, name):
        self.name = name
        self.rooms = []
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def remove_room(self, room):
        self.rooms.remove(room)
    
    def calculate_depreciation(self, date):
        for room in self.rooms:
            room.calculate_depreciation(date)

class StorageLocation:

    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def calculate_depreciation(self, date):
        for item in self.items:
            item.date_purchased = date
            item.depreciation_function = lambda x: x * 0.8


