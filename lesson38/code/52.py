from django.db import models

class RubricManager(models.Manager):
		def get_queryset(self):
				return RubricQuerySet(self.model, using=self._db)

		def order_by_bb_count(self):
				return self.get_queryset().order_by_bb_count()