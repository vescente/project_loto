class Group:

    # Static method - это метод, который не принимает экземпляр класса в качестве первого аргумента.
    @staticmethod
    def help():
        print('1. Add student to group')
        print('2. Remove student from group')
        print('3. Show group info')
        print('4. Show students list')
        print('5. Exit')

    @staticmethod
    def create_group_stat(n):
        # names = ['A', 'B', 'C', 'D', 'E']
        result = [Group(chr(65+i), i+1) for i in range(n) if i < 26]
        # for i in range(n):
        #     new_group = Group(names[i], i+1)
        #     result.append(new_group)

        return result

    # Class method - это метод, который принимает первым аргументом класс, а не экземпляр класса.
    @classmethod
    def create_group_class(cls, n):
        result = [cls(chr(65+i), i+1) for i in range(n) if i < 26]
        return result

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
            new_group = Group(self.name, self.number)
            new_group._students = self._students + other
        else:
            new_group_name = self.name
            new_group_number = self.number+other.number
            new_group = Group(new_group_name, new_group_number)
            new_group._students = self._students + other._students
        return new_group


class student_group(Group):
    pass


if __name__ == '__main__':

    # group_5b = Group('B', 3)
    # group_5b.add_student('Leo')
    # group_5b.add_student('Lax')
    # group_5b.add_student('Late')

    # Group.help()

    # gruops = Group.create_group_stat(5)

    # for g in gruops:
    #     print(g)

    # gruops = Group.create_group_class(5)
    # print(gruops)
    # for g in gruops:
    #     print(g)

    gruops = student_group.create_group_class(5)
    print(gruops)
    for g in gruops:
        print(g)

    gruops = student_group.create_group_stat(5)
    print(gruops)
    for g in gruops:
        print(g)
