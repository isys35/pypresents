urlpatterns = [
    path('about/', GreetingView.as_view(greeting="G'day")),
]