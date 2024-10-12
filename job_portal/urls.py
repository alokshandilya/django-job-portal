from django.urls import path

from .views import detail, index

urlpatterns = [
    path("", index, name="home"),
    path("job/<int:id>", detail, name="detail"),
]
