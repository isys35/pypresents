from django.db import models

class Blog(models.Model):
    # ...
    pass

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)