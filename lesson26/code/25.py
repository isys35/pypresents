from django.db import models

class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])