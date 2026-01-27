from objects import shreetej, shubham, ishaan, vaibhav, actions

def handleInput(whose, item, len_whose):
    match whose:
        case "sh":
            shreetej.items.append((item["price"]/len_whose, item["item"]))
            shreetej.total += item["price"]/len_whose
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": item["price"]/len_whose})
        case "ss":
            shubham.items.append((item["price"]/len_whose, item["item"]))
            shubham.total += item["price"]/len_whose
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": item["price"]/len_whose})
        case "ia":
            ishaan.items.append((item["price"]/len_whose, item["item"]))
            ishaan.total += item["price"]/len_whose
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": item["price"]/len_whose})
        case "vr":
            vaibhav.items.append((item["price"]/len_whose, item["item"]))
            vaibhav.total += item["price"]/len_whose
            actions.append({"roommate": shreetej.name, "item": item["item"], "price": item["price"]/len_whose})
        case "-":
            pass
            # TODO
