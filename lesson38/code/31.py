>>> from testapp.models import PrivateMessage
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username="editor")
>>> pm = PrivateMessage.objects.create(content="Hi", user=u)
>>> pm.content
"Hi"
>>> pm.user
<User: editor>