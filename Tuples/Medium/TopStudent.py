from collections import namedtuple

Student=namedtuple('Student',['name','age','grades'])

def top_student(students):
    print(students)
    return max(students, key= lambda s:sum(s.grades)/len(s.grades))

alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(Student)
print(alice)

print(top_student([alice, bob, charlie]))