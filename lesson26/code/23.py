from django.core import validators

class Bb(models.Model):
		title = models.CharField(max_length=50, verbose_name='Toвap',
					validators= [validators.RegexValidator(regex="^.{4,}$")],
					error_messages= {"invalid":"Неправильное название товара"})