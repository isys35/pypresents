Blog.objects.filter(entry__authors__name__isnull=True)