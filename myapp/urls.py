from django.urls import path
from .views import receive_data

urlpatterns = [
    path("submit/", receive_data, name="receive_data"),
]
