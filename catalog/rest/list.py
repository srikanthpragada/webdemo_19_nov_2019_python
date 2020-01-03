import requests

resp = requests.get("http://localhost:8000/catalog/rest/customers")
if resp.status_code == 200:
    customers = resp.json()
    for cust in customers:
         print(cust['id'], cust['name'], cust['email'])
else:
    print("Sorry! Could not get details of Customers!")
