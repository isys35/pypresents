# views.py
from django.views.generic import ListView
from .models import Bird

class BirdListView(ListView):
    model = Bird
    template_name = "bird_list.html"