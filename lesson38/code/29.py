from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
		content = models.TextField()

class PrivateMessage(Message):
		user = models.ForeignKey(User, on_delete=models.CASCADE)