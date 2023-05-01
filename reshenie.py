import csv
import json

from DomashkaEduard.DZ2.files import BOOKS_FILE_PATH, USERS_FILE_PATH

users = []
with open(USERS_FILE_PATH) as f:
    users = json.load(f)

users_list = []
for u in users:
    users_list.append({
        'name': u['name'],
        'gender': u['gender'],
        'address': u['address'],
        'age': u['age'],
        'books': []
    })

books_list = []
with open(BOOKS_FILE_PATH) as f:
    rd = csv.DictReader(f)
    for b in rd:
        books_list.append(b)
print(books_list)


