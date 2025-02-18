class Grpoup:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def remove_student(self, student):
        self._students.remove(student)

    def count_students(self):
        return len(self._students)

    def __str__(self):
        return f'Group {self.number}{self.name} with {len(self._students)} students'

    def __len__(self):
        return self.count_students()

    def __getitem__(self, item):
        return self._students[item]

    def __eq__(self, other):
        # return self.number == other.number and self.name == other.name
        return self._students == other._students

    def __contasins__(self, item):
        return item in self._students

    def __gt__(self, other):
        return len(self._students) > len(other._students)

    # метод складывания групп с именем и номером например Group 5B_3A with 7 students
    def __add__(self, other):
        if isinstance(other, list):
            new_group = Grpoup(self.name, self.number)
            new_group._students = self._students + other
        else:
            new_group_name = self.name
            new_group_number = self.number+other.number
            new_group = Grpoup(new_group_name, new_group_number)
            new_group._students = self._students + other._students
        return new_group

    @property
    def experiment(self):
        return len(self)


if __name__ == '__main__':
    # TODO: Define the class Student

    group_5b = Grpoup('B', 3)
    group_5b.add_student('Leo')
    group_5b.add_student('Lax')
    group_5b.add_student('Late')

    group_3a = Grpoup('A', 4)
    group_3a.add_student('Leo')
    group_3a.add_student('Lax')
    group_3a.add_student('Late')
    group_3a.add_student('Led')

    # print(group)
    # print(len(group))
    # print(group.count_students())
    print(group_5b)
    print(group_3a)
    print(group_3a == group_5b)
    print('exists' if 'Leo' in group_3a else 'not exists')
    print(group_3a > group_5b)
    print(group_3a.experiment)

    # общий список групп
    all_groups = group_5b + group_3a

    print(all_groups)

    all_groups += group_3a

    print(all_groups)

    all_groups += ['Lohn', 'Lane']
    print(all_groups)
