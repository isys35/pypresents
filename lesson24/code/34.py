class Book(models.Model):
		name = models.CharField(max_length=100, verbose_name="Наименование")
		description = models.TextField(null=True, verbose_name="Onиcaниe", blank=True)
		price = models.FloatField(null=True, verbose_name="Цена", blank=True)
		published = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано", db_index=True)

class Meta:
		verbose_name_plural = "Объявления"
		verbose_name = "Объявление"
		ordering = ['-published']