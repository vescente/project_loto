class Grpoup:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def __str__(self):
        return f'Group {self.number}{self.name} with {len(self._students)} students'


if __name__ == '__main__':
    # TODO: Define the class Student
    leo = 'Leo'
    max = 'Max'
    kate = 'Kate'

    group = Grpoup('B', 5)
    group.add_student(leo)
    group.add_student(max)
    group.add_student(kate)

    print(group)
    print(str(group))
