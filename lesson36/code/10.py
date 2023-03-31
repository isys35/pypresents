from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Rubric

def rubrics(request):
		RubricFormSet = modelsformset_factory(Rubric, fields=("name",), can_delete=True)
		if request.method == "POST":
				formset = RubricFormSet(request.POST)
				if formset.is_valid():
						formset.save()
						return redirect("bboard:index")
		else:
				formset = RubricFormSet()
		context = {"formset": formset}
		return render(request, "bboard/rubrics.html", context)