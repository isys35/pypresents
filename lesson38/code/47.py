class Bb(models.Model):
		...
		objects = models.Manager()
		by_price = BbManager()