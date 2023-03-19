>>> Entry.objects.values_list('headline', flat=True).get(pk=1)
'First entry'