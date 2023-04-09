class RevRubric(Rubric):
		class Meta:
			proxy = True
			ordering = ["name"]