class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + birth_year


input_1 = input()
input2 = input()
input_3 = input()

student = Student(input_1, input2, input_3)
print(student.id)
