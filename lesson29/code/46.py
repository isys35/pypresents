Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')