# urls.py
from django.urls import path
from books.views import PublisherBookListView

urlpatterns = [
    path('books/<publisher>/', PublisherBookListView.as_view()),
]