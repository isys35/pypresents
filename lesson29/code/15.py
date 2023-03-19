try:
    p = Article.objects.order_by('title', 'pub_date')[0]
except IndexError:
    p = None