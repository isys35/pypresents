class HomeWork(models.Model):
    subject = models.ForeignKey("Subject", on_delete=models.PROTECT)


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")