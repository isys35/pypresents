from django.views.generic import DetailView
from books.models import Publisher

class PublisherDetailView(DetailView):

    context_object_name = 'publisher'
    queryset = Publisher.objects.all()