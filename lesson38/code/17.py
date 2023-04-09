# создадим курс
python = Course.objects.create(name="Python")

# создадим двух студентов
tom = Student.objects.create(name="Tom")
sam = Student.objects.create(name="Sam")

# создаем поступления студентов на курс
tom_python = Enrollment(student=tom, course=python,
                        date=date.today(), mark=5)
sam_python = Enrollment(student=sam, course=python,
                        date=date.today(), mark=4)
# сохраняем поступления в бд
tom_python.save()
sam_python.save()

# получаем все курсы у Toma
tom_courses = tom.courses.all()
print(tom_courses[0].name)  # python

# получим всех студентов курса по python
python_students = python.student_set.all()
print(python_students[0].name)  # Tom