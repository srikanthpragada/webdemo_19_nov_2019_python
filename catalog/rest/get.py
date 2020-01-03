import requests

id = input("Enter customer id :")
resp = requests.get(f"http://localhost:8000/catalog/rest/customers/{id}")
if resp.status_code == 200:
    cust = resp.json()
    print(cust['name'], cust['email'])
else:
    print("Sorry! Customer not found!")
