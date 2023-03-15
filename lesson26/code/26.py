from django.core.exceptioms import ValidationError

class MinMaxValueValidator:
		def __init__(self, min_value, max_value):
				self.min_value = min_value
				self.max_value = max_value

		def __call__(self, value):
				if val < self.min_value or val > self.max_value:
						raise ValidationError("Введённое число должно находится в диапозоне от %(min)s до %(max)s",
																	code="out_of_range",
																	params={"min": self.min_value, "max": self.max_value})

