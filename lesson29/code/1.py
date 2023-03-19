>>> from bboard.models import Bb
>>> b = Bb.objects.get(pk=1)
>>> b.title
"Дача"
>>> b.content
"Два этажа , кирпич , свет , газ , канализация"
>>> b.price
10000.0
>>> b.pk
1