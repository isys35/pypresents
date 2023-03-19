>>> r = Rubric.objects.get(name="Мебель")
>>> b = Bb()
>>> b.rubric = r
>>> b.save()