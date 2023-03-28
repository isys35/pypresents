# urls.py
from django.urls import path
from books.views import PublisherListView

urlpatterns = [
    path('publishers/', PublisherListView.as_view()),
]