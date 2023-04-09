# создадим курсы
django = Course.objects.create(name="Django")
python = Course.objects.create(name="Python")

# создадим студента
tim = Student.objects.create(name="Tim")

# устанавливаем курсы для студента Tim
tim.courses.set([python, django], through_defaults={"date": date.today(), "mark": 4})

print(tim.courses.all().values_list())  # <QuerySet [(16, 'Python'), (15, 'Django')]>

# удаляем один курс
tim.courses.remove(django)
print(tim.courses.all().values_list())  # <QuerySet [(16, 'Python')]>

# удаляем все курсы
tim.courses.clear()
print(tim.courses.all().values_list())  # <QuerySet []>