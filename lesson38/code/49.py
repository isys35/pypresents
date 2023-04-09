from django.db import models

class RubricQuerySet(models.QuerySet):
		def order_by_bb_count(self):
			return self.annotate(cnt=models.Count("bb")).order_by("-cnt")