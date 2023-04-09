from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contentypes.models import ContentType

class Note(models.Model):
		content = models.TextField()
		content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
		object_id = models.PositiveIntegerField()
		content_object = GenericForeignKey(ct_field="content_type", fk_field="object_id")