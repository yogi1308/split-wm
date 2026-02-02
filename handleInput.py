from objects import shreetej, shubham, ishaan, vaibhav, actions

def handleInput(whose, item, len_whose):
    price = round(item["price"] / len_whose, 5)
    match whose:
        case "sh":
            shreetej.items.append((price, item["item"]))
            shreetej.total += price
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": price})
        case "ss":
            shubham.items.append((price, item["item"]))
            shubham.total += price
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": price})
        case "ia":
            ishaan.items.append((price, item["item"]))
            ishaan.total += price
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": price})
        case "vr":
            vaibhav.items.append((price, item["item"]))
            vaibhav.total += price
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": price})