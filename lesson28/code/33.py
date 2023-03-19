e = Entry.objects.get(id=10)
e.comments_on = False
e.save()