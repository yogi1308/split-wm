from objects import shreetej, shubham, ishaan, vaibhav, actions

def handleInput(whose, item):
    match whose:
        case "sh":
            shreetej.items.append((item["price"], item["item"]))
            shreetej.total += item["price"]
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": item["price"]})
        case "ss":
            shubham.items.append((item["price"], item["item"]))
            shubham.total += item["price"]
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": item["price"]})
        case "ia":
            ishaan.items.append((item["price"], item["item"]))
            ishaan.total += item["price"]
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": item["price"]})
        case "vr":
            vaibhav.items.append((item["price"], item["item"]))
            vaibhav.total += item["price"]
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": item["price"]})
        case "-":
            pass
            # TODO
