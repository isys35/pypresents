>>> u = User.objects.get(username='fsmith')
>>> freds_department = u.employee.department