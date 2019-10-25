from fattmerchant.client import FMClient

fatt = FMClient(
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudCI6IjZlZWQ2YTQzLWZiYTMtNGFlYi04ZjUzLTk0ZGY4MWU4MmJlMyIsImdvZFVzZXIiOnRydWUsInN1YiI6ImEwMWE1Zjc0LWNiZGItNDcwNC05ZTliLTU2ZmQ1YThlZTdiOCIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODAwMC8vYXV0aGVudGljYXRlIiwiaWF0IjoxNTcxNzY5NjgzLCJleHAiOjE4ODcxMjk2ODMsIm5iZiI6MTU3MTc2OTY4MywianRpIjoiTEhzYUxCMHE2Y3hFb0pFRCJ9.A2IlJHmlMulYkq5Vsbn9y6J2OLWI4mIymlV2KrjVdiQ",
    "local"
)

# data = {
#     "company_name": "Fattmerchant HELLO",
#     "contact_name": "Fattmerchant 1111111",
#     "contact_email": "info2@fattmerchant.com",
#     "contact_phone": "8555503288",
#     "address_1": "25 Wall Street",
#     "address_2": "Suite 1",
#     "address_city": "Orlando",
#     "address_state": "FL",
#     "address_zip": "32801"
# }

# token, team = fatt.teams.create(data)

# print token
# print repr(team)

# transactions = fatt.transactions.list({"page": 2})

# transaction = fatt.transactions.get(transactions[0].id)

pm = fatt.paymentmethods.get('0001477e-6d77-421b-9c78-3596e56618bb')
print repr(pm)

# deposits = fatt.deposits.list({'start_date': '2017-01-01 18:05:23'})

    # print deposits

    # deposit = fatt.deposits.get(
    #     {
    #         'start_date': '2017-01-01 18:05:23',
    #         'end_date': '2019-12-01 18:05:23'
    #     }
    # )

    # print deposit

    # data = {"tax": 2, "subtotal": 10}
    # total = 1.00
    # pre_auth = False

    # transaction = fatt.charges.create(
    #     '01f2d919-b220-448d-b9bf-8dd628c818d6', data, total, pre_auth
    # )

    # print transaction

    # data = {
    #     "firstname": "Austin",
    #     "lastname": "Burns",
    #     "company": "Moo",
    #     "email": "a@a.com",
    # }

    # customer = fatt.customers.create(data)

    # print repr(customer)

    # customers = fatt.customers.list()

    # print(customers)

    # customer = fatt.customers.get(customers[0].id)

    # print(customer)

    # payment_methods = fatt.customers.payment_methods(customer.id)

    # print(payment_methods)
