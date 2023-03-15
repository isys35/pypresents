class Spare(models.Model):
		name = models.CharField(max_length=30)

class Machine(models.Model):
		name = models.CharField(max_length=30)
		spares = models.ManyToManyField(Spare)