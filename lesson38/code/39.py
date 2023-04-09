from django.db import models


class RubricManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().order_by("order", "name")

    def order_by_bb_count(self):
        return super().get_queryset().annotate(cnt=models.Count("bb")).order_by("-cnt")