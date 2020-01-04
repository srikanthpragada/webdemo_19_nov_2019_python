import requests

id = input("Enter book id :")
resp = requests.delete(f"http://localhost:8000/catalog/rest/books/{id}")
if resp.status_code == 204:
    print("Book was deleted successfully!")
else:
    print("Sorry! Book not found!")
