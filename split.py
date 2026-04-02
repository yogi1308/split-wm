import json
from handleInput import handleInput
from objects import roommates, actions

with open("bill.json", "r") as f:
    data = f.read()

order = json.loads(data)


def log():
    for roommate in roommates:
        roommate.items.append((tax_divided, "tax"))
        roommate.total += tax_divided

        print("\n")
        print(roommate)


print()
i = 0
history = []
while i < len(order["items"]):
    item = order["items"][i]
    print(f"QTY: {item['qty']}   PRICE: ${item['price']}   ITEM: {item['item']}")
    whose = input().lower().replace(" ", "").split(",")
    while not (
        whose == ["-"] or all(w in [r.shortname for r in roommates] for w in whose)
    ):
        print(
            "Invalid input", whose, "  can only be - ", [r.shortname for r in roommates]
        )
        whose = input().lower().replace(" ", "").split(",")

    if "-" in whose:
        if i > 0:
            i -= 1
            last_whose = history.pop()
            for _ in last_whose:
                actions.pop()
            for name in last_whose:
                for r in roommates:
                    if r.shortname == name:
                        price, _ = r.items.pop()
                        r.total -= price
            print(f"Undid: {order['items'][i]['item']}")
        else:
            print("Cannot undo at start")
        continue

    elif "log" in whose:
        log()
        continue

    history.append(whose)
    for individual in whose:
        handleInput(individual, item, len(whose))
    i += 1


tax_divided = round(order["tax"] / len(roommates), 5)
log()

print("final: ", [f"{r.name}, {r.total:.5f}" for r in roommates])
