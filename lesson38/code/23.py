>>> from testapp.models import Spare, Machine, Note
>>> m1 = Machine.objects.get(name="Тепловоз")
>>> s1 = Spare.objects.get(name="Шпилька")
>>> n1 = Note.objects.create(content="Самая бесполезная деталь", content_object=s1)
>>> n2 = Note.objects.create(content="В нём не используются шпильки", content_object=m1)
>>> n1.content_object.name
"Шпилька"
>>> n2.content_object.name
"Тепловоз"