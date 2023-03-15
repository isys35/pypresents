from django.contrib import admin
from django.urls import path
from books.views import index

urlpatterns = [
		path('books/', index),
		path('admin/', admin.site.urls),
]
