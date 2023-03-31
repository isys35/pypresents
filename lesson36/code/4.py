formset = RubricFormSet(
	initial=[{"name": "Новая рубрика"}, {"name":"Ещё одна новая рубрика"}]
	queryset=Rubric.objects.all()[0:5]
)