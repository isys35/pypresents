class Rubric(models.Model):
		...
		objects = models.Manager()
		bbs = RubricManager()