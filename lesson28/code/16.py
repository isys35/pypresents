>>> from django.contrib.auth.models import User
>>> from testapp.models import AdvUser
>>> u = User.objects.get(username="admin")
>>> au = AdvUser.objects.create(user=u)