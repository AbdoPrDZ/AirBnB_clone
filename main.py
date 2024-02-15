#!/usr/bin/python3

from datetime import datetime

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

baseDict = {
    "id": "1",
    "created_at": datetime(2020, 1, 2, 5, 30, 1).isoformat(),
    "updated_at": datetime(2020, 1, 4, 4, 23, 12).isoformat(),
}

user1Dict = {
    "id": "1",
    "email": "abdopr47@gmail.com",
    "password": "123456",
    "first_name": "Abderrahmane",
    "last_name": "Guerguer",
    # "created_at": datetime(2023, 10, 10, 8, 43, 12).isoformat(),
    # "updated_at": datetime(2023, 10, 12, 3, 12, 10).isoformat(),
}

user2Dict = {
    "id": "2",
    "email": "abdopr47@gmail.com",
    "password": "123456",
    "first_name": "Abderrahmane",
    "last_name": "Guerguer",
    # "created_at": datetime(2023, 10, 10, 8, 43, 12).isoformat(),
    # "updated_at": datetime(2023, 10, 12, 3, 12, 10).isoformat(),
}

stateDict = {
    "id": "3",
    "name": "Alger",
    "created_at": datetime(2023, 10, 10, 8, 43, 12).isoformat(),
    "updated_at": datetime(2023, 10, 12, 3, 12, 10).isoformat(),
}

cityDict = {
    "id": "4",
    "state_id": "2",
    "name": "EL Hamiz",
    "created_at": datetime(2000, 9, 10, 8, 43, 12).isoformat(),
    "updated_at": datetime(2000, 9, 12, 3, 12, 10).isoformat(),
}

amenityDict = {
    "id": "5",
    "name": "Bathroom",
    "created_at": datetime(2021, 9, 10, 8, 43, 12).isoformat(),
    "updated_at": datetime(2021, 9, 12, 3, 12, 10).isoformat(),
}

placeDict = {
    "id": "6",
    "city_id": "4",
    "user_id": "1",
    "name": "Grate Dream Motel",
    "description": "Good motel with all required amenity",
    "number_rooms": 4,
    "number_bathroom": 5,
    "max_guest": 8,
    "price_by_night": 2000.0,
    "latitude": 97783.321,
    "longitude": 85675.765,
    "amenity_ids": ["5"],
    "created_at": datetime(2021, 9, 10, 8, 43, 12).isoformat(),
    "updated_at": datetime(2021, 9, 12, 3, 12, 10).isoformat(),
}

reviewDict = {
    "id": "7",
    "place_id": "6",
    "user_id": "2",
    "created_at": datetime(2021, 9, 10, 8, 43, 12).isoformat(),
    "updated_at": datetime(2021, 9, 12, 3, 12, 10).isoformat(),
}

# print(BaseModel(**baseDict))
user1 = User(**user1Dict)
user2 = User(**user2Dict)
# print(user1)
# print(State(**stateDict))
# print(City(**cityDict))
# print(Amenity(**amenityDict))
# print(Place(**placeDict))
# print(Review(**reviewDict))

storage = FileStorage()
storage.reload()

user1.save()
user2.save()

# storage.new(user)
# storage.save()

for item in storage.all().values():
    print(item)
