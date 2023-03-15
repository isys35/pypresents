from django.http import HttpResponse
from django.template import loader

from .models import Book

def index(request):
		template = loader.get_template('books/index.html')
		books = Book.objects.order_by("-published")
		context = {"books": books}
		return HttpResponse(template.render(context, request))