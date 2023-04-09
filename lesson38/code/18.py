# создадим курсы
django = Course.objects.create(name="Django")
python = Course.objects.create(name="Python")
java = Course.objects.create(name="Java")

# создадим студента
bob = Student.objects.create(name="Bob")

# добавляем курс для студента bob
bob.courses.add(django, through_defaults={"date": date.today(), "mark": 5})
# создаем курс для студента bob
bob.courses.create(name="C++", through_defaults={"date": date.today(), "mark": 4})

# получаем все курсы Boba
print(bob.courses.all().values_list())  # <QuerySet [(11, 'Django'), (14, 'C++')]>

# переустанавливаем курсы для студента bob
bob.courses.set([python, java], through_defaults={"date": date.today(), "mark": 4})

# снова получаем все курсы Boba
print(bob.courses.all().values_list())  # <QuerySet [(12, 'Python'), (13, 'Java')]>