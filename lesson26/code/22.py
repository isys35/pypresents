from django.core import validators

class Bb(models.Model):
		title = models.CharField(max_length=50, validators=[validators.RegexValidator(regex="^.{4,}$")])