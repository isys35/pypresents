class PrivateMessage(Message):
		...
		message = models.OneToOneField(Message, on_delete=models.CASCADE, parent_link=True)