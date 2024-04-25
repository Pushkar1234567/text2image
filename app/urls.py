from django.urls import path
from . import views

urlpatterns = [
    path('app/',views.test, name="test"),
    path('generate_image/',views.generate_image_view, name="generate_image")
]