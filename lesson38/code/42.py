class Rubric(models.Model):
		...
		bbs = RubricManager()

>>> # Теперь для доступа к диспетчеру записей исполь зуем атрибут
>>> # класса bbs
>>> Rubric.bbs.all()