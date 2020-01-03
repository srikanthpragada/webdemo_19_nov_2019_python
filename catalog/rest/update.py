import requests

id = input("Enter customer id :")
email = input("Enter customer email :")
resp = requests.put(f"http://localhost:8000/catalog/rest/customers/{id}",
                    {'email': email})
if resp.status_code == 200:
    print("Customer was updated successfully!")
elif resp.status_code == 404:
    print("Sorry! Customer not found!")
else:
    print("Sorry! Could not update customer due to error!")
