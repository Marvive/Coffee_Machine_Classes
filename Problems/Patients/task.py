class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here
    def __str__(self):
        return f"{self.name} {self.last_name}. {self.age}"

    def __repr__(self):
        return f"Object of the class Patient. name: {self.name}, last_name: {self.last_name}, age: {self.age}"


# newp = Patient("michael", "marvive", 28)
# print(newp)
# print(repr(newp))