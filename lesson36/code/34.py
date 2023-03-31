from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME

from .models import Rubric

def rubrics(request):
		RubricFormSet = modelformset_factory(Rubric, fields("name",), can_order=True, can_delete=True)
		if request.method == "POST":
				formset = RubricFormSet(request.POST)
				if formset.is_valid():
						for form in formset:
								if form.cleaned_data:
										rubric = form.save(commit=False)
										rubric.order = form.cleaned_data[ORDERING_FIELD_NAME]
										rubric.save()
						return redirect("bboard:index")
	else:
			formset = RubricFormSet()
	context = {"formset": formset}
	return render(request, "bboard/rubrics.html", context)				