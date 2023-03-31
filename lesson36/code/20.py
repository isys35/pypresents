# forms.py
from django.forms import ModelForm
from .models import Bird

# A regular form, not a formset
class BirdForm(ModelForm):
    class Meta:
      model = Bird
      fields = [common_name, scientific_name]