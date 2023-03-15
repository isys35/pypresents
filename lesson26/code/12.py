
class HomeWork(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name="homeworks")


....
# Получаем первую тему
first_subject = Subject.objects.first()
# Получаем доступ к связанным объявлениям через атрибут homeworks
# указанный в параметре related_name
hws = first_subject.homeworks.all()