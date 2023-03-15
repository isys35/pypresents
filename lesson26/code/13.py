class HomeWork(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_query_name="entry")


....

subjects = Subject.objects.filter(entry__name='Python')