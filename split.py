import json

with open('bill.json', 'r') as f:
    data = f.read()

order = json.loads(data)
for item in order["items"]:
    print(f"{item['qty']:>3}   ${item['price']:>6.2f}   {item['item']}")