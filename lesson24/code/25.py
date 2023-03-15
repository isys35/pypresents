from django.http import HttpResponse
from .models import Book

def index(request):
			s = 'Список книг\r\n\r\n\r\n'
			for b in Book.objects.order_by('-published'):
					s += b.name + '\r\n' + b.description + '\r\n\r\n'
			return HttpResponse(s, content_type='text/plain; charset=utf-8')