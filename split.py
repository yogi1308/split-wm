import json
from handleInput import handleInput
from objects import roommates

with open('bill.json', 'r') as f:
    data = f.read()

order = json.loads(data)

print()
for item in order["items"]:
    print(f"QTY: {item['qty']}   PRICE: ${item['price']}   ITEM: {item['item']}")
    whose = input().lower().split(", ")
    while not (whose == ["-"] or all(w in [r.shortname for r in roommates] for w in whose)):
        print("Invalid input", whose, "  can only be - ", [r.shortname for r in roommates])
        whose = input().lower().split(", ")
    
    for individual in whose:
        handleInput(individual, item, len(whose))            
    # TODO instead of handling each quantity individually let users enter an array of strings


tax_divided = order["tax"]/4
for roommate in roommates:
    roommate.items.append((tax_divided, "tax"))
    roommate.total += tax_divided

    print("\n")
    print(roommate)

print("final: ",  [f"{r.name}, {r.total}" for r in roommates])
