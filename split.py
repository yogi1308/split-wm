import json
class Roommate:
    def __init__(self, name, shortname):
        self.name = name
        self.shortname = shortname
        self.items = []
        self.total = 0.00

    def __str__(self):
        return_str = f"{self.name}\n"
        for item in self.items:
            return_str += f"${item[0]:<10} {item[1]}\n"
        return_str += f"{self.total}\n"
        return return_str

shreetej = Roommate(name="shreetej", shortname="sh")
shubham = Roommate(name="shubham", shortname="ss")
ishaan = Roommate(name="ishaan", shortname="ia")
vaibhav = Roommate(name="vaibhav", shortname="vr")

roommates = [shreetej, shubham, ishaan, vaibhav]

with open('bill.json', 'r') as f:
    data = f.read()

order = json.loads(data)

print()
for item in order["items"]:
    print(f"QTY: {item['qty']}   PRICE: ${item['price']}   ITEM: {item['item']}")
    for i in range(item["qty"]):
        whose = input(f"{i}/{item["qty"]}: ").lower()
        while whose not in [r.shortname for r in roommates]:
            print("Invalid input  [", whose, "]  can only be - ", [r.shortname for r in roommates])
            whose = input(f"{i}/{item["qty"]}: ").lower()
        
        match whose:
            case "sh":
                shreetej.items.append((item["price"], item["item"]))
                shreetej.total += item["price"]
            case "ss":
                shubham.items.append((item["price"], item["item"]))
                shubham.total += item["price"]
            case "ia":
                ishaan.items.append((item["price"], item["item"]))
                ishaan.total += item["price"]
            case "vr":
                vaibhav.items.append((item["price"], item["item"]))
                vaibhav.total += item["price"]
            


tax_divided = order["tax"]/4
for roommate in roommates:
    roommate.items.append((tax_divided, "tax"))
    roommate.total += tax_divided

    print(roommate)

print("final: ",  [f"{r.name}, {r.total}" for r in roommates])
