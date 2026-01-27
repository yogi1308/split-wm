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
        return_str += f"{self.total:<10} FINAL\n"
        return return_str

shreetej = Roommate(name="shreetej", shortname="sh")
shubham = Roommate(name="shubham", shortname="ss")
ishaan = Roommate(name="ishaan", shortname="ia")
vaibhav = Roommate(name="vaibhav", shortname="vr")

roommates = [shreetej, shubham, ishaan, vaibhav]
actions = []    