import requests

title = input("Enter title :")
author = input("Enter author : ")
publisher = input("Enter publisher : ")
price = input("Enter price : ")
data = {'title': title, 'author': author, 'mobile': publisher,
        'price': price}

resp = requests.post("http://localhost:8000/catalog/rest/customers", data)
if resp.status_code == 200:
    print("Customer added successfully!")
else:
    print("Sorry! Could not add customer!")
