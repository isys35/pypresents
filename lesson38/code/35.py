class Message(models.Model):
		content = models.TextField()
		name = models.CharField(max_length=20)
		email = models.EmailField()

		class Meta:
				abstract = True


class PrivateMessage(Message):
		user = models.ForeignKey(User, on_delete=models.CASCADE)
		# Переопределяем поле name
		name = models.CharField(max_length=40)
		# Удаляем поле email
		email = None