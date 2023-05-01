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
        book = {
            'title': b['Title'],
            'author': b['Author'],
            'pages': int(b['Pages']),
            'genre': b['Genre']
        }
        books_list.append(book)

num_users = len(users_list)
num_books = len(books_list)

max_books_per_user = num_books // num_users
remaining_books = num_books % num_users

book_index = 0
for i, user in enumerate(users_list):
    for j in range(max_books_per_user):
        user['books'].append(books_list[book_index])
        book_index += 1
    if i < remaining_books:
        user['books'].append(books_list[book_index])
        book_index += 1

with open('result.json', 'w') as f:
    json.dump(users_list, f, indent=4)
