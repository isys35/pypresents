from django.db import models

class BbManager(models.Manager):
		def get_queryset(self):
				return super().get_queryset().order_by("price")