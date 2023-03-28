app_name = "courses"

urlpatterns = [
    path("", views.courses, name="list"),
    path("create",  views.create_course, name="create")
]