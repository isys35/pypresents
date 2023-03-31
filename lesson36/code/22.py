# views.py
from django.views.generic import ListView, TemplateView # Import TemplateView
from .models import Bird
from .forms import BirdFormSet # Import the formset

class BirdListView(ListView):
    model = Bird
    template_name = "bird_list.html"

# View for adding birds
class BirdAddView(TemplateView):
    template_name = "add_bird.html"

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        formset = BirdFormSet(queryset=Bird.objects.none())
        return self.render_to_response({'bird_formset': formset})