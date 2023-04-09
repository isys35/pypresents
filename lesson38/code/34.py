class Message(models.Model):
		...
		class Meta:
				abstract = True


class PrivateMessage(Message):
		...