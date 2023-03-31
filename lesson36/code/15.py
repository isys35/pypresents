from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import Вb,Rubric

def bbs(request, rubric_id):
		BbsFormSet = inlineformset_factory(Rubric,Вb , form=BbForm, extra=l)
		rubric = Rubric.objects.get(pk=rubric_id)
		if request.method == "POST":
				formset = BbsFormSet(requst.POST, instance=rubric)
				if formset.is_valid():
						formset.save()
						return redirect("bboard:index")

		else:
				formset = BbsFormSet(instance=rubric)
		context = {"formset": formset, "current_rubric": rubric}
		return render(request, "bboard/bbs.html", context)