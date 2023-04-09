# фильтрация
students = Student.objects.filter(
    courses__name="Python",
    enrollment__mark__lte=4)

print(students.values_list())