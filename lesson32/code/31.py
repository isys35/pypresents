from django.urls import path
from books.views import AuthorDetailView

urlpatterns = [
    #...
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]