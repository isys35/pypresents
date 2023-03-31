from django.forms import modelformset_factory
from .models import Rubric

RubricFormSet = modelformset_factory(Rubric, fields=('name',))