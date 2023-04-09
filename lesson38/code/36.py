class Message(models.Model):

		class Meta:
				abstract = True
				ordering = ['name']


class PrivateMessage(Message):
		...
		class Meta(Message.Meta):
				pass