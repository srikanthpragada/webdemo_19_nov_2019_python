import requests

resp = requests.get("http://localhost:8000/catalog/rest/books")
if resp.status_code == 200:
    books = resp.json()
    for book in books:
         print(f"{book['id']} - {book['title']} - {book['author']}")
else:
    print("Sorry! Could not get details of books!")
