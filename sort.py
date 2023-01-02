students = ("Squidward", "Sandy", "Spongebob", "Mr. Krabs")

# students.sort(reverse= True)
# sorted_students = sorted(students, reverse=True)
#
# for i in sorted_students:
#     print(i)

# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr. Krabs", "C", 78)]
# grade = lambda grades:grades[1]
# age = lambda ages:ages[2]
# students.sort(key=grade)
#
# for i in students:
#     print(i)
#
# students.sort(key=age)
#
# for i in students:
#     print(i)

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

age = lambda ages:ages[2]

sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)








