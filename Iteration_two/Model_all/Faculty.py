# Faculty class is made, so that the instructors can only book rooms (after deadline) that belongs to their faculty

class Faculty:

    def __init__(self, name: str, list_institutes: []):
        self.name = name
        self.list_institutes = list_institutes

    def __str__(self):
        return f"Name: {self.name}, Institutes: {self.list_institutes}"


# Should faculties be a list?
# class Faculties:
# __faculty: list[str] = []  # a private attribute is prefixed by two underscores in Python

# def __init__(self=None):
# self.__faculty: list[str] = []  # a new object of the type faculties is created as an empty list

# def __str__(self):
# output = f"Number of faculty's: {len(self.__faculty)} \n"
# output = output + "The faculties are \n"
# output += ', '.join(str(h) for h in self.__faculty)
# return output

# faculty_list = [Faculty('DTU'), Faculty('KU SUND'), Faculty('KU SCIENCE')]
# here each faculty is an instance

# faculty_list = Faculties('DTU', 'KU SUND', 'KU SCIENCE']
# here each instance is a list of faculties
