class Rubric(models.Model):
    ...
    order = models.SmallIntegerField(default=0, db_index=True)
    ...

    class Meta:
        ...
        ordering = ["order", "name"]