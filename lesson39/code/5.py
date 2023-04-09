from .models import Rubric

class RubricMiddleware:
		def __init__(self, get_response):
				self.get_response = get_response

		def __call__(self, request):
				return self.get_response(request)

		def process_template_response(self, request, response):
				response.context_data["rubrics"] = Rubric.objects.all()
				return response